def fair(num):
    if len(num) == 0:
        return False
    elif len(num) == 1:
        return True
    elif num[0] == num[len(num)-1]:
        return fair(num[1::len(num)-1])

def square(highlow):
    
    highsqr = int(sqrt(highlow[1]))
    lowsqr = int(sqrt(highlow[0]))
    if lowsqr*lowsqr < highlow[0]: lowsqr+=1

    sqrs = []
    
    for x in range(lowsqr,highsqr+1):
        sqrs.append(x*x)
   
    fairs = 0
    
    for x in sqrs:
        if fair(str(x)) and fair(str(int(sqrt(x)))): fairs +=1
       
    return(fairs)    
    
from math import sqrt

filename = input("Filename: ")
filein = open(filename, "r")
filename = filename.strip(".in") +".out"
fileout = open(filename,"w")
results = []

T = int(filein.readline().strip())

for idx in range(0,T):
    bounds = filein.readline().strip().split(" ")
    bounds[0] = int(bounds[0])
    bounds[1] = int(bounds[1])
    
    fileout.write("Case #" + str(idx+1) + ": " + str(square(bounds)) +"\n")

filein.close()
fileout.close()