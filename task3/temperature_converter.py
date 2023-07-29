from tkinter import *

window= Tk()
window.title('Temperature Converter')
window.minsize(width=500, height=300)
window.config(padx=50,pady=2, bg="teal")

label=Label(text='TEMPERATURE CONVERTER',font=('Courrier',25,'bold'))
label.grid(column=2, row=0)
label.config(pady=40, bg="teal")

input=Entry()
input.grid(row=2,column=2)

ans=Label(text=' ',font=('Courrier',15,'bold'))
ans.grid(row=6,column=2)
ans.config(bg="teal")

def convert():
    temp = float(input.get())
    temp_F= temp*9/5+32
    ans['text']='Temperature in Fahrenheit is: '+str(int(temp_F))

def celsius():
    temp = float(input.get())
    temp_C= ((temp-32)*5)/9
    ans['text']='Temperature in Celsius is: '+str(int(temp_C))


button=Button(text='FAHRENHEIT', command=convert)
button.grid(row=2,column=1)

button=Button(text='CELSIUS', command=celsius)
button.grid(row=2,column=3)


window.mainloop()