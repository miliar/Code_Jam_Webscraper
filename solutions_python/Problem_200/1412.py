def solve(N):
    tn = [int(i) for i in list("%i"%N)]
    c = False
    for n in range(len(tn)-1):
        if tn[n]>tn[n+1] and not c:
            tn[n]=tn[n]-1
            c=True
        if c==True:
            tn[n+1]=9
    return int(''.join([str(i) for i in tn]))





T = int(input())
tn=[]
for t in range(T):
    N = int(input())
    #print(N)

    tidy=solve(N)
    while(tidy!= solve(tidy)):
       tidy = solve(tidy)
    print("Case #%i:"%(t+1), tidy)


