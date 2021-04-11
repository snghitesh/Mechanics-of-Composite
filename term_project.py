#****************************************** Name: HITESH PRAKASH PATIL *********************************************************
#****************************************** Roll No: 20ME63R21 *****************************************************************
#****************************************** Mechanics of Composite Term Project ************************************************

# This Program is Based on Plane Stress Assumption
# Also the prgram have limitation to validate maximum upto 8 laminate layers
# Some commands have been commented in the code that is for the code validation purpose of Coder only

ip_data =[] 
for inp in open('Input File.txt'): # Taking Input from Text File
    ip_data.append(inp.rstrip().split('='))
    
    
    
#-----------------------------------------------Effective Property Calculation Part---------------------------------------------

#Fibre Properties
E1 = float(ip_data[1][1]) # Longitudinal Modulous of Fibre
E2 = float(ip_data[2][1]) # Transverse Modulous of Fibre
nu12 = float(ip_data[3][1])# Poission's ratio of Fibre in 1-2 plane
G12 = float(ip_data[4][1]) # Shear Modulous of Fibre 

#Matrix Properties
E = float(ip_data[7][1]) # Elastic Modulous of Matrix
nu = float(ip_data[8][1]) # Poissions ratio of Matrix
G = 0.5*E/(1+nu)     #Calculating a shear modulous of matrix by assuming a isotropic matrix material if user if not giving input

#Fibre volume fraction
vf = float(ip_data[9][1])/100 # Fibre volume fraction in total volume of composite (input taken in percentage)
vm = (1-vf)                   # Matrix volume fraction in total volume of composite

# calculation of Effective Properties of Composite
E1C = vf*E1 + vm*E  # Elastic modulous of composite material in longitudinal direction
E2C = E2*E/(E2*vm + E*vf) # Elastic modulous of composite material in transverse direction
G12C = G12*G/(G12*vm + G*vf) # Shear modulous of composite material 
nu12C = vf*nu12 + vm*nu #Poisson's ratio of composite material in 1-2 plane 
E3C = E2C # E3 = E2 as material given is transversely isotropic

print(f"\n-------------------------------------\nEffective Properties of composite are:\n-------------------------------------\nLongitudinal Stiffness E1 = {E1C:0.2f} GPa\nTransverse Stiffness E2 = {E2C:0.2f} GPa\nShear Modulous G12 = {G12C:0.2f} GPa\nPoisson's ratio \u03BD12 = {nu12C:0.3f}")

E1_C = E1C*10**3 #Conversion from GPa to MPa
E2_C = E2C*10**3 #Conversion from GPa to MPa
G12_C = G12C*10**3 #Conversion from GPa to MPa
nu12_C = nu12C 
E3_C = E3C*10**3 #Conversion from GPa to MPa




#------------------------------------[A],[B],[D] Matrix Part and Plotting of Properties----------------------------------------

import numpy as np # Numerical Python package is needed to deal with matrix operations

nu21_C = nu12_C*E2_C/E1_C #nu21 not equal to nu12

# Now we calculate S matrix
S11 = 1/(E1_C)  # S11 Calculation
S12 = -nu21_C/(E2_C)  #S22 Calculation
#S13 = -nu31_C/(E3_C)  #Not required in plane stress assumption
S21 = -nu12_C/(E1_C) # S21 Calculation
S22 = 1/(E2_C) # S22 Calculation
#S23 = -nu32_C/(E3_C) #Not required in plane stress assumption
#S31 = -nu13_C/(E1_C) #Not required in plane stress assumption
#S32 = -nu23_C/(E2_C) #Not required in plane stress assumption
S33 = 1/(E3_C) # S33 Calculation
#S44 = 1/(G23_C) #Not required in plane stress assumption
#S55 = 1/(G13_C) #Not required in plane stress assumption
S66 = 1/(G12_C) # S66 Calculation

# S Matrix Formation
S = np.array([[S11,S12,0],[S21,S22,0],[0,0,S66]]) 
#print("S Matrix: \n",S)

# Q Matrix Formation
Q = np.linalg.inv(S) # Inverting a S matrix
#print("\nQ matrix is: \n",Q)

import matplotlib.pyplot as plt # This package is needed to plot the variation of properties with theta
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
    
