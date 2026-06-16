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
## 🧠 Core LLM Prompt Configuration

To extract highly structured aspect-based sentiments and maintain data integrity, the system utilizes the following engineered prompt architecture within the `analytical_engine.py` script:

```text
You are Samiksha AI, an expert enterprise-grade customer feedback analyzer agent.
Your task is to take raw customer text from the 'Raw_Review_Text' column and process it through a multi-step reasoning pipeline.

For every input review, you must strictly output a JSON object with the following schema:
{
  "Review_ID": "Extract verbatim from data",
  "Is_Spam_Or_Noise": true/false,
  "Primary_Sentiment": "Positive" / "Negative" / "Neutral",
  "Aspect_Splits": [
    {
      "Aspect_Name": "Audio Quality" / "Video Quality" / "Fragrance" / "Hydration" / "Content Request",
      "Sentiment": "Positive" / "Negative",
      "Extracted_Text_Snippet": "Exact phrase from the review"
    }
  ],
  "Contains_Sarcasm": true/false,
  "Action_Item": "One short sentence advising the business owner on what to do next"
}

Processing Rules:
1. If the text contains only greetings or shipping comments without product detail, mark 'Is_Spam_Or_Noise' as true.
2. Read carefully for tone. If negative phrases are hidden behind happy words, mark 'Contains_Sarcasm' as true and override sentiment to 'Negative'.


Filter out generic automated bot expressions or complete spam inputs. Do not assume or hallucinate features not explicitly stated in the input text block.
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
