from datetime import *

def sort(t):
    for passesLeft in range(len(t)-1, 0, -1):
        for index in range(passesLeft):
            if t[index] > t[index + 1]:
               t[index], t[index + 1] = t[index + 1], t[index]
    return t

f=open('B-large.in','r')
out=open('B-large.out','w')
lines=f.readlines()[:]
k=1
for j in range(int(lines[0][:-1])):
    
    T=int(lines[k][:-1])
    k+=1
    s=lines[k].find(' ')
    NA=int(lines[k][:s])
    NB=int(lines[k][s+1:-1])
    k+=1
    schedA=[]
    for i in range(NA):
        s=lines[k].find(' ')
        schedA.append([timedelta(hours=int(lines[k][:s][:2]),minutes=int(lines[k][:s][3:])),timedelta(hours=int(lines[k][s+1:-1][:2]),minutes=int(lines[k][s+1:-1][3:]))])
        k+=1
        
    schedB=[]
    for i in range(NB):
        s=lines[k].find(' ')
        schedB.append([timedelta(hours=int(lines[k][:s][:2]),minutes=int(lines[k][:s][3:])),timedelta(hours=int(lines[k][s+1:-1][:2]),minutes=int(lines[k][s+1:-1][3:]))])

        k+=1

   

    depA=[x[0] for x in schedA]
    depA=sort(depA)
    arrA=[x[1] for x in schedB]
    arrA=sort(arrA)
    
    depB=[x[0] for x in schedB]
    depB=sort(depB)
    arrB=[x[1] for x in schedA]
    arrB=sort(arrB)

    numA=0
    numB=0
   
    for t in depA:
        a=0
        if arrA:
            while t>=arrA[a]+timedelta(minutes=T):
                a+=1
                if a>=NB: break

        d=0
        while t>=depA[d]:
            d+=1
            if d>=NA: break

        if a+numA<=d-1: numA+=1

    for t in depB:
        a=0
        if arrB:
            while t>=arrB[a]+timedelta(minutes=T):
                a+=1
                if a>=NA: break

        d=0
        while t>=depB[d]:
            d+=1
            if d>=NB: break

        if a+numB<=d-1: numB+=1

    out.writelines('Case #'+str(j+1)+': '+str(numA)+' '+ str(numB)+'\n')


out.close()
f.close()

