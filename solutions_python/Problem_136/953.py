tc=int(input("TC"))
a=[]
for t in range(tc):
    cfx=input()
    cfx=[float(i) for i in cfx.split(" ")]
    c=cfx[0]
    f=cfx[1]
    x=cfx[2]
    t1=x/2
    to=0
    n=0
    t2=(c/(2+n*f))+(x/(2+(n+1)*f))
    while (t1>t2):
        to+=(c/(2+n*f))
        n+=1
        t1=t2
        t2=to+(c/(2+n*f))+(x/(2+(n+1)*f))
    to+=x/(2+n*f)
    a+=[str(to)]
for i in range(len(a)):
    print("Case #"+str(i+1)+": "+a[i])
