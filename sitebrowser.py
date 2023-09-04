from tkinter import Tk, Button,Label,Listbox
import webbrowser
win=Tk()
win.title("web browser")
win.geometry('800x450')
def  open_browser():
    webbrowser.open_new_tab('http:/www.python.org')
Button(win,text='web',command=open_browser,bg='blue',width=24,height=6,font=('arial',17)).grid(row=3,column=3)   
win.mainloop() 
