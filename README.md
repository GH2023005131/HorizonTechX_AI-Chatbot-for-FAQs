# 🤖 HorizonTechX AI – Intelligent FAQ Chatbot

HorizonTechX AI is a professional AI-powered FAQ chatbot developed using Python and Streamlit.  
The project uses Natural Language Processing (NLP) techniques such as TF-IDF Vectorization, Cosine Similarity, and Fuzzy Matching to intelligently understand and answer user queries.

It provides a modern chatbot interface with voice interaction, authentication, downloadable chat history, and a professional UI/UX experience.

---

# 🚀 Features

- 🔐 User Login Authentication
- 💬 Modern ChatGPT-style Chat Interface
- 🎤 Voice Input (Speech Recognition)
- 🔊 Voice Reply (Text-to-Speech)
- 🧠 NLP-based FAQ Matching
- ⚡ Fast Responses using TF-IDF & Cosine Similarity
- 🔍 Typo Handling using RapidFuzz
- 📥 Download Chat Feature
- 🗑️ Clear Chat Option
- 🌙 Professional Dark Glassmorphism UI
- 📱 Responsive Layout
- ☁️ Streamlit Cloud Deployable

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- NLTK
- Scikit-learn
- RapidFuzz
- SpeechRecognition
- pyttsx3

---

# 🧠 NLP Techniques Used

## 1. Text Preprocessing
- Lowercasing
- Stopword Removal
- Tokenization
- Special Character Removal

## 2. TF-IDF Vectorization
Converts text into numerical vectors based on word importance.

## 3. Cosine Similarity
Measures similarity between user queries and FAQ questions.

## 4. Fuzzy Matching
Handles spelling mistakes and similar words using RapidFuzz.

---

# 📂 Project Structure

```bash
HorizonTechX_AI/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   └── logo.png
│
├── chat_history/
│
├── downloads/
│
├── app.py
├── faq.csv
├── users.json
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/HorizonTechX-AI.git
cd HorizonTechX-AI
```

---

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Project

```bash
streamlit run app.py
```

---

# 🔑 Login Credentials

Example:

```json
{
  "admin": "admin123"
}
```

Stored inside:

```bash
users.json
```

---

# 📄 FAQ Dataset

The chatbot uses a custom FAQ dataset stored in:

```bash
faq.csv
```

Format:

```csv
"question","answer"
```

Example:

```csv
"what is python","Python is a high-level programming language."
```

---

# 🎤 Voice Features

## Voice Input
Uses Google Speech Recognition API to convert speech into text.

## Voice Reply
Uses pyttsx3 Text-to-Speech engine for AI voice responses.

---

# 🌐 Deployment

This project can be deployed easily using:

- Streamlit Cloud
- Render
- Railway
- Hugging Face Spaces

---

# 📸 UI Highlights

- Professional Dark Theme
- Glassmorphism Design
- ChatGPT-style Input Area
- Floating Mic Button
- Animated Listening Indicator
- Responsive Sidebar

---

# 🎯 Internship Task Coverage

✅ Collect and preprocess FAQ data  
✅ Similarity matching using NLP  
✅ Generate chatbot responses  
✅ Interactive chatbot interface  

---

# 📈 Future Improvements

- Multi-language Support
- OpenAI API Integration
- AI Summarization
- Database Integration
- User Chat Analytics
- Real-time AI Responses

---

# 👨‍💻 Developed By

**Akshith Mikki**

---

# 📜 License

This project is developed for educational and internship purposes.