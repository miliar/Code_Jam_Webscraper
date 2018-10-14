t = input()
use = '1023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, t+1):
    line = raw_input()
    chmap = {}
    out = ''
    next = 0
    for c in line:
        if c not in chmap:
            chmap[c] = use[next]
            next += 1
        out += chmap[c]
    print "Case #%s: %s" % (i, int(out, max(2, next)))

