# ========================= IMPORTS ========================= #

import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from rapidfuzz import fuzz

# ========================= PAGE CONFIG ========================= #

st.set_page_config(
    page_title="HorizonTechX AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================= NLTK ========================= #

@st.cache_resource
def download_nltk():

    nltk.download("punkt")

    nltk.download("stopwords")

download_nltk()

# ========================= SESSION ========================= #

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# ========================= LOAD FAQ ========================= #

@st.cache_data
def load_data():

    return pd.read_csv("faq.csv")

df = load_data()

df["Question"] = df["Question"].astype(str)

df["Answer"] = df["Answer"].astype(str)

# ========================= NLP ========================= #

stop_words = set(stopwords.words("english"))

def preprocess(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9 ]',
        '',
        text
    )

    words = word_tokenize(text)

    words = [

        word for word in words

        if word not in stop_words
    ]

    return " ".join(words)

df["Processed"] = df["Question"].apply(
    preprocess
)

# ========================= MODEL ========================= #

@st.cache_resource
def train_model():

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(
        df["Processed"]
    )

    return vectorizer, X

vectorizer, X = train_model()

# ========================= RESPONSE ========================= #

def get_response(user_question):

    processed_question = preprocess(
        user_question
    )

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarity = cosine_similarity(
        user_vector,
        X
    )

    best_match = np.argmax(similarity)

    score = similarity[0][best_match]

    best_question = df.iloc[best_match][
        "Question"
    ]

    fuzz_score = fuzz.ratio(
        user_question.lower(),
        best_question.lower()
    )

    if score > 0.15 or fuzz_score > 55:

        return df.iloc[best_match][
            "Answer"
        ]

    return (
        "Sorry, I couldn't understand "
        "your question. Please try "
        "asking differently."
    )

# ========================= CSS ========================= #

st.markdown("""

<style>

/* ================= APP ================= */

.stApp {

    background:
    radial-gradient(
        circle at top left,
        #1e3a8a 0%,
        transparent 25%
    ),

    radial-gradient(
        circle at bottom right,
        #0f766e 0%,
        transparent 25%
    ),

    linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );

    color:white;
}

/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {

    background:
    rgba(2,6,23,0.96);

    border-right:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(20px);
}

/* ================= TITLE ================= */

.main-title {

    text-align:center;

    font-size:78px;

    font-weight:900;

    margin-top:20px;

    margin-bottom:10px;

    background:
    linear-gradient(
        90deg,
        #60a5fa,
        #38bdf8,
        #14b8a6
    );

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;
}

.sub-title {

    text-align:center;

    font-size:24px;

    color:#94a3b8;

    margin-bottom:40px;

    line-height:1.8;
}

/* ================= CHAT ================= */

.stChatMessage {

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius:22px;

    padding:18px;

    margin-bottom:18px;

    backdrop-filter:blur(20px);

    box-shadow:
    0px 8px 30px rgba(0,0,0,0.2);
}

/* ================= CHAT INPUT ================= */

.stChatInputContainer {

    position:fixed !important;

    bottom:20px;

    left:320px;

    right:110px;

    z-index:999;

    background:
    rgba(15,23,42,0.92);

    border-radius:25px;

    border:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter:blur(20px);

    padding:10px;
}

/* ================= MIC BUTTON ================= */

#mic-btn {

    position:fixed;

    bottom:28px;

    right:25px;

    width:70px;

    height:70px;

    border-radius:50%;

    border:none;

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #06b6d4
    );

    color:white;

    font-size:26px;

    font-weight:bold;

    cursor:pointer;

    z-index:999999;

    box-shadow:
    0px 6px 20px
    rgba(37,99,235,0.35);

    transition:0.3s;
}

#mic-btn:hover {

    transform:scale(1.08);
}

/* ================= SCROLLBAR ================= */

::-webkit-scrollbar {

    width:8px;
}

::-webkit-scrollbar-thumb {

    background:#334155;

    border-radius:10px;
}

/* ================= SPACE ================= */

.main .block-container {

    padding-bottom:140px;
}

</style>

""", unsafe_allow_html=True)

# ========================= SIDEBAR ========================= #

st.sidebar.markdown(
    "## 🤖 HorizonTechX AI"
)

st.sidebar.write(
    "Your Intelligent AI FAQ Assistant"
)

voice_reply = st.sidebar.toggle(
    "🔊 Voice Reply",
    value=True
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "### ⚡ Features"
)

st.sidebar.markdown("""

- NLP FAQ Search
- Browser Voice Chat
- AI Chat Experience
- Fast Responses
- Smart Matching
- Modern UI/UX
- Voice Assistant
- Download Chat

""")

