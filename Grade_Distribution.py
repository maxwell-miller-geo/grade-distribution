# Python Grade Distribution Analyzer
# Objective: Take table data from NAU website table and record it for data processing
# import codecs

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import statistics as stat

###############

def read_table(html):
    Time = html[23:-5].replace("_"," ") # slices string to find semester
    class_table = pd.read_html(html, skiprows = [1]) # skips blank row
    under = class_table[0] 
    cut = under.drop(0)
    data = cut.drop(axis = 1, columns = 0)
    col_length = data.shape[1] # number of columns
    row_length = data.shape[0] # number of rows
    df = pd.DataFrame(data)
    df.index = [under.loc[y,0] for y in range(1,row_length+1)]
    df.columns = [under.loc[0,x] for x in range(1,col_length+1)]
    df['Instructor Name'] = df['Instructor Name'].astype(str)
    
    # Add raw data into a new column: list method
    classes = df.index
    conv = {4: 'A',3:'B',2:'C',1:'D',0:'F'}

    df['Raw'] = None # Create empty raw data series
    df['Average'] = None # creates average column
    df['Median'] = None 
    df['Mode'] = None 
    df['Standard Deviation'] = None
    df['Classes'] = df.index

    for row in range(len(df.index)): # loops through all of the rows
        raw = []
        for x in range(5): # A little funky but much less code
            number = int(df.iloc[row,x+3]) # Maybe another for loop for the raw data or a function?
            grade = 4 - x
            for y in range(number):
                    raw.append(grade)
        df.iloc[row, 16] = pd.Series([raw]) # needs to be a series and enclosed with brackets
        df.iloc[row, 17] = round(stat.mean(raw),3)
        df.iloc[row, 18] = stat.median(raw)
        df.iloc[row, 19] = stat.mode(raw)
        df.iloc[row, 20] = stat.stdev(raw)
    
    plt.bar(df.index,df['Average'])
    plt.title('Mean GPA {}'.format(Time))
    plt.xlabel('Class')
    plt.ylabel('Mean GPA (4 point scale)')
    plt.xticks(rotation = 30)
    #plt.show()
    #plt.close()
    return df
    
# Read this 
Fall2013 = read_table('C:/Users/mmmds/Desktop/GLGData/Fall_2003.html')
Spring2014 = read_table('C:/Users/mmmds/Desktop/GLGData/Spring_2004.html')

# Combine the datasets
CY = pd.concat([Fall2013,Spring2014])

# Find Classes with certain Professors
Wittke = CY[CY['Instructor Name'].str.contains('Wittke')]


