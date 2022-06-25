from tkinter import *

window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t) / 100
    interest = round(i,2)

show_result.destroy()

heading_label= Label(window,text='Simple Interest Calculator',fg='black',bg='white',font=('Calibri',20),bd=5)
heading_label.place(x=50,y=20)

principle = Label(window,fg='black',text='Principle',bg='white',font=('Calibri',20))
principle.place(x=20,y=140)

principle_entry = Entry(window, text = '', bd= 2, width=22)
principle_entry.place(x=150,y=142)

rate = Label(window,fg='black',text='Principle',bg='white',font=('Calibri',20))
rate.place(x=20,y=180)

rate_entry = Entry(window, text = '', bd= 2, width=22)
rate_entry.place(x=150,y=182)

time = Label(window,fg='black',text='Principle',bg='white',font=('Calibri',20))
time.place(x=20,y=240)

time_entry = Label(window,fg='black',text='Principle',bg='white',font=('Calibri',20))
time_entry.place(x=150,y=212)

calculate_button = Button(window,text='Calculate',fg='black',font=('Calibri',12),bg='white',bd=4)
calculate_button.place(x=20,y=260)

result_frame = LabelFrame(window,text='Result',bg='black',font=('Calibri',12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

show_result = Label(result_frame,text=' ',bg='white',font= ('Calibri',12),width=33)
show_result.place(x=20,y=20)
show_result.pack()

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t) / 100
    interest = round(i,2)

show_result.destroy()

message = Label(result_frame,text='Interest' +str(p)+ 'at rate of interest' +str(r)+ 'for' +str(t)+ 'years is' +str(interest), bg='white',font=('Calibri',12),width=33)
message.place(x=20,y=40)
message.pack()
