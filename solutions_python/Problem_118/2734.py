import os
from math import sqrt
from os import chdir
chdir(".")
def lirein():
    fin=open('input.txt',"r")
    nbrcases=int(fin.readline())
    cases=[]
    for i in range(nbrcases):
        caspresent=fin.readline().split(" ")
        for k in [0,1]:
            caspresent[k]=int(caspresent[k])
        cases.append(caspresent)
    return (cases)

def sol1case(case):
    binf,bsup=sqrt(case[0]),sqrt(case[1])
    binf,bsup=int(round(binf+0.49)),int(bsup)+1
    somme=0
    for i in range(binf,bsup):
        nbr=str(i)
        for j in range(len(nbr)//2):
            if nbr[j] != nbr[(len(nbr)-1)-j]:
                break
        else:
            nbr2=str(int(nbr)*int(nbr))
            for k in range(len(nbr2)//2):
                if nbr2[k] != nbr2[(len(nbr2)-1)-k]:
                    break
            else:
                somme +=1
    return (somme)

def ecrireout(sol):
    fout=open('output.txt','w')
    for i in range(len(sol)):
        fout.write("Case #"+str(i+1)+": "+str(sol[i])+"\n")

cases=lirein()
sol=[]
for i in range(len(cases)):
    sol.append(sol1case(cases[i]))
ecrireout(sol)
        
    
