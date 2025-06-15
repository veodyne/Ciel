#uses only vanilla python libraries, doesn't require pip install
#has its own terminal for running cmd prompt inputs and pip installs
#can run, save, and import python files
#standalone ide

from tkinter import *
from tkinter import filedialog
import os
import pathlib
from pathlib import Path


class App(Tk):
    def __init__(self):
        super().__init__()

        self.SCREENWIDTH = self.winfo_screenwidth()
        self.SCREENHEIGHT = self.winfo_screenheight()

        self.geometry(f"{self.SCREENWIDTH}x{self.SCREENHEIGHT}") #Set GUI dimensions to user's monitor resolution
        self.title("Ciel IDE")


        self.menubar = Menu()
        self.config(menu=self.menubar)


        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.fileMenu.add_command(label= "New File", command= self.newFile)
        self.fileMenu.add_command(label= "Open", command= self.openFile)
        self.fileMenu.add_command(label= "Save", command= self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Run", command= self.runFileCode)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Exit", command= self.exitFile)


        self.lines = Text(self, height=self.SCREENHEIGHT/400, width=self.SCREENWIDTH, bg="#252525", foreground="#FFFFFF") #Displays number of lines in code when saved.
        self.lines.insert("1.0", "Ln 0, Char 0")
        self.lines.configure(state=DISABLED)
        self.lines.pack(side=BOTTOM)


        #Create command line.
        self.cmdFrame = Frame(self, height=self.SCREENHEIGHT/400, width=self.SCREENWIDTH)
        self.cmdFrame.pack(side=BOTTOM)
        self.cmdLine = Text(self.cmdFrame, height=self.SCREENHEIGHT/500, width=int(self.SCREENWIDTH/10), bg="#131212", foreground="#FFFFFF")
        self.cmdLine.pack(side=LEFT)
        self.cmdButton = Button(self.cmdFrame, width=int(self.SCREENWIDTH/10), height=int(self.SCREENHEIGHT/500), bg="#0F0F0F", foreground="#FFFFFF", text="Execute CMD", command=self.cmdExecute)
        self.cmdButton.pack(side=RIGHT)

        #Create box to enter code.
        self.inputBox = Text(self, height=self.SCREENHEIGHT, width=int(self.SCREENWIDTH), bg="#3B3939", foreground="#FFFFFF")
        self.inputBox.pack()


    #Grabs CMD command and runs it.  
    def cmdExecute(self):
        self.rawCommand = '(self.cmdLine.get("1.0", END))'
        print(self.rawCommand)
        self.cmdCommand = compile(f"os.system({self.rawCommand})", "cmdcode", "exec")
        exec(self.cmdCommand)

    #Create new Ciel window.
    def newFile(self):
        newWindow(self)

    #Import Python file from local directory.
    def openFile(self):
        self.file = filedialog.askopenfile(defaultextension=".py", 
                                           filetypes=[("Python File",".py"), 
                                                      ("All Files", ".*")
                                                      ])
        
        self.pythonFile = str(self.file) #Getting name of Python file.
        self.replacer = ["<_io.TextIOWrapper name='", "' mode='r' encoding='cp1252'>"] #Getting rid of extra stuff to isolate the filename.
        for sub in self.replacer:
            self.pythonFile = self.pythonFile.replace(sub, "")
        print(self.pythonFile)

        self.fileCode = open(self.pythonFile, "r") #Open file in read mode.
        print(self.fileCode)
        linePos = 0
        letterPos = 0
        for x in self.fileCode:
            linePos += 1
            for y in x:
                letterPos += 1
                self.inputBox.insert(f"{linePos}.{letterPos}", y) #Insert contents of Python file in editor.
            self.inputBox.insert(f"{linePos}.{letterPos+1}", "\n")

    def saveFile(self):
        self.file = filedialog.asksaveasfile(defaultextension=".py",
                                             filetypes=[("Python File",".py"),
                                                        ("All Files", ".*")
                                                        ])
        
        self.file.write(str(self.inputBox.get("1.0", END)))
        self.file.close()
        print(self.file)

        #Update display showing number of lines and characters of file.
        self.lines.configure(state=NORMAL)
        self.lines.delete("1.0", END)
        self.Ln = int(self.inputBox.index('end-1c').split(".")[0])
        self.Char = len(self.inputBox.get("1.0", END))
        self.lines.insert("1.0", f"Ln {self.Ln}, Char {self.Char}")
        self.lines.configure(state=DISABLED)

    def runFileCode(self):
        self.codeCommand = compile(str(self.inputBox.get("1.0", END)), "code", "exec") #Grab all code in editor.
        exec(self.codeCommand) #Runs the code.


    def exitFile(self):
        self.destroy()



