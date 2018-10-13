import sys

f=open(sys.argv[1])
T=int(f.readline())

case=1
while case<T+1:
    l=f.readline().split()
    C=float(l[0])
    F=float(l[1])
    X=float(l[2])

    rate=2.0
    ans=0.0

    while True:
        #print "%f+%f<%f"%(C/rate,X/(rate+F),X/rate)
        if C/rate+X/(rate+F)<X/rate:
            ans+=C/rate
            rate+=F
            #print "rate=%f,ans=%f"%(rate,ans)
        else:
            ans+=X/rate
            break

    print "Case #"+str(case)+": %.7f"%ans
    case+=1



