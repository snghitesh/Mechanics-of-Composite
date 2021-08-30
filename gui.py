from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt # This package is needed to plot the variation of properties with theta
import numpy as np # Numerical Python package is needed to deal with matrix operations
from tkinter import filedialog as fd
import os
from numpy.core.fromnumeric import choose

from numpy.matrixlib.defmatrix import matrix


window = Tk()
window.title("Mechanics of Composite Term Project GUI")
window['background']='azure'

#window.geometry("1500x1000")

window.iconbitmap(r'D:\HP Mechanics of composites\icon.ico')

#################### Menubar ######################
menu_bar = Menu(window)
window.config(menu=menu_bar)


def open_file():
    filetypes = (('Python file', '*.py'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='D:\\',filetypes=filetypes)
    file=open(filename,'r')
    #print(file.read())
    file.close()
    pass

def cut_edit():
    pass
def copy_edit():
    pass
def paste_edit():
    pass
def undo_edit():
    pass
def redo_edit():
    pass

# File menu
file_menu  = Menu(menu_bar,bg="light yellow",tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=window.quit)

# Edit menu
edit_menu =Menu(menu_bar,bg="light yellow",tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Copy",command=copy_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Paste",command=paste_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=undo_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Redo",command=redo_edit)
###############################################################

#label for fibre
l1 = Label(window, text = "Enter the Properties",font=("Calibre Heading",16,'bold'),bg="azure",justify=LEFT).grid(row=2,column=0,columnspan=2)
l2 = Label(window, text = "Fibre",font=("Times New Roman",14,'bold','underline'),bg="azure").grid(column=0,row=3)
l3 = Label(window, text = "E1 (GPa)",font=("Times New Roman",12),justify=LEFT,bg="azure").grid(row=4)
l4 = Label(window, text = "E2 (GPa)",font=("Times New Roman",12),justify=LEFT,bg="azure").grid(column=0,row=5)
l5 = Label(window, text = "\u03BD12",font=("Times New Roman",12),justify=LEFT,bg="azure").grid(column=0,row=6)
l6 = Label(window, text = "G12 (GPa)",font=("Times New Roman",12),justify=LEFT,bg="azure").grid(column=0,row=7)
l7 = Label(window, text = "Vf %",font=("Times New Roman",12),justify=LEFT,bg="azure").grid(column=0,row=8)

#label for matrix

l8 = Label(window, text = "Matrix",font=("Times New Roman",14,'bold','underline'),justify=RIGHT,bg="azure").grid(column=3,row=3)
l9 = Label(window, text = "E (GPa)",font=("Times New Roman",12),justify=RIGHT,bg="azure").grid(column=3,row=4)
l10 = Label(window, text = "\u03BD",font=("Times New Roman",12),justify=RIGHT,bg="azure").grid(column=3,row=5)
l11 = Label(window, text = "G (GPa)",font=("Times New Roman",12),justify=RIGHT,bg="azure").grid(column=3,row=6)

extralabel = Label(window,text="                    ",bg="azure").grid(column=2,row=2)

e1 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e1.grid(column = 1,row =4) #E1

e2 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e2.grid(column = 1,row =5) #E2

e3 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e3.grid(column = 1,row =6) #nu12

e4 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e4.grid(column = 1,row =7) #G12

e5 = Spinbox(window, width = 13,from_ = 0, to = 100, bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e5.grid(column = 1,row =8) #Vf

e6 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e6.grid(column = 4,row =4) #E

e7 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e7.grid(column = 4,row =5) #nu

e8 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e8.grid(column = 4,row =6) #G

inputlabel = Label(window, text = "Other Input Parameter",font=("Calibre Heading",16,'bold'),justify=LEFT,bg="azure").grid(row=11,column=0,columnspan=2)
l13 = Label(window, text="No. of Laminates (n)",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=12,columnspan=2)
l14 = Label(window, text="Angle of Laminates (in \u00B0)",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=13,columnspan=2)
l15 = Label(window, text="Thickness of Composite (t)",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=14,columnspan=2)

l16 = Label(window, text="Nx",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=15,columnspan=2)
l17 = Label(window, text="Ny",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=16,columnspan=2)
l18 = Label(window, text="Nxy",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=17,columnspan=2)
l19 = Label(window, text="Mx",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=18,columnspan=2)
l20 = Label(window, text="My",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=19,columnspan=2)
l21 = Label(window, text="Mxy",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=20,columnspan=2)

#labu = Label(window,text="(Separate by , )",font=("Times New Roman",13),bg="azure").grid(column=3,row=13)
labu = Label(window,text="mm",font=("Times New Roman",13),bg="azure").grid(column=3,row=14)
labu = Label(window,text="N/mm",font=("Times New Roman",13),bg="azure").grid(column=3,row=15)
labu = Label(window,text="N/mm",font=("Times New Roman",13),bg="azure").grid(column=3,row=16)
labu = Label(window,text="N/mm",font=("Times New Roman",13),bg="azure").grid(column=3,row=17)
labu = Label(window,text="N",font=("Times New Roman",13),bg="azure").grid(column=3,row=18)
labu = Label(window,text="N",font=("Times New Roman",13),bg="azure").grid(column=3,row=19)
labu = Label(window,text="N",font=("Times New Roman",13),bg="azure").grid(column=3,row=20)
labu = Label(window,text="(Separate by , )",font=("Times New Roman",13),bg="azure").grid(column=3,row=21)

e9 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # n
e9.grid(column=2,row=12)

e10 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Angle
e10.grid(column=2,row=13)

e11 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # t
e11.grid(column=2,row=14)

e12 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Nx
e12.grid(column=2,row=15)

e13 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Ny
e13.grid(column=2,row=16)
e13.insert(0,"0")

e14 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Nxy
e14.grid(column=2,row=17)
e14.insert(0,"0")

e15 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Mx
e15.grid(column=2,row=18)
e15.insert(0,"0")

e16 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # My
e16.grid(column=2,row=19)
e16.insert(0,"0")

e17 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") # Mxy
e17.grid(column=2,row=20)
e17.insert(0,"0")

l22 = Label(window,text="\u03B8 range for Plot",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=21,columnspan=2) # theta variation
e18 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken")
e18.grid(column=2,row=21)
e18.insert(0,"-90,90")


inputlabel = Label(window, text = "Strength Paramater",font=("Calibre Heading",16,'bold'),justify=LEFT,bg="azure").grid(row=22,column=0,columnspan=2)
l25 = Label(window, text="XT",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=23,columnspan=2)  
l26 = Label(window, text="YT",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=24,columnspan=2)  
l27 = Label(window, text="XC",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=25,columnspan=2)  
l28 = Label(window, text="YC",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=26,columnspan=2)  
l29 = Label(window, text="S",font=("Times New Roman",13),justify=LEFT,bg="azure").grid(column=0,row=27,columnspan=2)

e19 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") #XT
e19.grid(column=2,row=23)

e20 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") #YT
e20.grid(column=2,row=24)

e21 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") #XC
e21.grid(column=2,row=25)

e22 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") #YC
e22.grid(column=2,row=26)

e23 = Entry(window, width = 15,bg = "floral white",justify=LEFT,borderwidth=4, relief="sunken") #S
e23.grid(column=2,row=27)

labu = Label(window,text="MPa",font=("Times New Roman",13),bg="azure").grid(column=3,row=23)
labu = Label(window,text="MPa",font=("Times New Roman",13),bg="azure").grid(column=3,row=24)
labu = Label(window,text="MPa",font=("Times New Roman",13),bg="azure").grid(column=3,row=25)
labu = Label(window,text="MPa",font=("Times New Roman",13),bg="azure").grid(column=3,row=26)
labu = Label(window,text="MPa",font=("Times New Roman",13),bg="azure").grid(column=3,row=27)

label = Label(window,text="Implement Criteria >>  ",font=("Times New Roman",15),bg="azure").grid(row = 27,column = 4)


def choose():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

    if fibre_select.get() == 'Carbon':
        e1.insert(0,"232")
        e2.insert(0,"15")
        e3.insert(0,"0.279")
        e4.insert(0,"24")
    if fibre_select.get() == 'AS4':
        e1.insert(0,"225")
        e2.insert(0,"15")
        e3.insert(0,"0.2")
        e4.insert(0,"15") 
    if fibre_select.get() == 'E-Glass 1200 tex':
        e1.insert(0,"80")
        e2.insert(0,"80")
        e3.insert(0,"0.2")
        e4.insert(0,"33.33")
    if fibre_select.get() == 'T300':
        e1.insert(0,"230")
        e2.insert(0,"15")
        e3.insert(0,"0.2")
        e4.insert(0,"15")
    if fibre_select.get() == 'E-Glass':
        e1.insert(0,"72.4")
        e2.insert(0,"72.4")
        e3.insert(0,"0.2")
        e4.insert(0,"30.2") 
    if fibre_select.get() == 'Select Fibre':
        messagebox.showerror("Error","Please Select Fibre")
    #if fibre_select.get() == 'Add':
        #fib_opt['state'] = 'normal'
    #    fib_opt['values']+=(fibre_select.get())

    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    if matrix_select.get() == "Epoxy-1":
        e6.insert(0,"3.45")
        e7.insert(0,"0.35")
        e8.insert(0,f"{(float(e6.get())/(2*(1 + float(e7.get())))):0.2f}")
    if matrix_select.get() == "Epoxy-2":
        e6.insert(0,"5.35")
        e7.insert(0,"0.35")
        e8.insert(0,f"{(float(e6.get())/(2*(1 + float(e7.get())))):0.2f}")
    if matrix_select.get() == "3501-6 Epoxy":
        e6.insert(0,"4.2")
        e7.insert(0,"0.34")
        e8.insert(0,f"{(float(e6.get())/(2*(1 + float(e7.get())))):0.2f}")
    if matrix_select.get() == "BSL914c Epoxy":
        e6.insert(0,"4")
        e7.insert(0,"0.35")
        e8.insert(0,f"{(float(e6.get())/(2*(1 + float(e7.get())))):0.2f}")
    if matrix_select.get() == "DY063 Epoxy":
        e6.insert(0,"3.35")
        e7.insert(0,"0.35")
        e8.insert(0,f"{(float(e6.get())/(2*(1 + float(e7.get())))):0.2f}")
    if matrix_select.get() == 'Select Matrix':
        messagebox.showerror("Error","Please Select Matrix")
    #if matrix_select.get() == 'Add':
    #    #mat_opt['state'] = 'normal'
    #    mat_opt['values']+=(matrix_select.get())

fibre_select = StringVar()
matrix_select = StringVar()

fib_opt = ttk.Combobox(window,width=14 ,textvariable=fibre_select)
fib_opt.grid(row=3,column=1)

mat_opt = ttk.Combobox(window,width=14, textvariable=matrix_select)
mat_opt.grid(row=3,column=4)

fib_opt['values'] = ['Select Fibre','Carbon','AS4','E-Glass 1200 tex','T300','E-Glass']
mat_opt['values'] = ['Select Matrix','Epoxy-1','Epoxy-2','3501-6 Epoxy','BSL914c Epoxy','DY063 Epoxy']

fib_opt['state'] = 'readonly'
mat_opt['state'] = 'readonly'

fib_opt.current(0)
mat_opt.current(0)

select_button = Button(window,text = "Default Input",font=("Calibre",10,'bold'),bg="light blue",command = choose).grid(row=3,column=2)

####################################################### Label Frame #####################################################
labelframe=LabelFrame(window,text="OUTPUT",width=600,cursor = "target",  height=600,fg = "black", font = "Calibri",bg="papaya whip")  
labelframe.grid(row=2,column=6,rowspan=20,columnspan=7)
labelframe.grid_propagate(FALSE)

#########################################################################################################################

def properties():
    myLabel1 = Label(window,text="                         ",bg="azure").grid(column=5,row=3)
    E1 = e1.get() # Longitudinal Modulous of Fibre
    if E1=="0":
        messagebox.showwarning("Warning","E1 value should be >0")
        return
    elif E1== "":
        messagebox.showerror("Error","Please enter value of E1")
        return
    else:
        try:
            E1 = float(e1.get())
            if E1<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of E1")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of E1")
            return

    E2 = e2.get() # Transverse Modulous of Fibre
    if E2=="0":
        messagebox.showwarning("Warning","E2 value should be >0")
        return
    elif E2== "":
        messagebox.showerror("Error","Please enter value of E2")
        return
    else:
        try:
            E2 = float(e2.get())
            if E2<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of E2")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of E2")
            return

    nu12 = e3.get() # Poission's ratio of Fibre in 1-2 plane
    if nu12=="0":
        messagebox.showwarning("Warning","\u03BD12 value should be greater than 0")
        return
    elif nu12== "":
        messagebox.showerror("Error","Please enter value of \u03BD12")
        return
    else:
        try:
            nu12 = float(e3.get())
            if nu12<=0 or nu12>1:
                messagebox.showwarning("Warning","Please enter value of \u03BD12 between 0 and 1")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of \u03BD12")
            return

    G12 = e4.get() # Shear Modulous of Fibre 
    if G12=="0":
        messagebox.showwarning("Warning","G12 value should be > 0")
        return
    elif G12== "":
        messagebox.showerror("Error","Please enter value of G12")
        return
    else:
        try:
            G12 = float(e4.get())
            if G12<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of G12")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of G12")
            return

    #Matrix Properties
    Em = e6.get() # Elastic Modulous of Matrix
    if Em=="0":
        messagebox.showwarning("Warning","E value should be > 0")
        return
    elif Em== "":
        messagebox.showerror("Error","Please enter value of E")
        return
    else:
        try:
            Em = float(e6.get())
            if Em<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of E")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of E")
            return

    nu = e7.get() # Poissions ratio of Matrix
    if nu=="0":
        messagebox.showwarning("Warning","\u03BD value should be greater than 0 ")
        return
    elif nu== "":
        messagebox.showerror("Error","Please enter value of \u03BD")
        return
    else:
        try:
            nu = float(e7.get())
            if nu<=0 or nu>1:
                messagebox.showwarning("Warning","Please enter value of \u03BD between 0 and 1")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of \u03BD")
            return

    G = e8.get()     #Calculating a shear modulous of matrix by assuming a isotropic matrix material if user if not giving input
    if G=="0":
        messagebox.showwarning("Warning","G value should be > 0")
        return
    elif G== "":
        messagebox.showerror("Error","Please enter value of G")
        return
    else:
        try:
            G = float(e8.get())
            if G<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of G")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of G")
            return

    #Fibre volume fraction
    vf = e5.get() # Fibre volume fraction in total volume of composite (input taken in percentage)
    if vf=="":
        messagebox.showerror("Error","Please enter value of fibre volume fraction")
        return
    else:
        try:
            vf = float(e5.get())/100
            if vf<=0 or vf>=1:
                messagebox.showwarning("Warning","Please enter fibre volume fraction % between 0 to 100")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of fibre volume fraction")
            return

    vm = (1-vf)              # Matrix volume fraction in total volume of composite
    # calculation of Effective Properties of Composite
    global E1_C,E2_C,G12_C,nu12_C,E3_C
    E1_C = (vf*E1 + vm*Em)*10**3  # Elastic modulous of composite material in longitudinal direction
    E2_C = (E2*Em/(E2*vm + Em*vf))*10**3 # Elastic modulous of composite material in transverse direction
    G12_C = (G12*G/(G12*vm + G*vf))*10**3 # Shear modulous of composite material 
    nu12_C = vf*nu12 + vm*nu #Poisson's ratio of composite material in 1-2 plane 
    E3_C = E2_C # E3 = E2 as material given is transversely isotropic

    extralabel=Label(labelframe,text="                 ",bg="papaya whip").grid(row=0,column=0)
    cal_frame = LabelFrame(labelframe,text="~~~~~~~~~~~~ EFFECTIVE PROPERTIES OF COMPOSITES ~~~~~~~~~~~~",width=400,cursor = "target",  height=500,fg = "navy", font = "Calibri",bg="papaya whip")
    cal_frame.grid(row=0,column=1,rowspan=5,columnspan=5)

    extralabel=Label(cal_frame,text="                 ",bg="papaya whip").grid(row=0,column=0)
    #myLabel2 = Label(labelframe, text="Effective Properties of Composite\n",font=("Calibre Heading",16,'bold'),bg="papaya whip").grid(column = 0,row = 0,columnspan=3)
    E1_label = Label(cal_frame, text="  E1  = "+str(f"{E1_C:0.2f}  MPa"),font = ("Times New Roman",12),width = 25,anchor=W,bg="papaya whip").grid(column=0,row=1)
    e1rule = Label(cal_frame,text="(Linear Rule of Mixture)",font = ("Times New Roman",12),fg="dark green",bg="papaya whip").grid(row=1,column=1)
    
    E2_label = Label(cal_frame, text="  E2  = "+str(f"{E2_C:0.2f}  MPa"),font = ("Times New Roman",12),width = 25,anchor=W,bg="papaya whip").grid(column=0,row=2)
    e2rule = Label(cal_frame,text="(Inverse Rule of Mixture)",font = ("Times New Roman",12),fg="dark green",bg="papaya whip").grid(row=2,column=1)

    G12_label = Label(cal_frame, text="  G12  = "+str(f"{G12_C:0.2f}  MPa"),font = ("Times New Roman",12),width = 25,anchor=W,bg="papaya whip").grid(column=0,row=3)
    g12rule = Label(cal_frame,text="(Inverse Rule of Mixture)",font = ("Times New Roman",12),fg="dark green",bg="papaya whip").grid(row=3,column=1)

    nu12_label = Label(cal_frame, text="  \u03BD12  = "+str(f"{nu12_C:0.2f}"),font = ("Times New Roman",12),width = 25,anchor=W,bg="papaya whip").grid(column=0,row=4)
    nu12rule = Label(cal_frame,text="(Linear Rule of Mixture)",font = ("Times New Roman",12),fg="dark green",bg="papaya whip").grid(row=4,column=1)

    E3_label = Label(cal_frame, text="  E3  = "+str(f"{E3_C:0.2f}  MPa"),font = ("Times New Roman",12),width = 25,anchor=W,bg="papaya whip").grid(column=0,row=5)
    e3rule = Label(cal_frame,text="(Inverse Rule of Mixture)",font = ("Times New Roman",12),fg="dark green",bg="papaya whip").grid(row=5,column=1)


    ABD_button = Button(window, height=10,width=8, text ="Calculate\n\n[A]\n\n[B]\n\n[D]\n\nMatrix",font = ("Times New Roman",14,'bold'),bg = "light blue",command=ABD_matrix).grid(column =4 ,row =14,rowspan=8)
    

