
import math



f2 = open('output.txt', 'w')

f1 = open('C-small-1-attempt0 (2).in', 'r')

t= int(f1.readline())
for i in range(t):
    s=f1.readline().split()
    n=int(s[0])
    k=int(s[1])
    u=float(f1.readline())
    s=f1.readline().split()
    arr=[]
    for j in range(n):
        arr.append(float(s[j]))
    arr=sorted(arr)
    arr=arr+[1]
    inc=0
    while u>0 and inc < n:
        if arr[inc] == arr[inc+1]:
            inc=inc+1
        else:
            ch=min(arr[inc+1]-arr[inc],u/(inc+1))
            arr[inc]=arr[inc]+ch
            u=u-(inc+1)*ch
    res=arr[inc]**(inc+1)
    for j in range(inc+1,n):
        res=res*arr[j]
    
        
    
    f2.write("Case #" +str(i+1) +": "+str(res) + "\n")
f2.close()
        

