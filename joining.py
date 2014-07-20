import pandas as pd

df = pd.read_csv("CombineSheet2.csv")
df1= pd.read_csv("CombinedNames.csv")

df1 =df1.rename(columns={'Name':'Name of Sender'})
df2=pd.merge(df, df1,on='Name of Sender', how='left',suffixes={'','_sender'})

df1= df1.rename(columns={'Name of Sender':'Name of Other'})
df2=pd.merge(df2, df1,on='Name of Other', how='left',suffixes={'','_other'})

df2.to_csv("Labeled2.csv")
