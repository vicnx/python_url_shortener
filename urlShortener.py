import configparser
from genericpath import exists
import os
import sys
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import simpledialog
from tkinter import messagebox
from tokenize import String
import webbrowser
import pyshorteners
from tkfontawesome import icon_to_image 
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

config = configparser.RawConfigParser()

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class App():
  def __init__(self):
    super().__init__()
    self.bitlyAPI = StringVar
    # self.check_apis()

  def check_apis(self):
    try:
        if not exists(resource_path('config.ini')):
          askapis = AskApis()
        else:
          config.read(resource_path('config.ini'))
          self.bitlyAPI = (config['APIS']['bitly'])
          messagebox.showinfo(message='Apis loaded successfully', title="Info")
          app.start()
    except:
        messagebox.showerror(message='Error please tell admin.', title="Error")
    return
    # self.bitlyAPi = askstring('Bitly API KEY', "Please enter <b>BITLY API KEY</b>:\nIf you don't enter it, the bitly shortener won't work.\nhttps://dev.bitly.com/docs/getting-started/authentication/",show='*')

  def create_window(self):
    self.root = tk.Tk()
    self.root.title("URL Shortener v0.1")
    self.root.option_add("*tearOff", False)
    self.root.resizable(False, False)
    self.root.geometry("1000x400")
    self.root.columnconfigure(index=0, weight=0)
    self.root.columnconfigure(index=1, weight=1)
    self.root.columnconfigure(index=2, weight=0)
    # self.root.columnconfigure(index=3, weight=1)
    self.root.rowconfigure(index=0, weight=1)
    self.root.rowconfigure(index=1, weight=0)
    self.root.rowconfigure(index=2, weight=0)
    self.root.rowconfigure(index=3, weight=3)
    self.root.rowconfigure(index=4, weight=1)
    # sizegrip = ttk.Sizegrip(self.root)
    # sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style
    style = ttk.Style(self.root)
    # Import the tcl file
    self.root.tk.call("source", "proxttk.tcl")
    # Set the theme with the theme_use method
    style.theme_use("proxttk")
    # TopFrame
    # style.configure('TFrame', background='green')
    # self.frame = ttk.Frame(self.root, padding=(0,0, 0, 0), style='TFrame')
    self.topFrame = ttk.Frame(self.root, padding=(0,0, 0, 0))
    self.topFrame.grid(row=0, column=1, padx=(20,5),pady=(10,10), sticky="nsew", rowspan=3)
    self.topFrame.columnconfigure(index=0, weight=1)
    self.topFrame.columnconfigure(index=1, weight=1)
    self.topFrame.columnconfigure(index=2, weight=0)
    self.topFrame.columnconfigure(index=3, weight=1)
    # Title
    title = ttk.Label(self.topFrame, text="URL SHORTENER",font="gotham 20  bold",foreground="#333333")
    title.grid(row=0, column=0, pady=10, columnspan=4)
    #label
    label1 = ttk.Label(self.topFrame, text="Put your long url...",font="gotham 10  bold",foreground="#333333")
    label1.grid(row=1, column=1, pady=10, padx=(80,0) ,columnspan=1)
    #Input
    self.urlInput = ttk.Entry(self.topFrame)
    self.urlInput.insert(0, "")
    self.urlInput.grid(row=2, column=1, pady=0, padx=(0,0), columnspan=1,sticky="we")
    #button
    accentbutton = ttk.Button(self.topFrame, text="CUT", style="AccentButton", command=lambda: self.shortUrls(), cursor="hand2")
    accentbutton.grid(row=2, column=2, padx=5, pady=0, sticky="nsew")

    #Bottom Frame
    self.bottomFrame = ttk.Frame(self.root, padding=(0,0, 0, 0))
    self.bottomFrame.grid(row=3, column=1, padx=(5,5),pady=(10,10), sticky="nsew", rowspan=1)
    self.bottomFrame.columnconfigure(index=0, weight=1)
    self.bottomFrame.columnconfigure(index=1, weight=1)
    self.bottomFrame.columnconfigure(index=2, weight=1)

    #TinyURL label & Input
    labelTinyUrl = ttk.Label(self.bottomFrame, text="TinyUrl",font="gotham 10  bold",foreground="#333333")
    labelTinyUrl.grid(row=0, column=0, pady=10, padx=(0,0) ,columnspan=1)
    self.tinyurlShorted = StringVar()
    self.urltinyurl = ttk.Entry(self.bottomFrame, state="readonly",textvariable=self.tinyurlShorted, cursor="hand2")
    self.urltinyurl.grid(row=1, column=0, pady=0, padx=(10,10), columnspan=1,sticky="nsew")

    #Bitly label & Input
    labelBitly = ttk.Label(self.bottomFrame, text="Bitly",font="gotham 10  bold",foreground="#333333")
    labelBitly.grid(row=0, column=1, pady=10, padx=(0,0) ,columnspan=1)
    self.bitlyurlShorted = StringVar()
    self.urlbitly = ttk.Entry(self.bottomFrame, state="readonly",textvariable=self.bitlyurlShorted, cursor="hand2")
    self.urlbitly.grid(row=1, column=1, pady=0, padx=(10,10), columnspan=1,sticky="nsew")

    #Bitly label & Input
    owly = ttk.Label(self.bottomFrame, text="Da.gd",font="gotham 10  bold",foreground="#333333")
    owly.grid(row=0, column=2, pady=10, padx=(0,0) ,columnspan=1)
    self.dagdShorted = StringVar()
    self.urldagd = ttk.Entry(self.bottomFrame, state="readonly",textvariable=self.dagdShorted, cursor="hand2")
    self.urldagd.grid(row=1, column=2, pady=0, padx=(10,10), columnspan=1,sticky="nsew")

    #Footer
    self.github = icon_to_image("github", fill="black", scale_to_width=20)  
    self.github_button = ttk.Button(master=self.root,text="Github", command=lambda:self.open_github(), image = self.github, compound = 'left', cursor="hand2")
    self.github_button.grid(row=4, column=1, pady=0, padx=10, sticky="w")
    self.clean = icon_to_image("broom", fill="black", scale_to_width=20)  
    self.clean_button = ttk.Button(master=self.root,text="Clean Apis", command=lambda:self.clean_apis(), image = self.clean, compound = 'left', cursor="hand2")
    self.clean_button.place(x=880,y=350)

  def clean_apis(self):
    if os.path.exists(resource_path('config.ini')):
       os.remove(resource_path('config.ini'))
    messagebox.showinfo(message="Apis cleaned successfully, please restart the app", title="Info")
    self.root.destroy()
    
  def open_github(self):
      webbrowser.open('https://www.github.com/vicnx', new=0, autoraise=True)

  def shortUrls(self):
    long_url = self.urlInput.get()
    short_noapi = pyshorteners.Shortener()
    try:
      self.tinyurlShorted.set(short_noapi.tinyurl.short(long_url))
    except Exception as e:
      messagebox.showerror(message="Tinyurl error.", title="Error")

    try :
      bitly = pyshorteners.Shortener(api_key=self.bitlyAPI)
      self.bitlyurlShorted.set(bitly.bitly.short(long_url))
    except Exception as e:
      messagebox.showerror(message="Bit.ly error, clean the api and try again please.", title="Error")
    try:
      self.dagdShorted.set(short_noapi.dagd.short(long_url))
    except Exception as e:
      messagebox.showerror(message="Da.gd error.", title="Error")

  def start(self):
    app.create_window()
    app.root.mainloop()


