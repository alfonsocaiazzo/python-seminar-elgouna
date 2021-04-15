#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

# return a continent for a given country (string) and a given dataframe
def get_continent(country, data):
    selected = data.loc[ data['location']==country]
    continent = selected['continent'].values[0]
    return continent
    
# return the population (in Mio.) for a given country (string) and a given dataframe
def get_population(country, data):
    selected = data.loc[ data['location']==country]
    result = selected['population'].values[0]/1e6
    return result


# we can actually be even more general: name tells us which property we need
def get_property(country,data,name):
    selected = data.loc[ data['location']==country]
    result = selected[name].values[0]
    return result

def plot_data_of_country(country,data,sampling=10):
    # select the data (df = short for 'dataframe')
    df= data.loc[data["location"]==country]

    # create a figure
    fig, ax = plt.subplots(figsize=(12,9))
    # we have to sample (if we show all data, the plot get very full)
    sampling = 10 #days
    # create a barplot
    plt.bar(df['date'][0::sampling],df['total_cases'][0::sampling]/1e6)
    
    # y-label
    plt.ylabel("Total cases")
    # x-axis
    plt.xticks(np.arange(len(df['date'][0::sampling])),df['date'][0::sampling].values,rotation = -90)

    # some function to make it nicer
    plt.tight_layout()
    plt.show()