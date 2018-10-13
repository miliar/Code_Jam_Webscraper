#!/usr/bin/python2.7

fichier = open("test","r")
fresult = open("result","w")

print ("COMPUTATION LAUNCHED")
T=0
i=1

for line in fichier:
    if T==0:
        T=int(line.strip('\n'))
    else:
        S=line.split(' ')[0]
        K=int(line.split(' ')[1].strip('\n'))
        L=[]
        for c in S:
            L.append(c)
        res=0
        for n in range(0,len(L)-K+1):
            if L[n]=='-':
                for m in range(0,K):
                    if L[n+m]=='-':
                        L[n+m]='+'
                    else:
                        L[n+m]='-'
                res+=1
        L=L[::-1]
        for n in range(0,len(L)-K+1):
            if L[n]=='-':
                for m in range(0,K):
                    if L[n+m]=='-':
                        L[n+m]='+'
                    else:
                        L[n+m]='-'
                res+=1
        if L.count('-')==0:
            res=str(res)
        else:
            res="IMPOSSIBLE"
        fresult.write("Case #"+str(i)+": "+res+"\n")
        i+=1

fichier.close()
fresult.close()
