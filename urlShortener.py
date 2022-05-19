import tkinter as tk
from tkinter import StringVar, ttk
from tokenize import String
import pyshorteners

class App():
  def __init__(self):
    super().__init__()

  def create_window(self):
    self.root = tk.Tk()
    self.root.title("URL Shortener v0.1")
    self.root.option_add("*tearOff", False)
    self.root.geometry("1000x500")
    self.root.columnconfigure(index=0, weight=0)
    self.root.columnconfigure(index=1, weight=1)
    self.root.columnconfigure(index=2, weight=0)
    # self.root.columnconfigure(index=3, weight=1)
    self.root.rowconfigure(index=0, weight=1)
    self.root.rowconfigure(index=1, weight=0)
    self.root.rowconfigure(index=2, weight=0)
    self.root.rowconfigure(index=3, weight=4)
    sizegrip = ttk.Sizegrip(self.root)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style
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
    self.urlInput.grid(row=2, column=1, pady=0, padx=(80,0), columnspan=1,sticky="we")
    #button
    accentbutton = ttk.Button(self.topFrame, text="CUT", style="AccentButton", command=lambda: self.shortUrls())
    accentbutton.grid(row=2, column=2, padx=5, pady=0, sticky="nsew")

    #Bottom Frame
    self.bottomFrame = ttk.Frame(self.root, padding=(0,0, 0, 0))
    self.bottomFrame.grid(row=3, column=1, padx=(20,5),pady=(10,10), sticky="nsew", rowspan=1)
    self.bottomFrame.columnconfigure(index=0, weight=1)
    self.bottomFrame.columnconfigure(index=1, weight=1)
    self.bottomFrame.columnconfigure(index=2, weight=1)
    self.bottomFrame.columnconfigure(index=3, weight=1)
    self.bottomFrame.columnconfigure(index=4, weight=1)
    self.bottomFrame.columnconfigure(index=5, weight=1)

    #label
    label2 = ttk.Label(self.bottomFrame, text="TinyUrl",font="gotham 10  bold",foreground="#333333")
    label2.grid(row=0, column=0, pady=10, padx=(0,0) ,columnspan=1)
    self.tinyurlShorted = StringVar()
    self.urltinyurl = ttk.Entry(self.bottomFrame, state="readonly",textvariable=self.tinyurlShorted)
    self.urltinyurl.grid(row=1, column=0, pady=0, padx=(0,0), columnspan=1,sticky="we")

  def print_url(self,location,url):
      location.insert(url)

  def shortUrls(self):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(self.urlInput.get())
    self.tinyurlShorted.set(short_url)

  def start(self):
    self.create_window()
    self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()