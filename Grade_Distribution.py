# Python Grade Distribution Analyzer
# Objective: Take table data from NAU website table and record it for data processing
# import codecs

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import statistics as stat
from IPython.display import display
import PySimpleGUI as sg
import wx


###############

########
## PySimpleGUI
##layout = [[sg.Text("NAU Geology Grade Distribution")], [sg.Button("OK")]]
##
### Create the window
##window = sg.Window("NAU Geology Grade Distribution", layout)
##
### Create an event loop
##while True:
##    event, values = window.read()
##    # End program if user closes window or
##    # presses the OK button
##    if event == "OK" or event == sg.WIN_CLOSED:
##        break
##window.close()

def read_table(html):
    Time = html[59:-5].replace("_"," ") # slices string to find semester (59 for GITHub, 23 for Laptop)
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

    #df['Raw'] = None # Create empty raw data series
    df['Average'] = None # creates average column
    df['Median'] = None
    df['Mode'] = None
    df['σ'] = None #standard deviation
    df['Semester'] = Time
    #df['Classes'] = df.index

    for row in range(len(df.index)): # loops through all of the rows
        raw = []
        for x in range(5): # A little funky but much less code
            number = int(df.iloc[row,x+3]) # Maybe another for loop for the raw data or a function?
            grade = 4 - x
            for y in range(number):
                    raw.append(grade)
        if len(raw) > 1:
            # Code below is supposed to insert the series of grades into 1 cell, but it does not work after saving it to another place WTF
            #df.iloc[row, 16] = pd.Series([raw]) # needs to be a series and enclosed with brackets
            df.iloc[row, 16] = round(stat.mean(raw),3)
            df.iloc[row, 17] = stat.median(raw)
            df.iloc[row, 18] = stat.mode(raw)
            df.iloc[row, 19] = stat.stdev(raw)
            # Plot here
        #plt.bar(df.index,df['Average'])
        #plt.title('Mean GPA {}'.format(Time))
        #plt.xlabel('Class')
        #plt.ylabel('Mean GPA (4 point scale)')
        #plt.xticks(rotation = 30)
    #plt.show()
    #plt.close()
    return df

# Read this
Fall_2003 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2003.html')
Spring_2004 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2004.html')
Fall_2004 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2004.html')
Spring_2005 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2005.html')
Fall_2005 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2005.html')
Spring_2006 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2006.html')
Fall_2006 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2006.html')
Spring_2007 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2007.html')
Fall_2007 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2007.html')
Spring_2008 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2008.html')
Fall_2008 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2008.html')
Spring_2009 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2009.html')
Fall_2009 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2009.html')
Spring_2010 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2010.html')
Fall_2010 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2010.html')
Spring_2011 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2011.html')
Fall_2011 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2011.html')
Spring_2012 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2012.html')
Fall_2012 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2012.html')
Spring_2013 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2013.html')
Fall_2013 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2013.html')
Spring_2014 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2014.html')
Fall_2014 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2014.html')
Spring_2015 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2015.html')
Fall_2015 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2015.html')
Spring_2016 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2016.html')
Fall_2016 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2016.html')
Spring_2017 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2017.html')
Fall_2017 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2017.html')
Spring_2018 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2018.html')
Fall_2018 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2018.html')
Spring_2019 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2019.html')
Fall_2019 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2019.html')
Spring_2020 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2020.html')
Fall_2020 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Fall_2020.html')
Spring_2021 = read_table('file:///C:/Users/themi/Documents/GitHub/grade-distribution/Spring_2021.html')

# Display settings changes
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
# Combine the datasets
CY = pd.concat([Fall_2003,Spring_2004,Fall_2004,Spring_2005,Fall_2005,Spring_2006,
                Fall_2006,Spring_2007,Fall_2007,Spring_2008,Fall_2008,Spring_2009,
                Fall_2009,Spring_2010,Fall_2010,Spring_2011,Fall_2011,Spring_2012,
                Fall_2012,Spring_2013,Fall_2013,Spring_2014,Fall_2014,Spring_2015,
                Fall_2015,Spring_2016,Fall_2016,Spring_2017,Fall_2017,Spring_2018,
                Fall_2018,Spring_2019,Fall_2019,Spring_2020,Fall_2020,Spring_2021])

# Find Classes with certain Professors
Wittke = CY[CY['Instructor Name'].str.contains('Wittke')]

# Introducing the GUI!

class MyFrame(wx.Frame):
    
##    def ask(parent=None, message='', default_value=''):
##        dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
##        dlg.ShowModal()
##        result = dlg.GetValue()
##        dlg.Destroy()
##        return result
      
    def __init__(self):
        super().__init__(parent=None, title='NAU Grade Distribution')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        my_btn = wx.Button(panel, label='Search')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)        
        self.Show()
        
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(CY[CY['Instructor Name'].str.contains(value)])
            print(f'You typed: "{value}"')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    
