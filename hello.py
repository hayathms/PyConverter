import tkinter
from tkinter import ttk


class CreateWindow:

    def __init__(self):
        '''From here GUI is initiated'''

        self.root = tkinter.Tk()
        frame = self.mainframe()
        mid = MiddleFrame(frame,1,0)
        mid.middle_frame()
        self.root.mainloop()


    def mainframe(self):
        '''This is The Method Which start building GUI'''

        frame = ttk.Frame(self.root, width='600px', height='300px', borderwidth=2, relief='sunken')
        frame.grid(row=0, column=0, sticky='NSEW')
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.buttons(frame)
        self.entries(frame)
        return frame
        

    def buttons(self, mainframe):
        '''Here comes all Mainframe Buttons''' 

        browse_button = ttk.Button(mainframe, command=exit, text = 'Browse')
        browse_button.grid(row = 0, column=0, sticky='N')


    def entries(self, mainframe):
        '''Here comes the Entry Widgets'''
        
        enter_files = ttk.Entry(mainframe)
        enter_files.grid(row=1, column=0)


class MiddleFrame:
    '''This class Initialised Parameters for Middle Frame'''


    def __init__(self, mainframe, column, row):
        '''Initialting Middle Frame'''

        self.mainframe = mainframe
        self.column = column
        self.row = row


    def middle_frame(self):
        '''Craeating Middle Frame'''

        frame = ttk.Frame(self.mainframe, width='200px', height='200px', borderwidth=2, relief='sunken')
        frame.grid(row=self.row, column=self.column, sticky='NSEW')
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)



a = CreateWindow()
