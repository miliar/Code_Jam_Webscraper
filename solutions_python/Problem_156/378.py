fin = open("input.txt", "r")
fout = open("output.txt", "w")

T = int(fin.readline())

for _ in xrange(T):
    n = int(fin.readline())
    p = map(int, fin.readline().split())
    mx = max(p)
    res = mx
    for i in xrange(1, mx):
        ans = i
        for x in p:
            if i < x:
                ans += (x - 1) / i
            #print "debug", i, (x - 1) / i
        res = min(res, ans)
    print >> fout, "Case #%d: %d" % (_ + 1, res)

fin.close()
fout.close()