def info_about_laminate():
    global n_layer,E
    if e9.get()=='':
        messagebox.showerror("Error","Please enter the value of number of layers first and then select symmetric")
        return
    else:
        try:
            n_layer = int(float(e9.get()))         # Number of layer in a composite
            if 0<=n_layer<2:
                messagebox.showerror("Error","Number of layers cannot be less than 2")
                return

            if n_layer%2 == 0:
                if Checkbutton1.get()==1:
                    messagebox.showinfo("Number of layers",f"Enter {n_layer/2} laminate angles and separate it by comma")
                    return
            if n_layer%2 != 0:
                if Checkbutton1.get()==1:
                    messagebox.showerror("Number of layers","Composite material cannot form symmetric structure as number of laminates are odd. Please enter all angles manually.")
                    return
            if n_layer<0:
                messagebox.showerror("Error","Do not enter negative value of number of layers")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of number of layers")
            return

Checkbutton1 = IntVar()
  
CB1 = Checkbutton(window, text = "Symmetric",font=("Arial",10,"bold"), variable = Checkbutton1,onvalue = 1,offvalue = 0,bg="azure",command=info_about_laminate).grid(row=13,column=3)


#------------------------------------[A],[B],[D] Matrix Part and Plotting of Properties----------------------------------------
def ABD_matrix():
    global A,B,D,mat,Q_list,z_list,Q,S,n_layer,T_sig_list,E
    nu21_C = nu12_C*E2_C/E1_C #nu21 not equal to nu12

    #Now we calculate S matrix
    S11 = 1/(E1_C)  # S11 Calculation
    S12 = -nu21_C/(E2_C)  #S22 Calculation
    S21 = -nu12_C/(E1_C) # S21 Calculation
    S22 = 1/(E2_C) # S22 Calculation
    S33 = 1/(E3_C) # S33 Calculation
    S66 = 1/(G12_C) # S66 Calculation

    #S Matrix Formation
    S = np.array([[S11,S12,0],[S21,S22,0],[0,0,S66]]) 

    #Q Matrix Formation
    Q = np.linalg.inv(S) # Inverting a S matrix
    
    #E = e10.get().split(",")        # Angles
    try:
        n_layer = int(float(e9.get())) 
    except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of number of layers")
            return

    if n_layer%2 ==0 and Checkbutton1.get()==1:
        E1 = e10.get().split(",")
        if len(E1)==n_layer/2:
            E2 = E1[::-1]
            E = E1+E2
            if len(E)!=n_layer:
                messagebox.showerror("Error","Please check number of input angles entered. There might be some mistake.")
                return
        else:
            messagebox.showerror("Error",f"You should have to enter {n_layer/2} angles only but you entered {len(E1)}. Please correct it")
            return
    else:
        E = e10.get().split(",")
        if len(E)!=n_layer and Checkbutton1.get()==0:
            messagebox.showerror("Error","Please check number of input angles entered. There might be some mistake.")
            return

    Q_list = []
    T_sig_list = []
    for j in range(0,n_layer):
        #print(f"\nLaminate layer {j+1}:")
        try:
            theta = float(E[j])   # Taking theta input in degrees for each layer 
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of angles of laminate")
            return

        thetar = theta*np.pi/180          # Converting theta into radians as numpy take angle in radians
        m = np.cos(thetar)                # Define m = cos(theta)
        n = np.sin(thetar)                # Define n = sin(theta)

        T_sigma = np.array([[m**2,n**2,2*m*n],[n**2,m**2,-2*m*n],[-m*n,m*n,(m**2-n**2)]])   # Defining a T sigma matrix
        #print("\nSigma Transformation Matrix:\n",T_sigma)

        T_epsilon = np.array([[m**2,n**2,m*n],[n**2,m**2,-m*n],[-2*m*n,2*m*n,(m**2-n**2)]]) # Definig a T epsilon matrix
        #print("\nStrain Transformation Matrix:\n",T_epsilon)

        #S_bar = np.matmul(np.matmul(np.linalg.inv(T_epsilon),S),T_sigma)
        Q_bar = np.matmul(np.matmul(np.linalg.inv(T_sigma),Q),T_epsilon) # Conversion of Q matrix from 1-2 coordinate to X-Y

        #print(f"\nQ matrix for layer {j+1}:\n",Q_bar)
        Q_list.append(Q_bar)
        T_sig_list.append(T_sigma)
    #print(Q_list)

    #A matrix
    A = np.zeros((3,3))       # Creating a blank array for A matrix
    B = np.zeros((3,3))       # Creating a blank array for B matrix
    D = np.zeros((3,3))       # Creating a blank array for D matrix
    t = e11.get()      # Total thickness of composite material
    if t=="0":
        messagebox.showwarning("Warning","Please enter the composite material thickness greater than 0")
        return
    elif t=="":
        messagebox.showerror("Warning","Please enter the value of thickness")
        return
    else:
        try:
            t = float(e11.get())
            if t<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of thickness of composite")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of thickness of composite")
            return

    t_k = t/n_layer           # Thickness of individual laminate in composite
    z_list = []
    b = 0
    a = -(n_layer)/2*t_k

    for i in range(0,(n_layer +1)): # For loop for creation of Z coordinates of each layers
        a = a + b
        b = t_k 
        z_list.append(a)
    #print("\nco-ordinate from mid plane of laminate : \n",z_list)
    
    extralabel = Label(window,text="       ",bg="azure").grid(column=5,row=12)
    

    for i in range(3):              #For loop for creating an A, B, D matrix separately
        for j in range(3):
            for k in range(len(Q_list)):
                A[i,j] = Q_list[k][i,j]*(z_list[k+1]-z_list[k]) + A[i,j]
                B[i,j] = (1/2) *Q_list[k][i,j]*((z_list[k+1])**2-(z_list[k])**2) + B[i,j]
                D[i,j] = (1/3) *Q_list[k][i,j]*((z_list[k+1])**3 -(z_list[k])**3) + D[i,j]

    A1 = np.around(A,decimals = 3) # Round off the A matrix elements upto 3 digits
    B1 = np.around(B,decimals = 3) # Round off the B matrix elements upto 3 digits
    D1 = np.around(D,decimals = 3) # Round off the D matrix elements upto 3 digits

    mat_frame = LabelFrame(labelframe,text="~~~~~~~~~~~~~~~~~~~~~~ MATRIX OUTPUT ~~~~~~~~~~~~~~~~~~~~~~",width=500,cursor = "target",  height=600,fg = "navy", font = "Calibri",bg="papaya whip")
    mat_frame.grid(row=7,column=1,columnspan=4)

    #Display A,B,D matrix
    extralabel = Label(window,text="                    ",bg="azure").grid(column=5,row=15)
    extralabel = Label(labelframe,text="                    ",bg="papaya whip").grid(column=0,row=6)
    extralabel = Label(mat_frame,text="                    ",bg="papaya whip").grid(column=0,row=0)
    extralabel = Label(mat_frame,text="                    ",bg="papaya whip").grid(column=0,row=4)
    extralabel = Label(mat_frame,text="                    ",bg="papaya whip").grid(column=0,row=8)
    l25 = Label(mat_frame, text="[A]  = ",font=("Times New Roman",13),bg="papaya whip").grid(column=0,row=2)
    l26 = Label(mat_frame, text="[B]  = ",font=("Times New Roman",13),bg="papaya whip").grid(column=0,row=6)
    l27 = Label(mat_frame, text="[D]  = ",font=("Times New Roman",13),bg="papaya whip").grid(column=0,row=10)

    extralabel = Label(mat_frame,text = "     ",font=("Times New Roman",13),bg="papaya whip").grid(row=2,column=4)
    Aunit = Label(mat_frame,text = "N/mm",font=("Times New Roman",13),bg="papaya whip").grid(row=2,column=5)
    Bunit = Label(mat_frame,text = "N",font=("Times New Roman",13),bg="papaya whip").grid(row=6,column=5)
    Dunit = Label(mat_frame,text = "N-mm",font=("Times New Roman",13),bg="papaya whip").grid(row=10,column=5)
    for i in range(3):
        for j in range(3):
            l22 = Label(mat_frame,text=str(A1[i,j]),font=("Times New Roman",13),width=12,relief=SUNKEN,fg="red",bg="papaya whip").grid(column=j+1,row=i+1)
            l23 = Label(mat_frame,text=str(B1[i,j]),font=("Times New Roman",13),width=12,relief=SUNKEN,fg="RoyalBlue4",bg="papaya whip").grid(column=j+1,row=i+5)
            l24 = Label(mat_frame,text=str(D1[i,j]),font=("Times New Roman",13),width=12,relief=SUNKEN,fg="SpringGreen4",bg="papaya whip").grid(column=j+1,row=i+9)

    extralabel = Label(mat_frame,text="                    ",bg="papaya whip").grid(column=0,row=12)
    mat1 = np.concatenate([A,B])             # Merging of A and B matrix
    mat2 = np.concatenate([B,D])             # Merging of B and D matrix
    mat = np.concatenate((mat1,mat2),axis=1) # Final Merging of 1st and 2nd matrix vertically
    matt = np.around(mat,decimals = 2)       # Round off the Element of ABD matrix upto digits
    return


