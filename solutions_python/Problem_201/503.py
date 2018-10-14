import math

n = 100


f = open("input1.in")
n = int(f.readline())
for m in range(n):
    ll = f.readline().strip().split()
    n = int(ll[0])
    k = int(ll[1])

    n1 = [1, n]
    n2 = [0, 0]
    pc = 0
    c = 1
    ans = n
    while True and k != 1:
        l = int((n1[1] - 1)/2)
        r = n1[1] - 1 - l   # r >= l
        if l != r:
            n1 = [n1[0], r]
            n2 = [n1[0]+2*n2[0], l]
        else:   # l = r
            zl = int((n2[1] - 1)/2)
            zr = n2[1] - 1 - zl
            n1 = [n1[0]*2 + n2[0], r]
            n2 = [n2[0], zl]
        pc = c
        c += n1[0] + n2[0]
        if c >= k:
            if pc + n1[0] >= k:
                ans = n1[1]
            else:
                ans = n2[1]
            break
    mm =  int((ans - 1)/2)
    print("Case #%d: %d %d" % (m+1, ans - mm - 1, mm))