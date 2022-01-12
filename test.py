from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
import ttkthemes

root=ttkthemes.ThemedTk(theme="arc", toplevel=True, themebg=True)
root.title("测试")
root.geometry("350x250")

btn1=Button(root,text="按钮")
btn1.pack()
root.mainloop()