i = float(ip_data[10][1])     #Lower theta limit for variation
theta = float(ip_data[11][1]) # Upper theta limit for variation
Ex_var = []
Ey_var = []
Gxy_var = []
Q16_var = []
x =[]
while(i<=theta):
    Ex_var.append(plot1(i-float(ip_data[8][1]))[0])  # Creating a bunch of E1 values for plot
    Ey_var.append(plot1(i-float(ip_data[8][1]))[1])  # Creating a bunch of E2 values for plot
    Gxy_var.append(plot1(i-float(ip_data[8][1]))[2]) # Creating a bunch of Gxy values for plot
    Q16_var.append(plot1(i-float(ip_data[8][1]))[3]) # Creating a bunch of Q16 values for plot
    x.append(i)                                      # Creating bunch of data for X axis in plot
    i=i+1
plt.plot(x,Ex_var)  # Plot of Ex versus theta variation
plt.plot(x,Ey_var)  # Plot of Ey versus theta variation
plt.plot(x,Gxy_var) # Plot of Gxy versus theta variation
plt.plot(x,Q16_var) # Plot of Q16 versus theta variation
plt.title("Variation of Properties with angle \u03F4\u00b0\n",fontsize=24) # Title of plot
plt.xlabel("Variation with \u03F4\u00b0 ---->",fontsize = 16)              # X lable for the plot
plt.ylabel("E1 , E2 , G12 , Q16 ---->",fontsize = 16)                      # Y lable for the plot
plt.legend([" E1"," E2"," G12"," Q16"],prop={"size":15},loc = 1,ncol=4)    # Legends to distinguish between multiple graphs
plt.grid()                                                                 # To on grid in the plot
plt.rcParams['figure.figsize'] = [20,10]                         # Using this command we can change size of plot [width,height]
plt.savefig("Variational plot of properties.pdf")                # To Save plot in pdf format in destination folder
print("\n-----\nPlot:\n-----\n")
plt.show()                                                       # To show the plot in output window


n_layer = int(ip_data[14][1])         # Number of layer in a composite  {Note: Maximum upto 8 layer this code can work}
Q_list = []
T_sig_list = []
for j in range(0,n_layer):
    #print(f"\nLaminate layer {j+1}:")
    theta = float(ip_data[j+17][1])   # Taking theta input in degrees for each layer 
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

# A matrix
A = np.zeros((3,3))       # Creating a blank array for A matrix
B = np.zeros((3,3))       # Creating a blank array for B matrix
D = np.zeros((3,3))       # Creating a blank array for D matrix
t = float(ip_data[25][1]) # Total thickness of composite material
t_k = t/n_layer           # Thickness of individual laminate in composite
z_list = []
b = 0
a = -(n_layer)/2*t_k

for i in range(0,(n_layer +1)): # For loop for creation of Z coordinates of each layers
    a = a + b
    b = t_k 
    z_list.append(a)
#print("\nco-ordinate from mid plane of laminate : \n",z_list)

for i in range(3):              # For loop for creating an A, B, D matrix separately
    for j in range(3):
        for k in range(len(Q_list)):
            A[i,j] = Q_list[k][i,j]*(z_list[k+1]-z_list[k]) + A[i,j]
            B[i,j] = (1/2) *Q_list[k][i,j]*((z_list[k+1])**2-(z_list[k])**2) + B[i,j]
            D[i,j] = (1/3) *Q_list[k][i,j]*((z_list[k+1])**3 -(z_list[k])**3) + D[i,j]
            
A1 = np.around(A,decimals = 3) # Round off the A matrix elements upto 3 digits
B1 = np.around(B,decimals = 3) # Round off the B matrix elements upto 3 digits
D1 = np.around(D,decimals = 3) # Round off the D matrix elements upto 3 digits

# Display A,B,D matrix
print(f"\n---------------------\nThe Matrix A (N/mm): \n---------------------\n{A1}")
print(f"\n-------------------\nThe Matrix B (N): \n-------------------\n{B1} ")
print(f"\n---------------------\nThe Matrix D (N-mm): \n---------------------\n{D1}")

