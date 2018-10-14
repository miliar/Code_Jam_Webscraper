def mintime():
    global C,X
    M=0.0
    S=2.0
    t=0.0
    while M<X:
        if X<=C:
           t=t+(X-M)/S
           M=X
        if M<C:
            t=t+(C-M)/S
            M=C
        if M>=C: 
            if (X+C-M)/(S+F) < (X-M)/S:
                M=M-C
                S=S+F
            else:
                t=t+(X-M)/S
                M=X
    return t
T=int(input())
for i in range(1,T+1):
    tmp=input().split()
    (C,F,X)=list(map(float,tmp))
    t=mintime()
    print("Case #",i,": ",t,sep="")
