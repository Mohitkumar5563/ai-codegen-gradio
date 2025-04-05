# 🤖 AI Code Generation Project

This project is an **AI-powered Code Generation Tool** built using **CodeGen model**, integrated into a simple web UI using **Gradio**. You can input prompts like "write a bubble sort function" and the AI will generate Python code instantly.

## 🚀 Features

- Code generation from text prompts
- Runs on Google Colab (with Tesla T4 GPU support)
- Lightweight, fast inference
- Easy-to-use web interface with Gradio
- Model: CodeGen (Salesforce/codegen-350M-multi)

## 📁 Files

- `app.py` – Main app with Gradio interface
- `model_loader.py` – Loads the model and tokenizer
- `interface.py` – Frontend logic
- `requirements.txt` – Dependencies to run locally (optional)

## 🧠 Example Prompt


# 🌐 How to Run (on Colab)

1. Open `app.py` in Colab
2. Run all cells
3. The Gradio interface will appear to generate code!

## 📦 Future Enhancements

- Support more models (Code LLaMA, StarCoder, etc.)
- Add download/save option for generated code
- Improve prompt understanding

----
