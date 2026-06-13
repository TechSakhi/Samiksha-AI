# Samiksha AI: Universal Review & comment Analyzer

Transforming messy, multi-platform e-commerce customer feedback into structured, actionable business intelligence using advanced LLM reasoning and custom data visualization.

---

## Overview

**Samiksha AI** is an enterprise-grade customer feedback analyzer agent. It dynamically ingests raw user reviews scraped from e-commerce platforms (like Flipkart), filters out spam and background noise, handles complex linguistic nuances like sarcasm, and structures the data into an automated, highly visual Business Executive Report Card.

Instead of relying on generic star ratings, Samiksha AI performs deep **Aspect-Based Sentiment Analysis (ABSA)** to extract concrete product drawbacks and highlights, enabling business owners to make immediate product development updates.

---

##  Key Features

* **Dynamic Data Ingestion:** Automated extraction and ingestion of multi-page customer reviews from e-commerce platforms.
* **Context-Aware Noise & Spam Filtering:** Leverages Gemini's high context window to separate irrelevant complaints (e.g., shipping issues) from actual product quality issues.
* **Advanced Sarcasm Detection:** Accurately flags and correctly interprets sarcastic user comments that typically break traditional rule-based sentiment tools.
* **Aspect-Based Sentiment Mapping:** Dissects sentences to isolate specific sentiments regarding parameters like product fragrance, texture, longevity, or safety.
* **Automated Executive Insights:** Generates a real-time analytics dashboard presenting categorical distribution and clear, actionable bullet points for business enhancement.

---

##  Tech Stack

* **Core Language:** Python 3.13
* **LLM Orchestration Engine:** Google AI Studio (Gemini API / `gemini-3-flash-preview`)
* **Data Processing & Analytics:** Pandas, JSON Structure Engineering
* **Interactive Dashboard UI:** Streamlit Framework
* **Data Visualizations:** Plotly, Matplotlib (Pie Charts, Distribution Graphs)

---

## 📁Repository Structure

```text
📁 Samiksha-AI/
│
├── 📁 data/
│   └── output1.json               # Scraped, raw and structured feedback dataset
│
├── 📁 src/
│   ├── app.py                    # Main Streamlit analytical dashboard interface
│   └── analytical_engine.py      # Core Gemini API prompt & processing pipeline
│
├── .gitignore                    # Python build, cache, and env exclusions
├── requirements.txt              # Complete Python dependency configuration manifest
└── README.md                     # System documentation page
---

## 📦 Installation & Local Configuration

Follow these steps to configure and execute Samiksha AI locally on your system:

### 1. Clone the Architecture
```bash
git clone [https://github.com/TechSakhi/Samiksha-AI.git](https://github.com/TechSakhi/Samiksha-AI.git)
cd Samiksha-AI
pip install -r requirements.txt
# Set your API Key
set GEMINI_API_KEY="your_actual_api_key_here"

# Run the dashboard
streamlit run src/app.py
