T = int(input())

for t in range(1,T+1):
    C,F,X = [float(i) for i in input().split()]
    
    res = 0.0
    r = 2.0

    while(X/r > (C/r)+(X/(r+F))):
        res += C/r
        r += F
    res += X/r
    print("Case #"+str(t)+": "+str(round(res,7)))
    

