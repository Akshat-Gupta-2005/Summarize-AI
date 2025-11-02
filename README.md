# Summarize-AI
# 📝 Age-Specific Summarizer

> Summarize any text into a simplified version that can be understood by a specific age group using Hugging Face and LangChain.

## 📌 Project Overview

**Age-Specific Summarizer** is a Python application that generates age-appropriate summaries of any text. By combining Hugging Face Transformers with LangChain, it allows users to simplify complex content for a target audience.

- **Purpose**: Make text accessible and easy to understand for different age groups.  
- **Use-case**: Teachers, parents, students, or content creators who want simplified explanations.  
- **Target users**: Educators, students, writers, and anyone needing age-specific summaries.

## 🚀 Features

- 🔹 Simplifies text according to a user-specified age group  
- 🔹 Uses Hugging Face BART summarization model  
- 🔹 Integrated with LangChain for structured prompt handling  
- 🔹 Simple command-line interface for quick usage  

## 🛠️ Tech Stack

| Layer           | Tools / Libraries                       |
|-----------------|----------------------------------------|
| **Language**    | Python                                 |
| **NLP / ML**    | Hugging Face Transformers, LangChain  |
| **Summarization** | Facebook BART (`facebook/bart-large-cnn`) |
| **Utilities**   | torch, torchvision, torchaudio        |

## 📚 Libraries & Dependencies

- `transformers` – Hugging Face models  
- `langchain` – LLM chaining and prompt management  
- `langchain-huggingface` – LangChain integration with Hugging Face  
- `torch`, `torchvision`, `torchaudio` – PyTorch libraries for backend support  

## 🏧 Project Structure
```
/
├── main.py # Entry point of the project
├── requirements.txt # Python dependencies
├── README.md
```


## ⚙️ Environment Setup

1. Create a Python virtual environment:
```bash
python -m venv venv
```
2. Activate the environment:
```
# Windows
./venv/Scripts/activate

# macOS/Linux
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Login to Hugging Face (to access models):
```
huggingface-cli login
```
5. Run the project:
```
python main.py
```

## 📡 Workflow & Pipeline

- Summarization Pipeline
    - Uses Hugging Face BART model for text summarization.

- LangChain Integration
    - Wraps the summarization model in LangChain to handle prompts and structured outputs.

- Age-Specific Summarization
    - Accepts user input for target age and text.
    - Generates a simplified summary suitable for the specified age.

## 🔎 Example Usage
```
Enter text to summarize:
"The solar system consists of the Sun and all the objects that orbit it, including planets, moons, and asteroids."

Enter target age for simplification:
10

🔹 **Generated Summary:**
"The solar system has the Sun at the center, and planets, moons, and asteroids go around it."
```
## 🧑‍💻 Concepts Learned

- Building NLP pipelines with Hugging Face Transformers
- Using LangChain for prompt management and LLM chains
- Simplifying text dynamically based on user input
- Working with Python virtual environments and dependency management

## 🤝 Contributing

Pull requests are welcome! Open an issue to discuss improvements or features.
#