mat1 = np.concatenate([A,B])             # Merging of A and B matrix
mat2 = np.concatenate([B,D])             # Merging of B and D matrix
mat = np.concatenate((mat1,mat2),axis=1) # Final Merging of 1st and 2nd matrix vertically
matt = np.around(mat,decimals = 2)       # Round off the Element of ABD matrix upto digits
print("\n\n-------------\nABD matrix = \n-------------\n",matt)          # Display ABD matrix




#--------------------------------------------Margin of Safety Part--------------------------------------------------------------

Nx = float(ip_data[28][1])               # Taking Nx input
Ny = float(ip_data[29][1])               # Taking Ny input
Nxy = float(ip_data[30][1])              # Taking Nxy input
Mx = float(ip_data[31][1])               # Taking Mx input
My = float(ip_data[32][1])               # Taking My input
Mxy = float(ip_data[33][1])              # Taking Mxy input
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
    

XT = float(ip_data[36][1]) # Taking Tensile Strength Input in X direction
XC = float(ip_data[38][1]) # Taking Compressive Strength Input in X direction
YT = float(ip_data[37][1]) # Taking Tensile Strength Input in Y direction
YC = float(ip_data[39][1]) # Taking Compressive Strength Input in Y direction
S = float(ip_data[40][1])  # Taking Shear Strength Input where S12=S23 assumption is followed
sigma33 = 0                # sigma33 = 0 Since plane stress assumption is taken.

tenslistM = []             # Creating a blank list for sorting purpose
complistM = []             # Creating a blank list for sorting purpose
tenslistF = []             # Creating a blank list for sorting purpose
complistF = []             # Creating a blank list for sorting purpose
R_listTF = []              # Creating a blank list for sorting purpose
R_listTM = []              # Creating a blank list for sorting purpose
R_listCF = []              # Creating a blank list for sorting purpose
R_listCM = []              # Creating a blank list for sorting purpose
print("\n\nHashin Failure Criteria:\n")
print("---------------------------------------------------------------------")
print("Laminate         Matrix                           Fibre")
print("---------------------------------------------------------------------")
print("           Tensile     Compressive         Tensile     Compressive")
print("---------------------------------------------------------------------")

def hashin(XT,XC,YT,YC,S):                 # Function defination for checking using Hashin Failure Criteria
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
            if (cond <1):       # if condition for safe criteria
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
                
hashin(XT,XC,YT,YC,S)           # Calling a function to validate Hashin failure criteria
               
for i in range(len(sigklist)):
    print(str(i+1).ljust(11)+tenslistM[i].ljust(12)+complistM[i].ljust(20)+tenslistF[i].ljust(12)+complistF[i])
print("---------------------------------------------------------------------")
#print("\n",R_listTM)
#print("\n",R_listCM)
#print("\n",R_listTF)
#print("\n",R_listCF)

rmin1 = [] # Creating a list for sorting purpose
rmin2 = [] # Creating a list for sorting purpose
rmin3 = [] # Creating a list for sorting purpose
rmin4 = [] # Creating a list for sorting purpose
Rmin1 = 0  # Initializing a variable
Rmin2 = 0  # Initializing a variable
Rmin3 = 0  # Initializing a variable
Rmin4 = 0  # Initializing a variable
Rfinal=np.zeros((1,8))   # Creating a one dimentional array
MF=[0,0,0,0,0,0,0,0]     # Null list
for i in range(8):       # For loop to extract suitable margin of safety value from Hashin failure criteria
    if (str(R_listTM[i]) == '-'):  # Sorting condition if found null element
        Rmin1 = 0
    if (str(R_listTM[i])!= '-' ):  # Sorting condition for finite value
        Rmin1 = R_listTM[i][0]
        for j in range(2):
            if(0< R_listTM[i][j]<=Rmin1):
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
    
    if (str(R_listTF[i]) == "-"):  # Sorting condition if found null element
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
    lst=[Rmin1,Rmin2,Rmin3,Rmin4]  # Bunch of four possible values of margin of safety
    
    val=Rmin1                      # Initial assignment of value in varible val
    g=0
    for k in lst:                  # for loop to determine type of failure mode
        g=g+1
        if(k!=0):
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

