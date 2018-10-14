import numpy as np
import matplotlib.pyplot as plt
import random

infile = open('A-small-attempt2.in', 'r')
outfile = open('outpu.txt', 'w')
lineas = infile.readlines()
x = 1
y = (x + 1) + 4
r = 0
for i in range(int(lineas[0])):
    num1 = int(lineas[x])
    num2 = int(lineas[y])
    l_x1 = map(int, lineas[num1+x].split(' '))
    l_x2 = map(int, lineas[num2+y].split(' '))
    cont = 0
    rslt = 0
    for i in range(4):
        for j in range(4):
            if l_x1[i] == l_x2[j]:
                cont = cont + 1
                rslt = l_x1[i]
            
    r = r + 1
    outfile.write("Case #")
    outfile.write(str(r))
    outfile.write(": ")
    if cont == 1:
        outfile.write(str(rslt))
    elif cont > 1:
        outfile.write("Bad magician!")
    else:
        outfile.write("Volunteer cheated!")
    outfile.write("\n")
    x = y+5
    y = (x+1) + 4


infile.close()
outfile.close()
