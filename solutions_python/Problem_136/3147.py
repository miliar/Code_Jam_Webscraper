def sol():
    C, F, X = map(float, input().split())
    
    tans = float('+inf')
    tc = 0
    cs = 2
    for i in range(int(X)+2):
        if (tc + (X / cs)) < tans:
            tans = tc + (X / cs)
        tc += C / cs
        cs += F
    return tans

tst = int(input())

for i in range(tst):
    print("Case #%d: %.8f" % ( i+1, sol()))