print("\n\nMargin of Safety Chart:\n")
print("---------------------------------------------------------------------------------------------------------------")
print("Laminate".ljust(18)+"\u03C31 (MPa)".ljust(18)+"\u03C32 (MPa)".ljust(18)+"\u03C312 (MPa)".ljust(14)+"R-intact".ljust(17)+"Critical Mode")
print("---------------------------------------------------------------------------------------------------------------")
for i in range(len(sigklist)):  # For loop to create margin of safety chart
    print(f"{str(float(ip_data[i+17][1])).ljust(18)}"+f"{str(sigklist[i][0,0]).ljust(18)}"+f"{str(sigklist[i][1,0]).ljust(19)}"+f"{str(sigklist[i][2,0]).ljust(15)+str(Rfinal1[0][i]).ljust(16)}"+MF[i])
    
print("---------------------------------------------------------------------------------------------------------------")

mini = np.amin(min(Rfinal1))    # To find an minimum value of margin of safety
result = np.where(Rfinal1 == np.amin(mini)) # to find an angle of ply for minimum margin of safety
print(f"\n\nThe first ply failure occur at laminate with angle {str(float(ip_data[result[1][1]+17][1]))} with margin of safety R = {mini}")



#*************************************************************************************************************************************************** User Can Directly Extract the Required Output in External Output file using Code Below*********************
          
opfile = open("Composite_Properties_Output_File.txt",'w')  # To create an output file 

opfile.write("-------------------------------------------------------------------------------------------------------------------------\n")
opfile.write("                                         Composite Properties with Ply Failure Analysis\n")
opfile.write("-------------------------------------------------------------------------------------------------------------------------\n\n")
opfile.write(f"\nEffective Properties of composite are:\n-------------------------------------\nLongitudinal Stiffness E1 = {E1C:0.2f} GPa\nTransverse Stiffness E2 = {E2C:0.2f} GPa\nShear Modulous G12 = {G12C:0.2f} GPa\nPoisson's ratio nu12 = {nu12C:0.3f}\n")

opfile.write(f"\nThe Matrix A (N/mm): \n--------------------\n{A1}\n")
opfile.write(f"\nThe Matrix B (N): \n--------------------\n{B1}\n")
opfile.write(f"\nThe Matrix D (N-mm): \n--------------------\n{D1}\n")
opfile.write(f"\nABD Matrix is: \n--------------\n{matt}\n")


opfile.write("\nHashin Failure Criteria:\n")
opfile.write("---------------------------------------------------------------------\n")
opfile.write("Laminate         Matrix                           Fibre\n")
opfile.write("---------------------------------------------------------------------\n")
opfile.write("           Tensile     Compressive         Tensile     Compressive\n")
opfile.write("---------------------------------------------------------------------\n")

for i in range(len(sigklist)):
    opfile.write(str(i+1).ljust(11)+tenslistM[i].ljust(12)+complistM[i].ljust(20)+tenslistF[i].ljust(12)+complistF[i])
    opfile.write("\n")
                         
opfile.write("---------------------------------------------------------------------\n\n")
opfile.write("\nMargin of Safety Chart:\n")
opfile.write("---------------------------------------------------------------------------------------------------------------\n")
opfile.write("Laminate Angle".ljust(18)+"sigma 1 (MPa)".ljust(15)+"sigma 2 (MPa)".ljust(22)+"sigma12 (MPa)".ljust(14)+"R-intact".ljust(17)+"Critical Mode\n")
opfile.write("---------------------------------------------------------------------------------------------------------------\n")
for i in range(len(sigklist)):
    opfile.write(f"{str(float(ip_data[i+17][1])).ljust(18)}"+f"{str(sigklist[i][0,0]).ljust(18)}"+f"{str(sigklist[i][1,0]).ljust(19)}"+f"{str(sigklist[i][2,0]).ljust(15)+str(Rfinal1[0][i]).ljust(16)}"+MF[i])
    opfile.write("\n")
    
opfile.write("---------------------------------------------------------------------------------------------------------------\n\n")
opfile.write(f"The first ply failure occur at laminate with angle {str(float(ip_data[result[1][1]+17][1]))} with margin of safety R = {mini}")

                 
opfile.close()         # To close the output file

#User is free to refer the properties obtained in the output text file
               
               
               
    