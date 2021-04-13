#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 01:14:43 2021

@author: caiazzo
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

filepath = "/Users/caiazzo/Desktop/Seminar-python-ElGouna/"

'''
The concept is the following: whenever we want to write a code - project, we 
have to follow these steps:
    - understand what you want to do 
    - plan the code steps in advance (on paper!)
    - write the skeleton of what you need
    - do some quick step and test
    - generalize
    - extensive test
    - document
    - share
'''

# see https://indianaiproduction.com/seaborn-heatmap/


# download data

# look at data: plot some data for germany (e.g.)

# generalize: how to plot data for one and multiple countries


class CountryData:
    def __init__(self,name,df):
        self.name=name
        country_df =  df.loc[df['location']==name]
        self.continent = country_df['continent'].values[0]
        self.population = country_df['population'].values[0]
    def set_data(self,df):
        country_df =  df.loc[df['location']==self.name]
        self.incidence = country_df['weekly_cases'].values/self.population*100000
     
        
        
    
def draw_heatmap(countries):
    all_data = []
    y_axis_labels = []
    for country in countries:
        country.set_data(df=full_data)
        tmp = country.incidence[-365:]
        all_data.append(tmp)
        print(len(tmp),len(country.incidence))
        y_axis_labels.append(country.name)
    data = np.array(all_data)
    fig, ax = plt.subplots(figsize=(10,20))
    ax = sns.heatmap(data, cbar_kws={"orientation": "horizontal"},
                 yticklabels=y_axis_labels,cmap="Spectral")
    
    

'''
function to get the continent of a country
'''
def get_continent(df = None, country=None):
    
    if df == None:
        # this should not happen. returning an empty array
        return None
    
    else:
        country_df =  df.loc[df['location']==country]
        continent = country_df['continent'].values[0]
    
        if len(country_df['continent'])==0:
            print("** Warning: I did not find any match for the country",
                  country)
            return None
        else:
            if len(country_df['continent'])>1:
                print(" ** Warning: I expected an array of length 1 but I found ", 
                      str(len(country_df['continent'])), 'values ')
    
        return continent

# version 0: using strings  
def plot_0_country_data(df = None, country=None, 
                      data_name = None, y_label = None,
                      sampling=30,
                      fig_name=None):
    fig, ax = plt.subplots(figsize=(12,9))
    for c_name in country:
        c = df.loc[full_data["location"]==c_name]
        dates = c['new_date'][1::sampling].values
        values = c[data_name][1::sampling].values
        plt.plot(dates,values,label=c_name,linewidth=3)
        
        #print(dates)
        plt.xticks(rotation = -90)
    plt.legend(framealpha=1,frameon=False).set_draggable(True)
    
    
    
    # change x-axis
    if y_label == None:
        plt.ylabel(data_name)
    else:
        plt.ylabel(y_label)
    plt.tight_layout()
    if not(fig_name==None):
        # save as pdf
        plt.savefig(fig_name)
    plt.show()

# version 1: using class
def plot_country_data(df = None, countries=None, 
                      data_name = None, y_label = None,
                      sampling=30,
                      fig_name=None):
    fig, ax = plt.subplots(figsize=(12,9))
    for country in countries:
        c = df.loc[full_data["location"]==country.name]
        dates = c['new_date'][1::sampling].values
        values = c[data_name][1::sampling].values
        plt.plot(dates,values,label=country.name,linewidth=3)
        
        #print(dates)
        plt.xticks(rotation = -90)
    plt.legend(framealpha=1,frameon=False).set_draggable(True)
    
    
    
    # change x-axis
    if y_label == None:
        plt.ylabel(data_name)
    else:
        plt.ylabel(y_label)
    plt.tight_layout()
    if not(fig_name==None):
        # save as pdf
        plt.savefig(fig_name)
    plt.show()

# Step 1: load data
# full data set
# ['date', 'location', 'new_cases', 'new_deaths', 'total_cases',
#    'total_deaths', 'weekly_cases', 'weekly_deaths', 'biweekly_cases',
#    'biweekly_deaths']
full_data = pd.read_csv(filepath+"full_data.csv")
day0 = '2020-01-22'
t0 = datetime.strptime(day0, "%Y-%m-%d")