def plots():
    global Ex_var,Ey_var,Gxy_var,Q16_var,x 
    theta_range = e18.get().split(",")
    if len(theta_range)>2:
        messagebox.showerror("Error",f"Please enter only two \u03B8 value only separated by comma in \u03B8 range for plot. You entered {len(theta_range)} values")
        return
    if len(theta_range)==0:
        messagebox.showerror("Error","Please enter value of \u03B8 in \u03B8 range for plot ")
        return
    #print(theta_range)
    def plot1(theta1):              # Function Defination for plotting a graph  
        thetar = theta1*np.pi/180 # Converting theta in radians
        m = np.cos(thetar)  #define m=cos(theta)
        n = np.sin(thetar)  #define n=sin(theta)

        T_sigma = np.array([[m**2,n**2,2*m*n],[n**2,m**2,-2*m*n],[-m*n,m*n,(m**2-n**2)]])   # [T_sigma] matrix
        #print("\nSigma Transformation Matrix:\n",T_sigma)

        T_epsilon = np.array([[m**2,n**2,m*n],[n**2,m**2,-m*n],[-2*m*n,2*m*n,(m**2-n**2)]]) # [T_epsilon] matrix
        #print("\nStrain Transformation Matrix:\n",T_epsilon)

        Q_bar = Q 

        #print("\nCompliance Matrix of XY plane:\n",S_bar)
        #print("\nStiffness Matrix of XY plane:\n",Q_bar)

        inv_Ex = m**4/E1_C + m**2*n**2*(1/G12_C - 2*nu12_C/E1_C) + n**4/E2_C
        Ex = 1/inv_Ex      # Ex formula for Variation vs theta

        nu_xy = Ex*((nu12_C/E1_C)*(m**4+n**4)-m**2*n**2*(1/E1_C + 1/E2_C - 1/G12_C))

        inv_Ey = n**4/E1_C + m**2*n**2*(1/G12_C - 2*nu12_C/E1_C) + m**4/E2_C
        Ey = 1/inv_Ey     # Eyformula for Variation vs theta

        #etaxy_x = Ex*(m**3*n*(2/E1_C + 2*nu12_C/E1_C - 1/G12_C) - m*n**3*(2/E2_C + 2*nu12_C/E1_C - 1/G12_C))

        #etaxy_y = Ex*(m*n**3*(2/E1_C + 2*nu12_C/E1_C - 1/G12_C) - m**3*n*(2/E2_C + 2*nu12_C/E1_C - 1/G12_C))

        inv_Gxy = 4*m**2*n**2*(1/E1_C + 1/E2_C + 2*nu12_C/E1_C) + (m**2-n**2)**2/G12_C
        Gxy = 1/inv_Gxy    # Gxy formula for variation vs theta

        Q16 = m**3*n*(Q_bar[0][0]-Q_bar[0][1]) + m*n**3*(Q_bar[0][1] - Q_bar[1][1]) - 2*m*n*(m**2-n**2)*Q_bar[2][2]
        return Ex,Ey,Gxy,Q16  

    try:
        i = float(theta_range[0])     #Lower theta limit for variation
        theta = float(theta_range[1]) # Upper theta limit for variation
    except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of angles in \u03B8 range ")
            return

    Ex_var = []
    Ey_var = []
    Gxy_var = []
    Q16_var = []
    x =[]
    while(i<=theta):
        Ex_var.append(plot1(i)[0])  # Creating a bunch of E1 values for plot
        Ey_var.append(plot1(i)[1])  # Creating a bunch of E2 values for plot
        Gxy_var.append(plot1(i)[2]) # Creating a bunch of Gxy values for plot
        Q16_var.append(plot1(i)[3]) # Creating a bunch of Q16 values for plot
        x.append(i)                                      # Creating bunch of data for X axis in plot
        i=i+1
    #E_1 = Button(window,height=1,width=10, text ="E1",font = ("Times New Roman",12,'bold'),bg = "light blue",command=E1_plot).grid(column =5 ,row =25)
    #E_2 = Button(window, height=1,width=10, text ="E2",font = ("Times New Roman",12,'bold'),bg = "light blue",command=E2_plot).grid(column =6 ,row =25)
    #G_12 = Button(window, height=1,width=10, text ="G12",font = ("Times New Roman",12,'bold'),bg = "light blue",command=G12_plot).grid(column =5 ,row =26)
    #Q_16 = Button(window, height=1,width=10, text ="Q16",font = ("Times New Roman",12,'bold'),bg = "light blue",command=Q16_plot).grid(column =6 ,row =26)
    def show():
        plot_req = clicked.get()
        if (plot_req == 'E1 vs \u03F4'):
            E1_plot()
        if plot_req == "E2 vs \u03F4":
            E2_plot()
        if plot_req == "G12 vs \u03F4":
            G12_plot()
        if plot_req == "Q16 vs \u03F4":
            Q16_plot()

    options = ["E1 vs \u03F4","E2 vs \u03F4","G12 vs \u03F4","Q16 vs \u03F4"]
    clicked = StringVar()

    # initial menu text
    clicked.set("- - - - - - Select - - - - - - " )
  
    # Create Dropdown menu
    drop = OptionMenu( window , clicked , *options)
    drop.config(width=18,height=1)
    drop.config(bg="snow",fg="gray1")
    drop.config(font=("Times New Roman",12,'bold'))
    drop.grid(column=5,row=24,rowspan=2)
  
    # Create button, it will change label text
    button = Button( window , text = "Show" ,font=("Times New Roman",12,'bold'),bg="light blue",height=1,width=11, command = show ).grid(column=6,row=24,rowspan=2)





