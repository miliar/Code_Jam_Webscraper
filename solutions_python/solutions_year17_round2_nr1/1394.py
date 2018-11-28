T=int(input())
i=1
while i<=T:
    y=input()
    y=y.split()
    D=int(y[0])
    horses=int(y[1])
    j=0
    TIME=0
    while(j<horses):
        x=input()
        x=x.split()
        d=int(x[0])
        speed=int(x[1])
        d=D-d
        t=d/speed
        if t>TIME:
            TIME=t
        j+=1
    answer=D/TIME
    print("Case #"+str(i)+":",("%.6f" % answer))
    i+=1
