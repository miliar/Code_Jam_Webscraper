t, T = 0, int(input())
while t != T:
    t += 1

    C, F, X = tuple(map(float, input().split()))
    d, f = 0, 2

    while C/f + X/(f+F) < X/f:
        d += C/f
        f += F
    d += X/f 

    print('Case #%d:' % t, d)
    
