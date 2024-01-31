# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:53:47 2024

@author: user
"""

import pandas as pd

file = pd.read_csv("data_02/iris.csv")

"""
Absolute path:
 C:/Users/user/Desktop/css2024_day02/css2024_day02/data_02/iris.csv

Relative path:
data_02/iris.csv
    
"""

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

file = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

file= pd.read_excel("data_02/residentdoctors.xlsx")

url = "https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = dataframe

df= pd.read_csv(url)


df= pd.read_csv("data_02/country_data_index.csv")


df = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())

df["LOWER_AGE"]= df["LOWER_AGE"].astype(int)

print(df.info())

"""
working with dates

"""

df = pd.read_csv("data_02/time_series_data.csv", index_col=0)

print(df.info())

df['Date'] = pd.to_datetime(df['Date'])

print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format = "%d-%m-%Y")

print(df.info())


df['Year']= df['Date'].dt.year


"""
.str
.extract
.astype
"""

df= pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

df.drop(index= 26, inplace = True)

df['Date']= pd.to_datetime(df['Date'])

print(df.info())

avg_cal= df["Calories"].mean()

df["Calories"].fillna(avg_cal,inplace=True)

"""
best practices
"""

df.dropna(inplace=True)

df= df.reset_index(drop=True)

df.loc[7, 'Duration'] = 45

df['Duration'] = df['Duration'].replace([450],50)

print(df)

df = pd.read_csv("data_02/iris.csv")

print(df.columns)

df["sepal_length_sq"] = df["sepal_length"]**2


grouped = df.groupby("class")

mean_square_values= grouped['sepal_length_sq'].mean()

print(mean_square_values)

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df= pd.concat([df1,df2], ignore_index= True)



df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")

#inner  join

df_merge_inner= pd.merge(df1, df2, on = "id")

df["class"] = df["class"].str.replace("iris-","")

df = pd.read_csv("data_02/iris.csv")

df["sepal_length_sq"] = df["sepal_length"]**2

df["class"] = df["class"].str.replace("Iris-", "")

df = df[df['sepal_length']>5]

df = df[df["class"] == "virginica"]

df.to_csv("pulsar.csv")


