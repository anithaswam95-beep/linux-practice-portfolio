df = pd.read_csv("airtravel.csv", skipinitialspace=True)
df.columns = df.columns.str.strip()
print(df.columns)
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("airtravel.csv")

print("Original data:")
print(df)
print()

# Rename first column
df = df.rename(columns={"Month": "month"})

# Convert year columns to numbers
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Summary statistics:")
print(df.describe())
print()

# Create total passengers column
df["total_passengers"] = df["1958"] + df["1959"] + df["1960"]

# Find busiest month
busiest_month = df.loc[df["total_passengers"].idxmax(), "month"]
print("Busiest month overall:", busiest_month)

# Save cleaned data
df.to_csv("airtravel_cleaned.csv", index=False)

# Save summary
df.describe().to_csv("airtravel_summary.csv")

# Plot chart
plt.figure(figsize=(10, 6))
plt.plot(df["month"], df["1958"], marker="o", label="1958")
plt.plot(df["month"], df["1959"], marker="o", label="1959")
plt.plot(df["month"], df["1960"], marker="o", label="1960")

plt.title("Airline Passengers by Month")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("airtravel_chart.png")

print("Done! Files created:")
print("airtravel_cleaned.csv")
print("airtravel_summary.csv")
print("airtravel_chart.png")

