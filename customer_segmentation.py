import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PROFESSIONAL STYLE
# =========================
plt.style.use('dark_background')
sns.set_theme(style="darkgrid")

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# =========================
# CUSTOMER SALES SUMMARY
# =========================
customer_data = df.groupby('COUNTRY')['SALES'].sum().reset_index()

# =========================
# CUSTOMER SEGMENT FUNCTION
# =========================
def segment_customer(sales):

    if sales > 15000:
        return "High Value"

    elif sales > 8000:
        return "Medium Value"

    else:
        return "Low Value"

# Apply customer segmentation
customer_data['Segment'] = customer_data['SALES'].apply(segment_customer)

# =========================
# KPI METRICS
# =========================
total_sales = customer_data['SALES'].sum()
avg_sales = customer_data['SALES'].mean()
top_country = customer_data.sort_values(by='SALES', ascending=False).iloc[0]['COUNTRY']

print("\n===== KPI METRICS =====")
print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Top Country:", top_country)

# =========================
# DASHBOARD TITLE
# =========================
print("\n===== CUSTOMER SEGMENTATION DASHBOARD =====")

# =========================
# ADVANCED BAR CHART
# =========================
plt.figure(figsize=(14,7))

ax = sns.barplot(
    data=customer_data,
    x='COUNTRY',
    y='SALES',
    hue='Segment',
    palette='magma'
)

plt.title(
    "Customer Segmentation Analysis",
    fontsize=22,
    fontweight='bold'
)

plt.xlabel("Country", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)

# Add value labels
for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='bottom',
        fontsize=10,
        color='white'
    )

plt.xticks(rotation=15)

plt.tight_layout()

# Save graph
plt.savefig(
    "advanced_customer_segmentation_bar.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

# =========================
# DONUT CHART
# =========================
segment_counts = customer_data['Segment'].value_counts()

plt.figure(figsize=(8,8))

colors = sns.color_palette('Set2')

wedges, texts, autotexts = plt.pie(
    segment_counts,
    labels=segment_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4)
)

plt.title(
    "Customer Segment Distribution",
    fontsize=20,
    fontweight='bold'
)

plt.tight_layout()

# Save chart
plt.savefig(
    "advanced_customer_segmentation_donut.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

# =========================
# SALES DISTRIBUTION CHART
# =========================
plt.figure(figsize=(12,6))

sns.lineplot(
    data=customer_data,
    x='COUNTRY',
    y='SALES',
    marker='o',
    linewidth=3,
    color='cyan'
)

plt.title(
    "Sales Distribution Across Countries",
    fontsize=20,
    fontweight='bold'
)

plt.xlabel("Country", fontsize=14)
plt.ylabel("Sales", fontsize=14)

plt.tight_layout()

# Save line graph
plt.savefig(
    "sales_distribution_line.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

# =========================
# INSIGHTS
# =========================
print("\n===== BUSINESS INSIGHTS =====")

print("\nHigh Value Customers:")
print(customer_data[customer_data['Segment']=="High Value"])

print("\nMedium Value Customers:")
print(customer_data[customer_data['Segment']=="Medium Value"])

print("\nLow Value Customers:")
print(customer_data[customer_data['Segment']=="Low Value"])

print("\n===== FINAL SUMMARY =====")
print("Top Performing Country:", top_country)
print("Total Revenue Generated:", total_sales)
print("Average Sales:", round(avg_sales,2))

print("\nProject Completed Successfully!")