from tkinter import *

window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t) / 100
    interest = round(i,2)
    show_result.destroy()

    message = Label(result_frame,text='Interest' +str(p)+ 'at rate of interest' +str(r)+ 'for' +str(t)+ 'years is' +str(interest), bg='white',font=('Calibri',12),width=55)
    message.place(x=20,y=40)
    message.pack()


heading_label= Label(window,text='Simple Interest Calculator',fg='black',bg='white',font=('Calibri',20),bd=5)
heading_label.place(x=50,y=20)

principle = Label(window,fg='black',text='Principle',bg='white',font=('Calibri',20))
principle.place(x=20,y=100)

principle_entry = Entry(window, text = '', bd= 2, width=22)
principle_entry.place(x=210,y=110)

rate = Label(window,fg='black',text='Rate of interest',bg='white',font=('Calibri',20))
rate.place(x=20,y=140)

rate_entry = Entry(window, text = '', bd= 2, width=22)
rate_entry.place(x=210,y=152)

time = Label(window,fg='black',text='Time',bg='white',font=('Calibri',20))
time.place(x=20,y=180)

time_entry = Entry(window,text='',bd=2,width=22)
time_entry.place(x=210,y=190)

calculate_button = Button(window,text='Calculate',fg='black',font=('Calibri',12),bg='white',bd=4,command=calculate_interest)
calculate_button.place(x=20,y=230)

result_frame = LabelFrame(window,text='Result',bg='black',font=('Calibri',12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=290)

show_result = Label(result_frame,text=' ',bg='white',font= ('Calibri',12),width=55)
show_result.place(x=20,y=20)
show_result.pack()

window.mainloop()


