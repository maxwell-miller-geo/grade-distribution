# Introducing the GUI!
import wx
import pandas as pd
import statistics as stat

# Display settings changes
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Read in geology distribution
df = pd.read_csv(r'C:\Users\themi\Documents\GitHub\grade-distribution\Geology_Grades.csv')
print(df)




class MyFrame(wx.Frame):
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
        prof = df[df['Instructor Name'].str.contains(value)]
        display = prof.iloc[:,[3,16,17,18,19,20,21,22]]
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'Professor {value}')
            print('All Classes taught')
            print(display)
            print('Average grade (A = 4, F = 0): ' + str(round(stat.mean(display['Average']),3)))
            print('Most taught class: ' + str(stat.mode(display['Classes']))) # need to remove NaN rows
            print(f"{value}'s most common grade: " + str(stat.mode(display['Mode'])))
            

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
