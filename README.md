# 🧠 Local Code Generator using Ollama (codellama:7b)

A Python-based desktop automation tool that allows you to generate Java code from any problem statement using a locally running LLM via **Ollama**.  
The tool listens for keyboard shortcuts, picks up copied text from your clipboard, sends it to a local AI model (`codellama:7b`), and automatically puts the generated code back into your clipboard.

> Fully offline. Fast. Private. No API keys required.

---

## ✨ Features

- Works completely **offline** using Ollama
- Uses **Code Llama 7B** locally
- Hotkey-based trigger system
- Clipboard-based automation
- Generates Java code automatically
- Can run completely in the **background**
- No cloud usage — full privacy
- Easy setup on Windows

---

## 🚀 How It Works

1. You copy any coding problem (Ctrl + C)
2. Press **Ctrl + Alt + A**
3. Code is generated using the local LLM (Ollama)
4. Output code is copied back to clipboard
5. Press **Ctrl + Alt + D** to exit the tool

---

## 🛠️ Requirements

### Software

- Python 3.10 or 3.11
- Ollama installed
- `codellama:7b` model pulled

### Python Libraries

- `keyboard`
- `pyperclip`
- `requests`

---

## 📦 Setup Instructions

### 1. Install Ollama

Download from:  
https://ollama.com

Verify installation:

```bash
ollama --version
```

---

### 2. Pull Code Llama Model

```bash
ollama pull codellama:7b
```

Test the model:

```bash
ollama run codellama:7b "Write Java code to print Hello World"
```

---

### 3. Install Python Dependencies

```bash
pip install keyboard pyperclip requests
```

---

### 4. Run Normally

```bash
python offline_cheating.py
```

---

## 🖥️ Run in Background (No Console Window)

### Start in background:

PowerShell command:

```powershell
Start-Process "pythonw.exe" -ArgumentList "offline_cheating.py" -WindowStyle Hidden
```

### Stop background process:

```powershell
Stop-Process -Name "pythonw" -Force
```

> You must run this command from the directory where `offline_cheating.py` exists.

---

## ⌨️ Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Generate code | Ctrl + Alt + A |
| Exit program | Ctrl + Alt + D |

---

## 🧩 Code Structure

```text
offline_cheating.py     Main program
README.md               Project documentation
```

---

## 🧪 Test API Connection (Optional)

Verify Python → Ollama communication:

```bash
py -3.11 -c "import requests; print(requests.post('http://localhost:11434/api/generate', json={'model':'codellama:7b','prompt':'Write a Java program','stream':False}).json()['response'])"
```

---

## 🔐 Privacy

- 100% Offline
- No internet usage
- No telemetry
- No tracking
- No API tokens

---

## ⚠️ Disclaimer

This project is intended for **educational and experimental use only**.  
Do not use this tool for academic dishonesty or violating institutional rules.

---

## 🧑‍💻 Author

**Abhishek Ghume**  
Electronics & Telecommunication Engineering Student  
VIT Pune  

---
