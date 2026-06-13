import json
import matplotlib.pyplot as plt

# 1. JSON data load karna
with open('output1.json', 'r') as file:
    data = json.load(file)

if isinstance(data, dict) and "reviews" in data:
    reviews_list = data["reviews"]
elif isinstance(data, dict):
    reviews_list = [value for key, value in data.items() if isinstance(value, dict)]
else:
    reviews_list = data

# 2. Sentiments aur Improvements/Action Items extract karna
sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
improvements_list = []

for review in reviews_list:
    # Sentiment count
    sentiment = review.get("Primary_Sentiment", "Neutral")
    if sentiment in sentiment_counts:
        sentiment_counts[sentiment] += 1
    
    # Check if there is a negative aspect or a valid action item
    action_item = review.get("Action_Item", "")
    if action_item and review.get("Is_Spam_Or_Noise") is False:
        improvements_list.append(f"- {action_item}")

# Agar koi action item nahi mila toh safe check
if not improvements_list:
    improvements_list.append("- Everything looks good! Maintain current standards.")

# 3. Create a Subplot Window (Left: Graph, Right: Report Card Text)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Samiksha AI - Enterprise Executive Report Card', fontsize=16, fontweight='bold', color='#1A237E')

# Left Subplot: Sentiment Pie Chart
labels = list(sentiment_counts.keys())
sizes = list(sentiment_counts.values())
colors = ['#4CAF50', '#FF5722', '#FFC107']
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax1.set_title('Overall Sentiment Distribution', fontsize=12, fontweight='bold')

# Right Subplot: Product Improvement Report Card
ax2.axis('off')  # No graph borders for text area
report_card_text = "PRODUCT IMPROVEMENT REPORT\n" + "="*30 + "\n\n"
report_card_text += "Actionable Insights For Business Owner:\n\n"
report_card_text += "\n".join(improvements_list[:5])  # Top 5 actions dikhane ke liye

ax2.text(0.05, 0.95, report_card_text, transform=ax2.transAxes, fontsize=11,
         verticalalignment='top', fontname='monospace', color='#212121',
         bbox=dict(boxstyle='round,pad=1', facecolor='#F5F5F5', edgecolor='#BDBDBD'))

plt.tight_layout()
plt.show()