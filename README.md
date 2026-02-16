# 🏠 UrbanRoof Property Inspection AI

AI-powered property inspection assistant built using **Mistral-7B-Instruct-v0.2** via HuggingFace Inference API.

This system helps identify potential moisture, dampness, leakage, and structural concerns by generating structured, inspection-focused responses.

---

## 🚀 Model Information

- **LLM Used:** `mistralai/Mistral-7B-Instruct-v0.2`
- **Provider:** HuggingFace
- **Inference Method:** Hosted Inference API (No local model download)
- **Architecture:** Transformer-based Large Language Model (7B parameters)

Model Link:  
https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

---

## 🧠 Features

✅ Structured inspection-style responses  
✅ Controlled, professional tone  
✅ No pricing or guarantee assumptions  
✅ Clarifying diagnostic questions  
✅ Safe next-step recommendations  
✅ Fast response (No GPU required)  

---


## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/UrbanRoof-Property-AI.git
cd UrbanRoof-Property-AI

python -m venv venv
venv\Scripts\activate   # Windows

python app.py


flask (optional if using API backend)
huggingface_hub
python-dotenv
