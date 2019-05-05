from tkinter import *
from tkinter import ttk
from random import random, randint
from time import sleep

root = Tk()

center_a1 = (66,45)
center_a2 = (243,45)
center_a3 = (400,45)
center_b1 = (66,197)
center_b2 = (243,197)
center_b3 = (400,197)

root.title("Добро пожаловать в приложение vi.py")
root.geometry('1500x450')

Label(root,text = 'a1').place(x = center_a1[0], y = center_a1[1])
Label(root,text = 'a2').place(x = center_a2[0], y = center_a2[1])
Label(root,text = 'a3').place(x = center_a3[0], y = center_a3[1])
Label(root,text = 'b1').place(x = center_b1[0], y = center_b1[1])
Label(root,text = 'b2').place(x = center_b2[0], y = center_b2[1])
Label(root,text = 'b3').place(x = center_b3[0], y = center_b3[1])

linecenter = ''

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
table=ttk.LabelFrame(tab1,text = 'Table')
draw_field=ttk.LabelFrame(tab1,text = 'Draw')


tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='yellow unit')
tab_control.add(tab2, text='blue unit')
#############

Label(table, text='cross').grid(column=2, row=0)
Label(table, text='motion').grid(column=3, row=0)

number_of_step = 1

canvas = Canvas(draw_field,width = 500 , height = 300)
canvas.pack()

# Label(canvas , text = 'hello , Canvas!').place(x = 10 , y = 10)

crosses = []
motions = []
btn_edit=[]

Label(draw_field,text = 'a1').place(x = center_a1[0], y = center_a1[1])
Label(draw_field,text = 'a2').place(x = center_a2[0], y = center_a2[1])
Label(draw_field,text = 'a3').place(x = center_a3[0], y = center_a3[1])
Label(draw_field,text = 'b1').place(x = center_b1[0], y = center_b1[1])
Label(draw_field,text = 'b2').place(x = center_b2[0], y = center_b2[1])
Label(draw_field,text = 'b3').place(x = center_b3[0], y = center_b3[1])

def create_step():
    global number_of_step
    global motion
    global cross
    global crosses
    global motions
    global confirm_setting1
    global linecenter
    global linecenter1
    Label(table, text=str('step: ' + str(number_of_step))).grid(column=1, row=number_of_step)
    cross = Entry(table)
    cross.grid(column=2, row=number_of_step)
    motion = Entry(table)
    motion.grid(column=3, row=number_of_step)
    confirm_setting1 = Button(table,text = 'confirm',command = confirm)
    confirm_setting1.grid(column = 4 , row = number_of_step)
    #Label(tab1, text=str('step: ' + str(motion.get()))).grid(column=4, row=number_of_step)
	#saver1 = Button(tab1,text = 'save',command = save1)
    #saver1.grid(column = 5,row = 0
    saver1 = Button(table,text = 'save',command = save1)
    saver1.grid(column = 5,row = 0)
    root.after(1, updater)
    number_of_step += 1
    #canvas.create_line(100, 100, 200, 200)
    btn_plus.destroy()                                                            
    m_unit_1 = crosses
    for i in range(len(m_unit_1)-1):
        if m_unit_1[i] == 'a1':
            linecenter = center_a1
        if m_unit_1[i] == 'a2':
            linecenter = center_a2
        if m_unit_1[i] == 'a3':
            linecenter = center_a3
        if m_unit_1[i] == 'b1':
            linecenter = center_b1
        if m_unit_1[i] == 'b2':
            linecenter = center_b2
        if m_unit_1[i] == 'b3':
            linecenter = center_b3

        if m_unit_1[i+1] == 'a1':
            linecenter1 = center_a1
        if m_unit_1[i+1] == 'a2':
            linecenter1 = center_a2
        if m_unit_1[i+1] == 'a3':
            linecenter1 = center_a3
        if m_unit_1[i+1] == 'b1':
            linecenter1 = center_b1
        if m_unit_1[i+1] == 'b2':
            linecenter1 = center_b2
        if m_unit_1[i+1] == 'b3':
            linecenter1 = center_b3

    canvas.create_line(linecenter[0],linecenter[1],linecenter1[0],linecenter1[1])
    


# Label(tab1,text = str(number_of_step)).grid(column = 4,row = 4)


def updater():
    global btn_plus
    btn_plus = Button(table, text='+', command=create_step)
    btn_plus.grid(column=0, row=number_of_step)


def save1():
    handle1 = open('motion1.txt', 'w')
    handle2 = open('crosses1.txt', 'w')
    for i in range(len(motions)):
        handle1.write(motions[i] + '\n')
    for i in range(len(crosses)):
        handle2.write(crosses[i] + '\n')

def edit():
    pass
def confirm():
    global motion
    global cross
    global crosses
    global motions
    global confirm_setting1
    global number_of_step
    global btn_edit
    global number_of_step
    global motion
    global cross
    global crosses
    global motions
    global confirm_setting1
    global linecenter
    global linecenter1
    
    motions.append(str(motion.get()))
    crosses.append(str(cross.get()))
    print(motions)
    print(crosses)
    confirm_setting1.destroy()
    name_edit = 'edit'+str(number_of_step-1)
    btn_edit.append(Button(table,text = name_edit,command = edit))
    btn_edit[number_of_step-2].grid(column = 4,row = number_of_step-1)

def mouse(event):
    #x = event.x
    #y = event.y
    #print('x: '+str(x))
    #print('y: '+str(y))
    pass

#Button(draw_field,text = '0').pack()
tab_control.pack(expand=1, fill='both')
table.pack(side= LEFT)
draw_field.pack(side = LEFT)
root.bind('<Motion>',mouse)
root.after(100, updater)
root.mainloop()