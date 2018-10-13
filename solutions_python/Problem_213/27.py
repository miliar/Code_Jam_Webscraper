
import math



f2 = open('output.txt', 'w')

f1 = open('B-large (3).in', 'r')

t= int(f1.readline())
for i in range(t):
    s=f1.readline().split()
    n=int(s[0])
    c=int(s[1])
    m=int(s[2])
    arr=[]
    arrc=[0]*c
    arrb=[0]*n
    for j in range(m):
        s=f1.readline().split()
        arr.append([int(s[0])-1,int(s[1])-1])
    for j in range(m):
        arrc[arr[j][1]]=arrc[arr[j][1]]+1
        arrb[arr[j][0]]=arrb[arr[j][0]]+1
    res=0
    su=0
    for j in range(n):
        su=su+arrb[j]
        if math.ceil(su/(j+1)) >res:
            res= math.ceil(su/(j+1))
    if max(arrc) > res:
        res =max(arrc)
    res2=0
    for j in range(n):
        if arrb[j]>res:
            res2=res2+arrb[j]-res
    
    f2.write("Case #" +str(i+1) +": "+str(res)+" " + str(res2) + "\n")
f2.close()
        

