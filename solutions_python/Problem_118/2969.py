import math
def isInteger(n):
    if n%2 == 0 or (n+1)%2 == 0:
    #if n%1==0:
        return True
    return False
def check(n):
        k=str(n)
        l=k[::-1]
        if k==l:
                m=math.sqrt(n)
                if isInteger(m):
                        o=str(int(m))
                        p=o[::-1]
                        if o==p:
                                return True
        return False
f1=open("C-small-attempt0.in","r")
f2=open("Output","w")
s=f1.readline()
t=int(s)
u=1
while t:
        count=0
        s=f1.readline()
        a=s.split(" ")
        low=int(a[0])
        high=int(a[1][:-1])
        for i in range(low,high+1):
                if check(i):
                        count=count+1
        f2.write("Case #"+str(u)+": "+str(count)+"\n")
        t=t-1
        u=u+1
f1.close()
f2.close()
