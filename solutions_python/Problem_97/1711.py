'''
Created on 14 avr. 2012

@author: SsqualL
'''
f=open('C-small-attempt0.in','r')
f.readline()
r=f.readline()
res=open('output2.txt',"w")

compt=1
egalite=0
s=""
while r!="":
    L=r.split()
    nbinf=int(L[0])
    nbsup=int(L[1])
    Nombre=[]
    L=[]
    for i in range(nbinf,nbsup+1):
        Nombre.append(i)
    for k in range(0,len(Nombre)):
        a=str(Nombre[k])
        for j in range(1,len(a)):
            for i in range(0,len(a)):
                s=s+a[(i+j)%len(a)]
            if s[0]!=0 and int(s)>=nbinf and int(s)<=nbsup and ((Nombre[k],int(s))in L )== False and ((int(s),Nombre[k])in L )== False and int(s)!=Nombre[k]:
                L.append((Nombre[k],int(s)))
            s=""

    S="Case #"+str(compt)+": "+str(len(L))+"\n"
    res.write(S)
    r=f.readline()
    compt=compt+1