def E1_plot():
    plt.figure(1)
    plt.plot(x,Ex_var)  # Plot of Ex versus theta variation
    plt.title("E1 Vs Angle \u03F4\n",fontsize=24)
    plt.xlabel("\u03F4\u00b0 ---->",fontsize = 16)              # X lable for the plot
    plt.ylabel("E1 (MPa) ---->",fontsize = 16)
    plt.legend([" E1"],prop={"size":15},loc = 1,ncol=4)
    plt.grid()
    plt.show()

def E2_plot():
    plt.figure(2)
    plt.plot(x,Ey_var)  # Plot of Ex versus theta variation
    plt.title("E2 Vs Angle \u03F4\n",fontsize=24)
    plt.xlabel("\u03F4\u00b0 ---->",fontsize = 16)              # X lable for the plot
    plt.ylabel("E2 (MPa) ---->",fontsize = 16)
    plt.legend([" E2"],prop={"size":15},loc = 1,ncol=4)
    plt.grid()
    plt.show()
    
def G12_plot():
    plt.figure(3)
    plt.plot(x,Gxy_var)  # Plot of Ex versus theta variation
    plt.title("G12 Vs Angle \u03F4\n",fontsize=24)
    plt.xlabel("\u03F4\u00b0 ---->",fontsize = 16)              # X lable for the plot
    plt.ylabel("G12 (MPa) ---->",fontsize = 16)
    plt.legend([" G12"],prop={"size":15},loc = 1,ncol=4)
    plt.grid()
    plt.show()
    
