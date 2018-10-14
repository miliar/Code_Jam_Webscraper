T=int(input())

for testCase in range(0,T):
    P = int(input())
    M = [int(a) for a in input().split()]
    prices = []
    for i in range(0, P):
        prices.append([int(a) for a in input().split()])

    s = 0
    for i in range(0, P):
        m = []
        for i in range(0, len(M), 2):
            j = min(M[i],M[i+1])
            j -= 1
            if j < 0:
                s += 1
            m.append(j)
        M = m
    
    print('Case #{0}: {1}'.format(testCase+1, s))
