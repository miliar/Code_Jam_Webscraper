C = int(raw_input())

for x in range(1, C+1):

    nl = raw_input().split()
    
    N = int(nl[0])

    t = []
    for i in range(1, N+1):
        t += [ int(nl[i]) ]
    t.sort()

    d = []
    for i in range(0, N-1):
        for j in range(i+1, N):
            d += [ t[j] - t[i] ]

    T = d[0]
    for i in range(1, len(d)):
        dividend = T
        divisor = d[i]
        while divisor != 0:
            remainder = dividend % divisor
            dividend = divisor
            divisor = remainder
        T = dividend

    if t[0] % T == 0:
        y = 0
    else:
        y = T - (t[0] % T)
    
    print "Case #" + str(x) + ": " + str(y)
