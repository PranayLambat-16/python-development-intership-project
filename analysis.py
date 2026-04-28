import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df.head())

avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)

plt.bar(df["Name"], df["Salary"])
plt.title("Salary by Name")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.savefig("bar_chart.png")
plt.close()

plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.savefig("scatter_plot.png")
plt.close()

corr = df.corr(numeric_only=True)
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Heatmap")
plt.savefig("heatmap.png")
plt.close()
