# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 21:20:51 2017

@author: Bredock
"""
def findChange(num):
    cambio = -1
    for i in range(0, len(num)-1):
        if (num[i] > num[i+1]):
            cambio = i
            continue
    return cambio

file = "G:\Programming\Google Jam\B-large.in"
file_out = "G:\Programming\Google Jam\B-small-attempt0.out"
f = open(file)
g = open(file_out, "w")
f.readline()

line = f.readlines()
num_case = 0
for l in line:
    num_case+=1
    num = l.rstrip()
    num_int = int(num)
    if (len(num) > 1):
        cambio = findChange(num)
    else:
        cambio = -1
    while (cambio >= 0):
        if (int(num) <= 9):
            num_fin = num
        elif (cambio == 0):
            if (int(num[cambio])-1 == 0):
                char_ini = ""
            else:
                char_ini = str(int(num[cambio])-1)
            num_fin = char_ini + '9'*(len(num[cambio+1:]))
        else:
            num_fin = num[:cambio] + str(int(num[cambio])-1) + '9'*(len(num[cambio+1:]))
            
        cambio = findChange(num_fin)
        num = num_fin
    g.write("Case #"+str(num_case)+": "+str(num)+"\n")
 
g.close()