import pandas as pd
df=pd.read_csv("C:\source_code\sem 5.csv")
print(df)
import matplotlib.pyplot as plt
plt.bar(df["Period"],df["Count"])
plt.xlabel('x-axis lable')
plt.ylabel('y-axis lable')
plt.title('bar plot')
plt.show()
plt.stem(df["Period"],df["Count"])
plt.xlabel('x-axis lable')
plt.ylabel('y-axis lable')
plt.title('stem plot')
plt.show()
plt.stackplot(df["Period"],df["Count"])
plt.xlabel('x-axis lable')
plt.ylabel('y-axis lable')
plt.title('stackp plot')
plt.show()
plt.scatter(df["Period"],df["Count"])
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('scatter plot')
plt.show()
plt.hist(df["Period"],weights=df["Count"])
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('histogram plot')
plt.show()




