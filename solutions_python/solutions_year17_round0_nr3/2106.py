import sys

t=int(input().strip())
for i in range(t):
    x,y=input().strip().split(' ')
    n=int(x)
    stl=int(y)
    a=[]
    a.append(n)
    j=0
    while j<stl-1:
        a.sort()
        k=a[-1]
        a.pop()
        if k%2==0:
            a.append((k//2)-1)
        else:
            a.append(k//2)
        a.append(k//2)
        j=j+1
    a.sort()
    l=a[-1]
    if l%2==0:
         print("Case #"+str(i+1)+": "+str(l//2)+" "+str((l//2)-1))
    else:
        print("Case #"+str(i+1)+": "+str(l//2)+" "+str(l//2))
