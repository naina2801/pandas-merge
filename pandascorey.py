import pandas as pd
df1 = pd.read_csv('sample.csv')
df2 = pd.read_csv("sample2.csv")
data1 = pd.DataFrame(df1)
data2 = pd.DataFrame(df2)
res = pd.merge(data1,data2)
print(res.to_csv("output.csv"))