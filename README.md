# 🧠 Reddit Depression Detection using Transformer Models

A Natural Language Processing (NLP) project for automatic depression detection from Reddit posts using transformer-based language models.

The project compares multiple pretrained transformer architectures and provides an interactive Gradio interface for real-time prediction.

---

## Overview

This project aims to classify Reddit posts into:

- 🟢 Non-Depressed
- 🔴 Depressed

using fine-tuned transformer models trained on Reddit text.

---

## Models

| Model | Purpose |
|-------|---------|
| MiniLM | Depression Classification |
| ELECTRA | Depression Classification |

---

## Features

- Depression detection from Reddit posts
- Fine-tuned MiniLM model
- Fine-tuned ELECTRA model
- Interactive Gradio interface
- Model comparison
- Transformer-based NLP pipeline

---

## Project Structure

```text
reddit-depression-detection-transformers/

├── Models/
│   ├── nreimers MiniLM Model/
│   └── saved_model_electra/
│
├── Mini LM Model.ipynb
├── electra-small-discriminator.ipynb
├── GUI.ipynb
├── Gradio.py
│
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/reddit-depression-detection-transformers.git

cd reddit-depression-detection-transformers

pip install -r requirements.txt
```

---

## Run

```bash
python Gradio.py
```

---

## Technologies

- Python
- PyTorch
- Hugging Face Transformers
- MiniLM
- ELECTRA
- Gradio
- Scikit-learn
- Pandas

---

## Future Improvements

- Larger multilingual dataset
- Explainable AI (XAI)
- Confidence visualization
- Multi-class mental health detection
- Web deployment

---

## License

MIT License