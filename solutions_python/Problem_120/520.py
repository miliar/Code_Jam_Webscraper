import math
a=open("A-large.in")
b=open("out22.txt","w")
T=int(a.readline())
for i in range(T):
    line=a.readline()
    e=line.find(" ")
    r=int(line[:e])
    t=int(line[e+1:])
    #utilizamos sumatoria, buscamos val:
    n=int(math.sqrt(t))
    if 2*r*n-n+2*n*n<t:
        n=t
    num=15
    while num>1:
        while True:
            area=2*r*n-n+2*n*n
            if area>t and n>0:
                n=n-10**num
            else:
                break
        n=n+10**num
        num=num-1
    while True:
        area=2*r*n-n+2*n*n
        if area>t:
            n=n-1
        else:
            break
    b.write("Case #"+str(i+1)+": "+str(n)+"\n")
a.close()
b.close()
