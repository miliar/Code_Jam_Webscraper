
import math



f2 = open('output.txt', 'w')

f1 = open('A-large (2).in', 'r')

t= int(f1.readline())
for i in range(t):
    s=f1.readline().split()
    n=int(s[0])
    k=int(s[1])
    arr=[]
    for j in range(n):
        s=f1.readline().split()
        arr.append([int(s[0])*int(s[1]),int(s[0])])
    arr2=sorted(arr,reverse=True)
    res=0
    for j in range(k):
        res=res+2*math.pi*arr2[j][0]
    maxr=0
    for j in range(k):
        if arr2[j][1]>maxr:
            maxr=arr2[j][1]
    res=res+maxr*maxr*math.pi
    last=maxr*maxr + 2*arr2[k-1][0]
    for j in range(k,n):
        if arr2[j][1]*arr2[j][1]+2*arr2[j][0] > last:
            last=arr2[j][1]*arr2[j][1]+2*arr2[j][0]
    res=res+math.pi*(last-maxr*maxr - 2*arr2[k-1][0])
        
    
    f2.write("Case #" +str(i+1) +": "+str(res) + "\n")
f2.close()
        

