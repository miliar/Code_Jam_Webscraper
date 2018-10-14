
import math



f2 = open('output.txt', 'w')

f1 = open('A-large (3).in', 'r')

t= int(f1.readline())
for i in range(t):
    s=f1.readline().split()
    n=int(s[0])
    p=int(s[1])
    arr=[0]*p
    s=f1.readline().split()
    for j in range(n):
        arr[int(s[j])% p] = arr[int(s[j])% p] + 1
    res=0
    if p==2:
        res=n-arr[1]//2
    if p==3:
        x=min(arr[1],arr[2])
        y=max(arr[1],arr[2])-x
        res=n- x- (2*y)//3
    if p==4:
        x=min(arr[1],arr[3])
        y=max(arr[1],arr[3])-x
        res=n-x-arr[2]//2-(3*y+2*(arr[2]%2))//4
    
    f2.write("Case #" +str(i+1) +": "+str(res) + "\n")
f2.close()
        

