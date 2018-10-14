inf = open("a_pre.in", "r")
ouf = open("a.out", "w")
m = {}
for t in xrange(4):
    a = inf.readline()
    b = inf.readline()
    for i in xrange(len(a)):
        ca = a[i]
        cb = b[i]
        m[ca] = cb
inf.close()

inf = open("a.in", "r")

T = int(inf.readline())
for t in range(T):
    print >> ouf, "Case #" + str(t + 1) + ": ",
    s = inf.readline()
    for i in xrange(len(s)):
        cs = s[i]
        if cs in m:
            ouf.write(m[cs])
        else:
            ouf.write(cs)
inf.close()
ouf.close()    

