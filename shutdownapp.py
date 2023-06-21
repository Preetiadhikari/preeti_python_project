from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")



st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button =Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus" ,
 command=restart)
r_button.place(x=150,y=60,height=50,width=200)


rt_button =Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus"
,command=restart_time  )
rt_button.place(x=150,y=170,height=50,width=200) #y=60+50+50=170


lg_button =Button(st,text="log-out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus"
, command=logout)
lg_button.place(x=150,y=270,height=50,width=200)#y=170+50+50=270

st_button =Button(st,text="shut-down",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",
command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)#y=270+50+50=370

















st.mainloop()