def Q16_plot():
    plt.figure(4)
    plt.plot(x,Q16_var)  # Plot of Ex versus theta variation
    plt.title("Q16 Vs Angle \u03F4\n",fontsize=24)
    plt.xlabel("\u03F4\u00b0 ---->",fontsize = 16)              # X lable for the plot
    plt.ylabel("Q16 (MPa) ---->",fontsize = 16)
    plt.legend([" Q16"],prop={"size":15},loc = 1,ncol=4)
    plt.grid()
    plt.show()
    

def Hashin_failure():    
    XT = e19.get() # Taking Tensile Strength Input in X direction
    if XT=="0":
        messagebox.showwarning("Warning","Please enter XT value greater than 0")
        return
    elif XT=="":
        messagebox.showerror("Error","Please enter XT value")
        return
    else:
        try:    
            XT = float(e19.get()) 
            if XT<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of XT")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of XT")
            return

    YT = e20.get() # Taking Tensile Strength Input in Y direction
    if YT=="0":
        messagebox.showwarning("Warning","Please enter YT value greater than 0")
        return
    elif YT=="":
        messagebox.showerror("Error","Please enter YT value")
        return
    else:
        try:
            YT = float(e20.get()) 
            if YT<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of YT")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of YT")
            return

    XC = e21.get() # Taking Compressive Strength Input in X direction
    if XC=="0":
        messagebox.showwarning("Warning","Please enter XC value greater than 0")
        return
    elif XC=="":
        messagebox.showerror("Error","Please enter XC value")
        return
    else:
        try:
            XC = float(e21.get())
            if XC<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of XC")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of XC")
            return

    YC = e22.get() # Taking Compressive Strength Input in Y direction
    if YC=="0":
        messagebox.showwarning("Warning","Please enter YC value greater than 0")
        return
    elif YC=="":
        messagebox.showerror("Error","Please enter YC value")
        return
    else:
        try:
            YC = float(e22.get())
            if YC<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of YC")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of YC")
            return

    S = float(e23.get())  # Taking Shear Strength Input where S12=S23 assumption is followed
    if S=="0":
        messagebox.showwarning("Warning","Please enter S value greater than 0")
        return
    elif S=="":
        messagebox.showerror("Error","Please enter S value")
        return
    else:
        try:
            S = float(e23.get())
            if S<=0:
                messagebox.showerror("Error","Do not enter negative or 0 value of S")
                return
        except ValueError:
            messagebox.showerror("Error","Please check and enter only numerical value of S")
            return

    def hashin(XT,XC,YT,YC,S):
        global R_listTF,R_listTM,R_listCM,R_listCF,sigklist,tenslistM,complistM,tenslistF,complistF
        Nx = e12.get()               # Taking Nx input
        if Nx=="":
            messagebox.showerror("Error","Please enter Nx value")
            return
        else:
            try:
                Nx = float(e12.get())
                if Nx<0:
                    messagebox.showerror("Error","Do not enter negative value of Nx")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of Nx")
                return

        Ny = e13.get()               # Taking Ny input
        if Ny=="":
            messagebox.showerror("Error","Please enter Ny value")
            return
        else:
            try:
                Ny = float(e13.get()) 
                if Ny<0:
                    messagebox.showerror("Error","Do not enter negative value of Ny")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of Ny")
                return


        Nxy = e14.get()              # Taking Nxy input
        if Nxy=="":
            messagebox.showerror("Error","Please enter Nxy value")
            return
        else:
            try:
                Nxy = float(e14.get())
                if Nxy<0:
                    messagebox.showerror("Error","Do not enter negative value of Nxy")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of Nxy")
                return
        Mx = e15.get()               # Taking Mx input
        if Mx=="":
            messagebox.showerror("Error","Please enter Mx value")
            return
        else:
            try:
                Mx = float(e15.get())
                if Mx<0:
                    messagebox.showerror("Error","Do not enter negative value of Mx")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of Mx")
                return
        My = e16.get()               # Taking My input
        if My=="":
            messagebox.showerror("Error","Please enter My value")
            return
        else:
            try:
                My = float(e16.get())
                if My<0:
                    messagebox.showerror("Error","Do not enter negative value of My")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of My")
                return

        Mxy = float(e17.get())              # Taking Mxy input
        if Mxy=="":
            messagebox.showerror("Error","Please enter Mxy value")
            return
        else:
            try:
                Mxy = float(e17.get())
                if Mxy<0:
                    messagebox.showerror("Error","Do not enter negative value of Mxy")
                    return
            except ValueError:
                messagebox.showerror("Error","Please check and enter only numerical value of Mxy")
                return

        N_bar = np.array([[Nx],[Ny],[Nxy]])      # Formation of N bar matrix
        M_bar = np.array([[Mx],[My],[Mxy]])      # Formation of M bar matrix
        #print("\nN_bar\n",N_bar)
        #print("\nM_bar\n",M_bar)
        NM = np.concatenate((N_bar,M_bar))       # Formation of NM matrix
        #print("\nNM matrix = \n",NM)
        EK = np.matmul(np.linalg.inv(mat),NM)    # Calculation of epsilon_K matrix
        E_K = np.around(EK,decimals =8)          # Round off epsilon_K matrix upto 8 decimals
        #print("\n\u03B5K = \n",E_K)
        E0 = np.vsplit(E_K,2)[0]                 # Extracting epsilon0 matrix 
        K = np.split(E_K,2)[1]                   # Extracting K matrix 
        #print(E0)
        #print(K)
        
        sigklist = []
        for i in range(len(z_list)-1):                  # For loop for creating an sigma matrix
            z = (z_list[i] + z_list[i+1])/2             # Average of Z value
            E = E0 + z*K                                # Calculating epsilon matrix
            sigmak = np.matmul(Q_list[i],E)             # Calculating sigma xy matrix
            sigmak12 = np.matmul(T_sig_list[i],sigmak)  # Calculating sigma 12 matrix
            sigk12 = np.around(sigmak12,decimals=3)
            sigklist.append(sigk12)
            #print(sigklist)
            #print(f"\n\u03B5 Matrix {i+1}\n {E}")
            #print(f"\n\u03C3 X-Y Matrix ({i+1})\n {sigmak}")
            #print(f"\n\u03C3 1-2 Matrix ({i+1})\n {sigmak12}")
            sigma33 = 0                # sigma33 = 0 Since plane stress assumption is taken.
            
            tenslistM = []             # Creating a blank list for sorting purpose
            complistM = []             # Creating a blank list for sorting purpose
            tenslistF = []             # Creating a blank list for sorting purpose
            complistF = []             # Creating a blank list for sorting purpose
            R_listTF = []              # Creating a blank list for sorting purpose
            R_listTM = []              # Creating a blank list for sorting purpose
            R_listCF = []              # Creating a blank list for sorting purpose
            R_listCM = []              # Creating a blank list for sorting purpose        
        
        for i in range(len(sigklist)):
            matcon = sigklist[i][1] + sigma33  # Hashin criteria condition to check matrix failure
            fibcon = sigklist[i][0]            # Hashin criteria conditon to check fibre failure
            sigma11 = sigklist[i][0]           # Fetching sigma11 value from sigmak12 matrix
            sigma22 = sigklist[i][1]           # Fetching sigma22 value from sigmak12 matrix           
            sigma66 = sigklist[i][2]           # Fetching sigma12 value from sigmak12 matrix
            if (matcon > 0):
                cond = ((sigklist[i][1] + sigma33)/YT)**2 + (sigklist[i][2]/S)**2  # Condition for tensile matrix failure
                a = cond            # a,b,c coefficient of aR^2 + bR + c =0 equation
                b = 0
                c = -1
                if (cond <1): # if condition for safe criteria
                     tenslistM.append("Safe")
                     complistM.append("-")
                     R = np.roots([a,b,c])                # Finding a roots of equation
                     R_listTM.append(R)
                     R_listCM.append("-")
                else:               # Condition for unsafe criteria
                    tenslistM.append("Fails")
                    complistM.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listTM.append(R)
                    R_listCM.append("-")
                 
            else:
                cond = ((YC/(2*S))**2 - 1)*(sigklist[i][1]/YC) + (sigklist[i][1]/(4*S))**2 + (sigklist[i][2]/S)**2 # Condition for compressive matrix failure
                a = (sigklist[i][1]/(4*S))**2 + (sigklist[i][2]/S)**2  # a,b,c coefficient of aR^2 + bR + c =0 equation
                b = ((YC/(2*S))**2 - 1)*(sigklist[i][1]/YC)
                c = -1
                if (cond <1):       # if condition for safe criteria        
                    complistM.append("Safe")
                    tenslistM.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listCM.append(R)
                    R_listTM.append("-")
                else:               # Condition for unsafe criteria
                    complistM.append("Fails")
                    tenslistM.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listCM.append(R)
                    R_listTM.append("-")
                 
            if (fibcon > 0):   
                cond = (sigklist[i][0]/XT)**2 + (sigklist[i][2]/S)**2 # Condition for tensile fibre failure
                a = (sigklist[i][0]/XT)**2 + (sigklist[i][2]/S)**2    # a,b,c coefficient of aR^2 + bR + c =0 equation
                b = 0
                c = -1
                if (cond <1):       # if condition for safe criteria
                    tenslistF.append("Safe")
                    complistF.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listTF.append(R)
                    R_listCF.append("-")
                else:               # Condition for unsafe criteria
                    tenslistF.append("Fails")
                    complistF.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listTF.append(R)
                    R_listCF.append("-")
                 
            else:                                                                
                cond = (sigklist[i][0]/XC)**2    # Condition for compressive fibre failure
                a = (sigklist[i][0]/XC)**2       # a,b,c coefficient of aR^2 + bR + c =0 equation
                b = 0
                c = -1
                if (cond <1):       # if condition for safe criteria
                    complistF.append("Safe")
                    tenslistF.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listCF.append(R)
                    R_listTF.append("-")
                else:               # Condition for unsafe criteria
                    complistF.append("Fails")
                    tenslistF.append("-")
                    R = np.roots([a,b,c])                # Finding a roots of equation
                    R_listCF.append(R)
                    R_listTF.append("-")
    hashin(XT, XC, YT, YC, S)
    NW1 = Toplevel()
    NW1.iconbitmap(r'D:\HP Mechanics of composites\icon.ico')
    NW1.title("Hashin Failure Implementation")
    NW1['background']='papaya whip'
    labframe1 = LabelFrame(NW1,text="Hashin Failure Criteria",width=500,cursor = "target",  height=600,fg = "green", font = ("Calibri",14,'bold'),bg="papaya whip" )
    labframe1.grid(row=0,column=1)
    #labframe1.grid_propagate(FALSE)
    #labh = Label(labframe1, text = "Hashin Failure Criteria:",font=("Times New Roman",16,'bold'),bg="papaya whip").grid(row = 0, column = 0)
    extralabel = Label(NW1,text = "       ",bg="papaya whip").grid(row=0,column=0)
    extralabel = Label(NW1,text = "       ",bg="papaya whip").grid(row=0,column=2)
    extralabel = Label(labframe1,text = "         ",bg="papaya whip").grid(row=1,column=0)
    labh = Label(labframe1, text = "Laminate No.",font=("Times New Roman",14,'bold'),fg="OrangeRed4",bg="papaya whip").grid(row = 2, column = 0)
    labh = Label(labframe1, text = "Matrix",font=("Times New Roman",14,'bold'),fg="OrangeRed4",bg="papaya whip").grid(row = 2, column = 1,columnspan=2)
    labh = Label(labframe1, text = "Fibre",font=("Times New Roman",14,'bold'),fg="OrangeRed4",bg="papaya whip").grid(row = 2, column = 3,columnspan=2)
    labh = Label(labframe1, text = "Tensile    ",font=("Times New Roman",14,'bold'),fg="blue4",bg="papaya whip").grid(row = 3, column = 1)
    labh = Label(labframe1, text = "Compressive  ",font=("Times New Roman",14,'bold'),fg="blue4",bg="papaya whip").grid(row = 3, column = 2)
    labh = Label(labframe1, text = "Tensile   ",font=("Times New Roman",14,'bold'),fg="blue4",bg="papaya whip").grid(row = 3, column = 3)
    labh = Label(labframe1, text = "Compressive",font=("Times New Roman",14,'bold'),fg="blue4",bg="papaya whip").grid(row = 3, column = 4)
    for i in range(len(sigklist)):
        lab = Label(labframe1, text = str(i+1),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=4+i,column = 0)
        if str(tenslistM[i])=='-':
            lab = Label(labframe1, text= str(tenslistM[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=1)
        else:
            if str(tenslistM[i]) == "Safe":
                lab = Label(labframe1, text= str(tenslistM[i]),font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row=4+i,column=1)
            else:
                lab = Label(labframe1, text= str(tenslistM[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=1)

        if str(complistM[i])=='-':
            lab = Label(labframe1, text= str(complistM[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=2)
        else:
            if str(complistM[i]) == "Safe":
                lab = Label(labframe1, text= str(complistM[i]),font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row=4+i,column=2)
            else:
                lab = Label(labframe1, text= str(complistM[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=2)

        if str(tenslistF[i])=='-':
            lab = Label(labframe1, text= str(tenslistF[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=3)
        else:
            if str(tenslistF[i]) == "Safe":
                lab = Label(labframe1, text= str(tenslistF[i]),font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row=4+i,column=3)
            else:
                lab = Label(labframe1, text= str(tenslistF[i]),font=("Times New Roman",14,'bold'),fg="red",bg="papaya whip").grid(row=4+i,column=3)

        if str(complistF[i])=='-':
            lab = Label(labframe1, text= str(complistF[i]),font=("Times New Roman",14,'bold'),fg ="red",bg="papaya whip").grid(row=4+i,column=4)
        else:
            if str(complistF[i]) == "Safe":
                lab = Label(labframe1, text= str(complistF[i]),font=("Times New Roman",14,'bold'),fg ="green",bg="papaya whip").grid(row=4+i,column=4)
            else:
                lab = Label(labframe1, text= str(complistF[i]),font=("Times New Roman",14,'bold'),fg ="red",bg="papaya whip").grid(row=4+i,column=4)

    extralabel = Label(labframe1,text = "         ",bg="papaya whip").grid(row=n_layer+4,column=0)
    Button(NW1, text = "Exit",height=1,width=10,font = ("Times New Roman",12,'bold'),bg='azure', command=NW1.destroy).grid(row=n_layer+5,column=1)

def margin_of_safety():
    rmin1 = [] # Creating a list for sorting purpose
    rmin2 = [] # Creating a list for sorting purpose
    rmin3 = [] # Creating a list for sorting purpose
    rmin4 = [] # Creating a list for sorting purpose
    Rmin1 = 0  # Initializing a variable
    Rmin2 = 0  # Initializing a variable
    Rmin3 = 0  # Initializing a variable
    Rmin4 = 0  # Initializing a variable
    Rfinal=np.zeros((1,n_layer))   # Creating a one dimentional array
    global MF
    MF=[]      # Null list
    for i in range(n_layer):
        MF.append(0)
    
    for i in range(n_layer):       # For loop to extract suitable margin of safety value from Hashin failure criteria
        if (str(R_listTM[i]) == '-'):  # Sorting condition if found null element
            Rmin1 = 0
        if (str(R_listTM[i])!= '-' ):  # Sorting condition for finite value
            Rmin1 = R_listTM[i][0]
            for j in range(2):
                if (0< R_listTM[i][j]<=Rmin1):
                    Rmin1 = R_listTM[i][j]
        rmin1.append(Rmin1)
    
        if (str(R_listCM[i]) == '-'):  # Sorting condition if found null element
            Rmin2 = 0
        if (str(R_listCM[i])!= '-' ):  # Sorting condition for finite value
            Rmin2 = R_listCM[i][0]
            for j in range(2):
                if(0< R_listCM[i][j]<=Rmin2):
                    Rmin2 = R_listCM[i][j]
        rmin2.append(Rmin2)
    
        if (str(R_listTF[i]) == '-'):  # Sorting condition if found null element
            Rmin3 = 0
        if (str(R_listTF[i])!= '-' ):  # Sorting condition for finite value
            Rmin3 = R_listTF[i][0]
            for j in range(2):
                if(0< R_listTF[i][j]<=Rmin3):
                    Rmin3 = R_listTF[i][j]
        rmin3.append(Rmin3)
    
        if (str(R_listCF[i]) == '-'):  # Sorting condition if found null element
            Rmin4 = 0
        if (str(R_listCF[i])!= '-' ):  # Sorting condition for finite value
            Rmin4 = R_listCF[i][0]
            for j in range(2):
                if(0< R_listCF[i][j]<=Rmin4):
                    Rmin4 = R_listCF[i][j]
        rmin4.append(Rmin4)
        lst = [Rmin1,Rmin2,Rmin3,Rmin4]  # Bunch of four possible values of margin of safety
    
        val=max(lst)                      # Initial assignment of value in varible val
        g=0
        for k in lst:                  # for loop to determine type of failure mode
            g=g+1
            if(k!=0 and k>0):
                if(k<=val):
                    Rfinal[0,i]=k
                    val=k
                    if(g==1):
                        MF[i]="Matrix in Tensile"
                    elif(g==2):
                        MF[i]="Matrix in Compressive"
                    elif(g==3):
                        MF[i]="Fibre in Tensile"
                    else:
                        MF[i]="Fibre in Compressive"

    Rfinal1 = np.around(Rfinal,decimals=3) # Round off value of Margin of Safety     
    NW2 = Toplevel()
    NW2.iconbitmap(r'D:\HP Mechanics of composites\icon.ico')
    NW2.title("Margin of Safety")
    NW2['background']='papaya whip'
    labframe2 = LabelFrame(NW2,text="Margin of Safety",width=500,cursor = "target",  height=600,fg = "navy", font = ("Calibri",14,'bold'),bg="papaya whip" )
    labframe2.grid(row=0,column=1)

    extralabel = Label(NW2,text = "      ",bg="papaya whip").grid(row=0,column=0)
    extralabel = Label(NW2,text = "      ",bg="papaya whip").grid(row=0,column=2)
    #labh = Label(labframe2, text = "Margin of Safety Chart:",font=("Times New Roman",16,'bold'),bg="papaya whip").grid(row = 0, column = 0,columnspan=2)
    extralabel = Label(labframe2,text = "         ",bg="papaya whip").grid(row=1,column=0)
    labh = Label(labframe2, text = "Laminate Angle  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 0)
    labh = Label(labframe2, text = "\u03C31 (MPa)  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 1)
    labh = Label(labframe2, text = "\u03C32 (MPa)  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 2)
    labh = Label(labframe2, text = "\u03C312 (MPa)  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 3)
    labh = Label(labframe2, text = "R-Intact  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 4)
    labh = Label(labframe2, text = "Critical Mode  ",font=("Times New Roman",14,'bold'),fg="green",bg="papaya whip").grid(row = 2, column = 5)
    for i in range(len(sigklist)):
        lab = Label(labframe2, text = str(E[i]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column = 0)
        lab = Label(labframe2, text= str(sigklist[i][0,0]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column=1)
        lab = Label(labframe2, text= str(sigklist[i][1,0]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column=2)
        lab = Label(labframe2, text= str(sigklist[i][2,0]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column=3)
        lab = Label(labframe2, text= str(Rfinal1[0][i]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column=4)  
        lab = Label(labframe2, text= str(MF[i]),font=("Times New Roman",14,'bold'),bg="papaya whip").grid(row=3+i,column=5) 

    extralabel = Label(labframe2,text = "         ",bg="papaya whip").grid(row=n_layer+4,column=0)
    Button(NW2, text = "Exit",height=1,width=10,font = ("Times New Roman",12,'bold'),bg='azure', command=NW2.destroy).grid(row=n_layer+5,column=1) 


def analyze():
    inp_req=select.get()
    if inp_req=="Hashin Failure Criteria":
        Hashin_failure()
    if inp_req=="Margin of Safety":
        margin_of_safety()


opt = ['Hashin Failure Criteria','Margin of Safety']
select = StringVar()
select.set("- - - - - - Select - - - - - - ")

drpdwn = OptionMenu(window,select,*opt)
drpdwn.config(width=18,height=1)
drpdwn.config(bg="snow",fg="gray1")
drpdwn.config(font=("Times New Roman",12,'bold'))
drpdwn.grid(column =5 ,row =27)

########################## Buttons ######################################

calc_prop = Button(window, height=1,width=18, text ="Calculate Properties",font = ("Times New Roman",14,'bold'),bg = "light blue",command=properties).grid(column =3 ,row =8,columnspan=2)
#ABD_button = Button(window, height=10,width=8, text ="Calculate\n\n[A]\n\n[B]\n\n[D]\n\nMatrix",font = ("Times New Roman",14,'bold'),bg = "light blue",command=ABD_matrix).grid(column =4 ,row =14,rowspan=8)

Plot_button = Button(window,height=1,width=11, text ="Click for Plots",font = ("Times New Roman",12,'bold'),bg = "light blue",command=plots).grid(column =4 ,row =24,rowspan=2)


#Hashin_button = Button(window,height=1,width=13, text ="Hashin Failure",font = ("Times New Roman",14,'bold'),bg = "light blue",command=Hashin_failure).grid(column =4 ,row =28 )
#MOS_button = Button(window,height=1,width=13, text ="Margin of Safety",font = ("Times New Roman",14,'bold'),bg = "light blue",command=margin_of_safety).grid(column =5 ,row =28 )
button = Button(window,text="Evaluate",font=("Times New Roman",12,'bold'),bg="light blue",height=1,width=11, command = analyze).grid(column=6,row=27)
###########################################################################


window.mainloop()
