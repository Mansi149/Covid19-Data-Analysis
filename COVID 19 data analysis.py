# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:27:42 2020

@author: Mansi
"""
# Importing the modules

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

"""  PART 1 """

# Importing covid19 dataset

corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')

# Deleting the useless columns 

corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)

# Aggregating the rows by the country

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

# Visualizing data related to a country for example Australia, Italy and Spain

corona_dataset_aggregated.loc['Australia'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()

# Calculating a good measure of a country for example Australia

corona_dataset_aggregated.loc['Australia'].plot()
plt.legend()

# Caculating the first derivative of the curve

corona_dataset_aggregated.loc['Australia'].diff().plot()
plt.legend()

# Find maxmimum infection rate for Australia

corona_dataset_aggregated.loc['Australia'].diff().max()

# Find maximum infection rate for all of the countries

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates

# Create a new dataframe with only needed column

corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])

""" PART 2 """

# Importing the WorldHappinessReport.csv dataset

world_happiness_report = pd.read_csv("worldwide_happiness_report.csv")

# Drop the useless columns

columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)

# Changing the indices of the dataframe

world_happiness_report.set_index(['Country or region'],inplace=True)

# Joining the two datasets

data = world_happiness_report.join(corona_data).copy()

# correlation matrix ( it is representing the currelation between every two columns of our dataset )

data.corr()

# Visualization of the results
# Plotting GDP vs maximum Infection rate

x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Social support vs maximum Infection rate

x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Healthy life expectancy vs maximum Infection rate

x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Freedom to make life choices vs maximum Infection rate

x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

 