# ========================= DOWNLOAD CHAT ========================= #

chat_text = ""

for sender, message in st.session_state.chat_history:

    chat_text += (
        f"{sender}: {message}\n"
    )

st.sidebar.download_button(

    label="📥 Download Chat",

    data=chat_text,

    file_name="chat_history.txt",

    mime="text/plain",

    use_container_width=True
)

# ========================= CLEAR CHAT ========================= #

if st.sidebar.button(
    "🗑️ Clear Chat",
    use_container_width=True
):

    st.session_state.chat_history = []

    st.rerun()

# ========================= TITLE ========================= #

st.markdown("""

<div class="main-title">
    HorizonTechX AI
</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="sub-title">
    Industry-level AI FAQ Assistant with intelligent NLP,
    browser voice interaction, and modern chatbot experience.
</div>

""", unsafe_allow_html=True)

# ========================= DEFAULT MESSAGE ========================= #

if len(st.session_state.chat_history) == 0:

    st.session_state.chat_history.append(
        (
            "assistant",
            "👋 Hello! Welcome to HorizonTechX AI. How can I assist you today?"
        )
    )

# ========================= CHAT HISTORY ========================= #

for sender, message in st.session_state.chat_history:

    with st.chat_message(sender):

        st.markdown(message)

# ========================= CHAT INPUT ========================= #

user_input = st.chat_input(
    "Ask anything..."
)

# ========================= PROCESS CHAT ========================= #

if user_input:

    st.session_state.chat_history.append(
        ("user", user_input)
    )

    response = get_response(
        user_input
    )

    st.session_state.chat_history.append(
        ("assistant", response)
    )

    st.rerun()

# ========================= LAST RESPONSE ========================= #

last_response = ""

if len(st.session_state.chat_history) > 0:

    last_sender, last_message = \
        st.session_state.chat_history[-1]

    if last_sender == "assistant":

        last_response = last_message

# ========================= VOICE JS ========================= #

voice_reply_js = (
    "true"
    if voice_reply
    else "false"
)

safe_last_response = (
    last_response
    .replace("`", "")
    .replace("'", "")
    .replace("\n", " ")
)

st.components.v1.html(f"""

<button id="mic-btn">
🎤
</button>

<script>

const voiceReply = {voice_reply_js};

const micBtn =
document.getElementById(
    "mic-btn"
);

let recognition;

let listening = false;

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if(!SpeechRecognition){{

    alert(
        "Speech Recognition not supported in this browser"
    );
}}

else {{

    recognition =
        new SpeechRecognition();

    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.lang = "en-US";

    micBtn.onclick = () => {{

        if(!listening) {{

            recognition.start();

            listening = true;

            micBtn.innerHTML = "🔴";
        }}

        else {{

            recognition.stop();

            listening = false;

            micBtn.innerHTML = "🎤";
        }}
    }};

    recognition.onresult = (event) => {{

        const transcript =
            event.results[0][0].transcript;

        const textarea =
            window.parent.document
            .querySelector(
                'textarea'
            );

        if(textarea) {{

            textarea.focus();

            const nativeInputValueSetter =
                Object.getOwnPropertyDescriptor(
                    window.HTMLTextAreaElement
                    .prototype,
                    "value"
                ).set;

            nativeInputValueSetter.call(
                textarea,
                transcript
            );

            textarea.dispatchEvent(
                new Event(
                    'input',
                    {{
                        bubbles:true
                    }}
                )
            );

            // ================= AUTO SEND ================= //

            setTimeout(() => {{

                const forms =
                    window.parent.document
                    .querySelectorAll(
                        "form"
                    );

                forms.forEach((form) => {{

                    const submitButton =
                        form.querySelector(
                            'button[type="submit"]'
                        );

                    if(submitButton) {{

                        submitButton.click();
                    }}
                }});

            }}, 1000);
        }}

        listening = false;

        micBtn.innerHTML = "🎤";
    }};

    recognition.onerror = (
        event
    ) => {{

        console.log(
            event.error
        );

        listening = false;

        micBtn.innerHTML = "🎤";
    }};
}}

function speak(text) {{

    if(!voiceReply) return;

    if(!text) return;

    window.speechSynthesis.cancel();

    const speech =
        new SpeechSynthesisUtterance(
            text
        );

    speech.lang = "en-US";

    speech.rate = 1;

    speech.pitch = 1;

    speech.volume = 1;

    window.speechSynthesis.speak(
        speech
    );
}}

setTimeout(() => {{

    speak(`{safe_last_response}`);

}}, 1200);

</script>

""", height=120)