#Copy of main app for when user clicks "New File".
class newWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SCREENWIDTH = self.winfo_screenwidth()
        self.SCREENHEIGHT = self.winfo_screenheight()

        self.geometry(f"{self.SCREENWIDTH}x{self.SCREENHEIGHT}")
        self.title("Ciel IDE")


        self.menubar = Menu()
        self.config(menu=self.menubar)


        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.fileMenu.add_command(label= "New File", command= self.newFile)
        self.fileMenu.add_command(label= "Open", command= self.openFile)
        self.fileMenu.add_command(label= "Save", command= self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Run", command= self.runFileCode)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Exit", command= self.exitFile)

        self.lines = Text(self, height=self.SCREENHEIGHT/400, width=self.SCREENWIDTH, bg="#252525", foreground="#FFFFFF")
        self.lines.insert("1.0", "Ln 0, Char 0")
        self.lines.configure(state=DISABLED)
        self.lines.pack(side=BOTTOM)

        self.cmdFrame = Frame(self, height=self.SCREENHEIGHT/400, width=self.SCREENWIDTH)
        self.cmdFrame.pack(side=BOTTOM)
        self.cmdLine = Text(self.cmdFrame, height=self.SCREENHEIGHT/500, width=int(self.SCREENWIDTH/10), bg="#131212", foreground="#FFFFFF")
        self.cmdLine.pack(side=LEFT)
        self.cmdButton = Button(self.cmdFrame, width=int(self.SCREENWIDTH/10), height=int(self.SCREENHEIGHT/500), bg="#0F0F0F", foreground="#FFFFFF", text="Execute CMD", command=self.cmdExecute)
        self.cmdButton.pack(side=RIGHT)


        self.inputBox = Text(self, height=self.SCREENHEIGHT, width=int(self.SCREENWIDTH), bg="#3B3939", foreground="#FFFFFF")
        self.inputBox.pack()

    def cmdExecute(self):
        self.rawCommand = '(self.cmdLine.get("1.0", END))'
        print(self.rawCommand)
        self.cmdCommand = compile(f"os.system({self.rawCommand})", "cmdcode", "exec")
        exec(self.cmdCommand)

    def newFile(self):
        newWindow(self)

    def openFile(self):
        self.file = filedialog.askopenfile(defaultextension=".py", 
                                           filetypes=[("Python File",".py"), 
                                                      ("All Files", ".*")
                                                      ])
        
        self.pythonFile = str(self.file)
        self.replacer = ["<_io.TextIOWrapper name='", "' mode='r' encoding='cp1252'>"]
        for sub in self.replacer:
            self.pythonFile = self.pythonFile.replace(sub, "")
        print(self.pythonFile)

        self.fileCode = open(self.pythonFile, "r")
        print(self.fileCode)
        linePos = 0
        letterPos = 0
        for x in self.fileCode:
            linePos += 1
            for y in x:
                letterPos += 1
                self.inputBox.insert(f"{linePos}.{letterPos}", y)
            self.inputBox.insert(f"{linePos}.{letterPos+1}", "\n")

    def saveFile(self):
        self.file = filedialog.asksaveasfile(defaultextension=".py",
                                             filetypes=[("Python File",".py"),
                                                        ("All Files", ".*")
                                                        ])
        
        self.file.write(str(self.inputBox.get("1.0", END)))
        self.file.close()
        print(self.file)

        self.lines.configure(state=NORMAL)
        self.lines.delete("1.0", END)
        self.Ln = int(self.inputBox.index('end-1c').split(".")[0])
        self.Char = len(self.inputBox.get("1.0", END))
        self.lines.insert("1.0", f"Ln {self.Ln}, Char {self.Char}")
        self.lines.configure(state=DISABLED)

    def runFileCode(self):
        self.codeCommand = compile(str(self.inputBox.get("1.0", END)), "code", "exec")
        exec(self.codeCommand)

    def exitFile(self):
        self.destroy()



app = App()
app.mainloop()