import math

pi = math.pi

for t in range(int(raw_input())):

    n, k = map(int,raw_input().strip().split())

    a = [0 for i in range(n)]

    for i in range(n):
        r, h = map(int,raw_input().strip().split())
        curve = 2 * r * h
        flat = r * r
        a[i] = (curve, flat)


    a = sorted(a, key = lambda i:i[0], reverse=True)

    #print a

    m = 0
    base = 0
    for i in range(k):
        if a[i][1] > m:
            m = a[i][1]
            base = i

#    print 'b', base


    short = k-1
    for i in range(k, n):
        if a[i][1] > a[base][1]:
            extra = a[i][0] + a[i][1]
            if extra - (a[short][0] + a[base][1]) > 0:
                base = i
                short = i

    ans = 0
    for i in range(k-1):
        ans += a[i][0]

    ans = ans + a[short][0] + a[base][1]

    ans *= pi


    print 'Case #{}: {}'.format(t+1, ans)