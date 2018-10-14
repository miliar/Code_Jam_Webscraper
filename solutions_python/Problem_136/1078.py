
def solve(test):
    c, f, x = raw_input().split()
    c = float(c)
    f = float(f)
    x = float(x)
    r = 2
    t = x / r

    tcum = 0.0

    while 1:

        tnext = c / r
        tot = x / (f + r)
        #print t, tot, tnext

        if t > (tot + tnext):
            t = tot
            tcum += tnext
            r += f
        else:
            break

    print "Case #%d: %.7f" % ( test, round(t + tcum, 7))


t = int(raw_input())
for i in xrange(t):
    solve(i + 1)
