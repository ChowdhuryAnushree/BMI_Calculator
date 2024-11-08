#	Create a program for a BMI calculator that takes the name, age, height, and weight of a person and stores the data into a file.
#	Allow the application to show weather the user is Underweight, Overweight, Obese, or Normal. Make sure you add validation rules.
#	Add a ‘Show Graph’ button that display a pie chart of the data stored, showing the percentage of people under certain BMI categories.

import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    bmi = int(weight) / ((int(height) / 100) ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

def showgraph():
    categories = {'Obese': 0, 'Normal': 0, 'Overweight': 0,'Underweight': 0}
    with open('user_data.txt','r') as file:
        for line in file:
            status = line.split(',')[-1].strip()
            if status in categories:
                categories[status] += 1

    labels = list(categories.keys())
    sizes = list(categories.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Weight Category Distribution')
    plt.show()

def save_data():
    weight = weightentry.get()
    height = heightentry.get()
    name = nameentry.get()
    if weight != '' and height != '' and name !='':
        age = ageentry.get()
        bmi = calculate_bmi(weight, height)
        with open('user_data.txt', 'a') as filewrite:
            filewrite.write('Name:'+name.title() + ', ' + 'Age: '+age + ', ' + 'Weight: '+ weight +'kg' +', '+ 'Height: '+ height+'cm'+', '+bmi+'\n')
        print('Saved')
    else:
        tkinter.messagebox.showwarning(title='Error:Missing data',message='Enter Weight, height and name of the person to proceed ')
    #tkinter.messagebox.showinfo(message=bmi)
    result_label.config(text="BMI: " + str(bmi))

window = tkinter.Tk()
window.title('BMI Calculator')
frame = tkinter.Frame(window)
frame.pack()

userinfoframe = tkinter.LabelFrame(frame,text = 'User Information')
userinfoframe.grid(row =0, column=0)

namelabel = tkinter.Label(userinfoframe,text='Name')
namelabel.grid(row=0,column=0)
nameentry = tkinter.Entry(userinfoframe)
nameentry.grid(row=0,column=1)

agelabel=tkinter.Label(userinfoframe, text='Age')
agelabel.grid(row=0,column=2)
ageentry=tkinter.Entry(userinfoframe)
ageentry.grid(row=0,column=3)

heightlabel = tkinter.Label(userinfoframe,text='Height(in cm)')
heightlabel.grid(row=1,column=0)
heightentry = tkinter.Entry(userinfoframe)
heightentry.grid(row=1,column=1)

weightlabel=tkinter.Label(userinfoframe, text='Weight(in kg)')
weightlabel.grid(row=1,column=2)
weightentry=tkinter.Entry(userinfoframe)
weightentry.grid(row=1,column=3)


savebtn=tkinter.Button(frame,text='Calculate BMI',command=save_data)
savebtn.grid(row=3,column=0)

showgraphbtn=tkinter.Button(frame,text='Show Graph',command=showgraph)
showgraphbtn.grid(row=4,column=0)

result_label = ttk.Label(window, text="BMI: ")
result_label.pack()

window.mainloop()