new_dates = []
for d in full_data['date']:
    t1 = datetime.strptime(d, "%Y-%m-%d")
    td = t1-t0
    new_dates.append(td.days)
    
full_data['new_date']=new_dates
#print(full_data.columns)
# 'date', 'location', 'new_cases', 'new_deaths', 'total_cases',
# 'total_deaths', 'weekly_cases', 'weekly_deaths', 'biweekly_cases',
# 'biweekly_deaths'




# latest dataset: contain only last available data.
# useful because there is a country->region mapping

# 'iso_code', 'continent', 'location', 'last_updated_date', 'total_cases',
# 'new_cases', 'new_cases_smoothed', 'total_deaths', 'new_deaths',...
latest_data = pd.read_excel(filepath+"owid-covid-latest.xlsx")
#print(latest_data.columns)
de = latest_data.loc[latest_data['location']=="Germany"]
continent = de['continent'].values[0]


# Step 2: UNDERSTAND look at data

de = full_data.loc[full_data["location"]=="Germany"]
plt.rcParams.update({'font.size': 16})
fig, ax = plt.subplots(figsize=(12,9))
plt.plot(de['date'][1::10],de['total_cases'][1::10]/1e6)
# change x-axis
plt.ylabel("Total cases")
plt.xticks(np.arange(len(de['date'][1::10])),de['date'][1::10].values,rotation = -90)
plt.tight_layout()
#plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees
plt.show()






    
# Step 3: PLAN make a plan of what we want to do


''' 
Step 4: try some function to get familiar with data: for example, we can 
- (4.1) plot the evolution for a country or for a continent
- (4.2) combine some of the columns 
- (4.3) combine the two datasets
- (4.4) have a look at different plotting options 

'''

'''
Step 5: generalize/looping/functions:
    Do not repeat yourself! We will try to avoid code repetition and make the 
    same plots with less code, or playing with the options as a function parameters
'''

'''
Step 6: IDEA: plot a heatmap matrix showing the variation of the incidence per country over time.
Reference: the map for berlin for ages groups
'''

data = np.random.randn(50, 20)


# get incidence for each country
all_countries = np.unique(full_data['location']).tolist()
blacklist = ['Europe', 'European Union','World','South America',
             'North America','Africa','Asia','Oceania']
for b in blacklist:
    all_countries.remove(b)


europe = []
for a in all_countries:
    country = CountryData(name=a,df=latest_data)
    if country.continent == "Europe":
        europe.append(country)
        
        
large = []
for a in all_countries:
    country = CountryData(name=a,df=latest_data)
    if country.continent == "Europe" or country.continent == "South America": 
        if country.population > 10000000:
            large.append(country)


    

# compute incidence
all_data = []
y_axis_labels = []
all_countries= europe
for a in all_countries:
    country = CountryData(name=a,df=latest_data)
    country.set_data(df=full_data)
    if len(country.incidence)>365:
        #print(len(country.incidence))
        tmp = country.incidence[-365:]
        all_data.append(tmp)
        print(len(tmp),len(country.incidence))
        y_axis_labels.append(country.name)
        
data = np.array(all_data)
fig, ax = plt.subplots(figsize=(10,20))
ax = sns.heatmap(data, cbar_kws={"orientation": "horizontal"},
                 yticklabels=y_axis_labels,cmap="Spectral")
    

# alternative: we create a DF with columns:
# country_name, date1, .... , dateM
# and use the seaborn built in function


# generalize:
# plot heatmap per selected countries


  

'''
Step 7: PLAN THE STEPS YOUR CODE ON PAPER
'''

'''
STEP 8: DO A QUICK IMPLEMENTATION AND TEST
'''

# single continent

# for given population size


'''
STEP 9: GENERALIZE & TEST
'''

'''
STEP 10: PUBLISH!
'''



df = full_data.groupby('location')