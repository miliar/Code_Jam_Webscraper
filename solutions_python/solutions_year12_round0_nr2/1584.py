inf = open("b.in", "r")
ouf = open("b.out", "w")
T = int(inf.readline())
for t in range(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    a = [int(i) for i in inf.readline().split()]
    n = a[0]
    s = a[1]
    p = a[2]
    a = a[3:]
    ans = 0
    for x in a:
        k = x / 3
        r = x % 3
        if r != 0:
            k += 1
        if k >= p:
            ans += 1
        elif (k == p - 1) & (r != 1) & (s > 0) & (x > 1) & (x < 29):
             ans += 1
             s -= 1
    print >> ouf, ans
inf.close()
ouf.close()    