class AskApis():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("URL Shortener v0.1")
        self.root.geometry("450x200")
        self.root.option_add("*tearOff", False)
        self.root.resizable(False, False)
        self.root.columnconfigure(index=0, weight=0)
        self.root.columnconfigure(index=1, weight=1)
        self.root.columnconfigure(index=2, weight=0)
        self.root.rowconfigure(index=0, weight=0)
        self.root.rowconfigure(index=1, weight=0)
        self.root.rowconfigure(index=2, weight=0)
        self.root.rowconfigure(index=3, weight=0)
        self.root.rowconfigure(index=4, weight=0)
        style = ttk.Style(self.root)
        # Import the tcl file
        self.root.tk.call("source", "proxttk.tcl")
        # Set the theme with the theme_use method
        style.theme_use("proxttk")
        labelBitlyToken = ttk.Label(self.root, text="BITLY TOKEN",font="gotham 10  bold")
        labelBitlyToken.grid(row=0, column=1, pady=5, padx=(0,0) ,columnspan=2)
        infoBitly = ttk.Label(self.root, text="If you don't enter it, the bitly shortener won't work.",font="gotham 9  bold")
        infoBitly.grid(row=1, column=1, pady=5, padx=(0,0) ,columnspan=2)
        tokenurlBitly = ttk.Label(self.root, text="https://dev.bitly.com/docs/getting-started/authentication/",font="gotham 9  bold",foreground="#0000EE", cursor="hand2")
        tokenurlBitly.grid(row=2, column=1, pady=5, padx=(0,0) ,columnspan=2)
        self.bitlyToken = StringVar()
        self.bitlyToken = ttk.Entry(self.root)
        self.bitlyToken.grid(row=3, column=1, pady=5, padx=(20,20), columnspan=1,sticky="nsew")
        self.saveTokens = icon_to_image("github", fill="black", scale_to_width=20)  
        self.saveTokens = ttk.Button(master=self.root,text="Save Apis", command=lambda:self.get_apis(), compound = 'left',cursor="hand2", style="AccentButton")
        self.saveTokens.grid(row=4, column=1, pady=20, padx=20, sticky="e")
        self.root.mainloop()
        
    def get_apis(self):
      app.bitlyAPI = self.bitlyToken.get()
      config.add_section('APIS')
      config['APIS']['bitly'] = self.bitlyToken.get()
      with open("config.ini", 'w') as f:
          config.write(f)
      #Close this window.
      self.root.destroy()
      #start main app.
      app.start()


if __name__ == "__main__":
    app = App()
    app.check_apis()