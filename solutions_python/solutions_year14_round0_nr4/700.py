def r():
    return map(float, raw_input().split())
def solve():
    n = input()
    a = r()
    b = r()
    a.sort()
    b.sort()
    al, bl = 0, 0
    ar, br = len(a) - 1, len(b) - 1
    res1 = 0
    while al <= ar:
        if a[al] < b[bl]:
            br -= 1
        else:
            res1 += 1
            bl += 1
        al += 1
    res2 = n
    i, j = 0, 0
    while i < len(a) and j < len(b):
        while b[j] < a[i] and j < len(b):
            j += 1
            if j >= len(b):
                break
        if j != len(b):
            if b[j] > a[i]:
                res2 -= 1
        i += 1
        j += 1
    return res1, res2
    
T=input()
for t in xrange(T):
    r1, r2 = solve()
    print "Case #" + str(t+1) + ": " + str(r1) + " " + str(r2)

