inf = open("c.in", "r")
ouf = open("c.out", "w")
T = int(inf.readline())
for t in range(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    n = inf.readline()
    a = [int(i) for i in inf.readline().split()]
    x = reduce(lambda x, y: x ^ y, a, 0)
    if x == 0:
        sum = reduce(lambda x, y: x + y, a, 0)
        m = min(a)
        print >> ouf, sum - m
    else:
        print >> ouf, "NO"
inf.close()
ouf.close()    

