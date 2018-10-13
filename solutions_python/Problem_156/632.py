fin = open("in", "r")
fout = open("out", "w")
t = int(fin.readline())
for tt in xrange(t):
    n = int(fin.readline())
    a = map(int, fin.readline().split(' '))
    ans = 1000
    for cnt in xrange(1, 1001):
        special = 0
        for x in a:
            if x > cnt:
                excess = x - cnt
                special += excess / cnt + (excess % cnt > 0)

        ans = min(ans, special + cnt)

    fout.write("Case #%d: %d\n" % (tt + 1, ans))
