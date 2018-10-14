'''Apr 14, 2012 Autor: Artur'''
# -*- coding: utf-8 -*-

from collections import deque
file_in = open("C-small-attempt1.in", "r")
file_out = open("C-small-attempt1.out", "w")
katse=[]
def dq_arvuks(dq):
    arv = ""
    if dq[0]=="0":
        return(0)
    for i in range (dq.__len__()):
        arv+=dq[i]
    return int(arv)

def recycled(min, märgid, max):
    katse2=[]
    vastus=0
    arv = dq_arvuks(märgid)
    katse.append(arv)
    for i in range (märgid.__len__()):
        märgid.append(märgid.popleft())
        arv2 = dq_arvuks(märgid)
        if arv2 >= min and arv2 <= max and (arv, arv2) not in katse2 and arv2 not in katse and arv < arv2:
            katse2.append((arv, arv2))
            vastus+=1
    return(vastus)

for case, rida in enumerate(file_in):
    if case == 0:
        mitu = int(rida)
    else:
        vastus = 0
        katse=[]
        file_out.write("Case #" + str(case) + ": ")
        tükid = rida.strip().split(" ")
        miinimum = int(tükid[0])
        maksimum = int(tükid[1])
        for i in range (miinimum, maksimum):
            märgid = deque([])
            for märk in str(i):
               märgid.append(märk)
            vastus += recycled(miinimum, märgid, maksimum)
        if case != mitu:
            file_out.write(str(vastus) + "\n")
        else:
            file_out.write(str(vastus))
