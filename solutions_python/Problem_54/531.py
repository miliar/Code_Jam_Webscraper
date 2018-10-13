import fractions
import sys
fid = open(sys.argv[1])
C = int(fid.next().strip())
for i, l in enumerate(fid):
    v = map(long, l.strip().split())
    t = list(set(v[1:]))
    t.sort()
    hdr = 'Case #'+str(i+1)+': '
    if len(t) == 1:
        print hdr+str(0)
    elif len(t) == 2:
        T = (t[-1]-t[0])
        addv = T - (t[-1] % T)
        if addv == T: addv = 0
        print hdr + str(addv)
    else:
        diff1 = [t1-t[0] for t1 in t[1:]]
        diff2 = [fractions.gcd(d1, diff1[0]) for d1 in diff1[1:]]
        T = min(diff2)
        addv = T - (t[-1] % T)
        if addv == T: addv = 0
        print hdr + str(addv)
