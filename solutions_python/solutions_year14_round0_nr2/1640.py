import math
def solve(c,f,x):
    farmsGrabbed=-1
    bestTime=10000000000000000
    while True:
        time=0
        farmsGrabbed+=1
        curFarms=farmsGrabbed
        curF=2
        curC=0
        while curFarms:
            curFarms-=1
            time+=(c-curC)/curF
            curC=0
            curF+=f
        time+=(x-curC)/curF
        if time>bestTime:
            return str(bestTime)
        bestTime=time
        
    

X=open("b.in")
z=open("output.txt","w")
case=0
cases=int(X.readline())
line=X.readline().split()
while case<cases:
    case+=1
    print case


    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    z.write("Case #"+str(case)+": "+solve(c,f,x)+"\n")
    line=X.readline().split()
z.close()
