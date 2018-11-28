#https://code.google.com/codejam/contest/2270488/dashboard#s=p1
import os

def lireinput():
    finput=open("input.txt","r")
    nbrcase=int(finput.readline())
    cases=[]
    for i in range(nbrcase):
        caspresent=[]
        taille=finput.readline()
        hauteur,largeur=int(taille.split(" ")[0]),int(taille.split(" ")[1])
        for j in range(hauteur):
            ligne=finput.readline()
            ligne=ligne.split(" ")
            for k in range(largeur):
                ligne[k]=int(ligne[k])
            caspresent.append(ligne)
        cases.append(caspresent)
    return (cases)

def resoudre1case(case):
    lrg=len(case[0])
    ht=len(case)
    
    for y in range(ht):
        for x in range(lrg):
            nbr=case[y][x]
            smlrg=0
            smht=0
            for i in range(lrg):
                smlrg+=case[y][i]
            for j in range(ht):
                smht+=case[j][x]
            if (smht <= nbr*ht or smlrg<= nbr*lrg):
                pass
            else :
                return ("NO")
    return ("YES")

def ecrireoutput(cases):
    fout=open("output.txt","w")
    for i in range(len(cases)):
        fout.write("Case #"+str(i+1)+": "+cases[i]+"\n")

cases=lireinput()
sol=[]
for i in range(len(cases)):
    sol.append(resoudre1case(cases[i]))
ecrireoutput(sol)
    
                
    
