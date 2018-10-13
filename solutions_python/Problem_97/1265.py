


def transform(i, lo, hi):
    q = str(i)
    n = q
    for c in q:
        n = n[-1:] + n[:-1]
        m = int(n)
        l = min(m,i)
        h = max(m,i)
        if len(str(m)) != len(q) or m == i or l<lo or h>hi:
            continue
        s.add((l,h))
        


f = open("C-small-attempt0.in")
o = open("out3.txt", "w")
T = int(f.readline())

for t in range(T):
    s = set()

    q = [int(a) for a in f.readline().split()]
    if not q[0]/10:
        o.write("Case #%d: 0\n" % (t+1))
        continue
    for i in xrange(q[0], q[1]+1):
        transform(i, q[0], q[1])
    o.write("Case #%d: %d\n" % (t+1, len(s)))

o.close()
