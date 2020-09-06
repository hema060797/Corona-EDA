# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:26:35 2020

@author: hemahemu
"""


#importing libraries 
#The requests library allows sending HTTP requests through Python,which will be used to obtain the dataset from the internet
#pandas is a open-source Python library that provides powerful data structures and data analysis tool to deal with datasets.
#matplotlib.pyplot and seaborn is packages for Python are the most popular and used packages for data visulaization through Python
import pandas as pd
import requests
import matplotlib.pyplot
import seaborn as sns
filename='covid-data.csv'
data_url='https://covid.ourworldindata.org/data/owid-covid-data.csv'
dataset=requests.get(data_url).content
df=open(filename,'wb')
df.write(dataset)
df.close()
df1=pd.read_csv(filename)
print(df1.columns)
print(df1.describe())
print(df1.shape)
#lets us check for missing values in the dataset
print(df1.isnull().sum())
print(df1.dtypes)
print(df1.fillna(0,inplace=True))
print(df1.isnull().sum())
totalcases=df1.groupby('location')['new_cases'].sum()
totalcases=totalcases.sort_values(ascending=False)
print(totalcases)
most_affected_countries=totalcases[1:11].index
print(most_affected_countries)
#no of cases in top 10 countries
cases=totalcases[1:11].values   
totaldeaths=df1.groupby('location')['new_deaths'].sum()
print(totaldeaths)
#no of deaths in top 10 countries
deaths=totaldeaths[most_affected_countries].values
print(deaths)
death_cases_df=pd.DataFrame({'Country':most_affected_countries,'Total Case':cases,'Total Deaths':deaths})
print(death_cases_df)

import matplotlib.pyplot as plt
dataplot=pd.melt(death_cases_df,id_vars=['Country'],value_vars=['Total Case','Total Deaths'],var_name='Metric',value_name='Case Count')
plt.figure(figsize=(10,5))
sns.barplot(x="Country",hue="Metric",y="Case Count",data=dataplot)
plt.title('Most Affected top10 countries')
plt.show()