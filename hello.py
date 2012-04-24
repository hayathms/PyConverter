import tkinter
from tkinter import ttk
from tkinter import filedialog


countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
                'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
                'Sweden', 'Switzerland')


class CreateWindow:

    def __init__(self):
        '''From here GUI is initiated'''

        self.root = tkinter.Tk()
        frame = self.mainframe()
        first = FirstFrame(frame,0,0)
        first.first_frame()
        mid = MiddleFrame(frame,1,0)
        mid.middle_frame()



        self.root.mainloop()


    def mainframe(self):
        '''This is The Method Which start building GUI'''

        frame = ttk.Frame(self.root,
                          width='600px',
                          height='300px',
                          borderwidth=2,
                          relief='sunken',
                          padding=10)
        frame.grid(row=0, column=0, sticky='NSEW', rowspan=2)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        return frame
        

class FirstFrame:
    '''This class Initialised Parameters for First Frame'''


    def __init__(self, mainframe, column, row):
        '''Initialting Middle Frame'''

        self.mainframe = mainframe
        self.column = column
        self.row = row


    def first_frame(self):
        '''Craeating Middle Frame'''

        frame = ttk.Frame(self.mainframe,
                          width='200px', 
                          height='200px',
                          borderwidth=2, 
                          relief='sunken',
                          padding=5)
        frame.grid(row=self.row, column=self.column, sticky='NSEW', rowspan=2)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.buttons(frame)
        self.lbox(frame)


    def buttons(self, mainframe):
        '''Here comes all First Frame Buttons''' 

        browse_button = ttk.Button(mainframe, command=open_file, text = 'Browse')
        browse_button.grid(row = 0, column=0, sticky='N')


    def lbox(self, mainframe):
        '''Here comes the Entry Widgets'''


        cnames = tkinter.StringVar(value=countrynames)
        listbox = tkinter.Listbox(mainframe, height=10, listvariable=cnames)
        listbox.grid(column=0, row=1)
        scroll = ttk.Scrollbar(mainframe, orient='vertical', command=listbox.yview)
        listbox.configure(yscrollcommand=scroll.set)
        scroll.grid(column=1, row=1, sticky='NS')
        listbox['yscrollcommand'] = scroll.set
        ttk.Sizegrip(mainframe).grid(column=1, row=2, sticky='SE')


class MiddleFrame:
    '''This class Initialised Parameters for Middle Frame'''


    def __init__(self, mainframe, column, row):
        '''Initialting Middle Frame'''

        self.mainframe = mainframe
        self.column = column
        self.row = row


    def middle_frame(self):
        '''Craeating Middle Frame'''

        frame = ttk.Frame(self.mainframe,
                         width='200px',
                         height='200px',
                         borderwidth=2,
                         relief='sunken',
                         padding=5)
        frame.grid(row=self.row,
                   column=self.column,
                   sticky='NSEW',
                   rowspan=2)
        frame.columnconfigure(self.column, weight=1)
        frame.rowconfigure(self.row, weight=1)





def open_file():

    filename = filedialog.askopenfilename(multiple=True)




    print (filename)

   










a = CreateWindow()
