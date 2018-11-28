def lr(n):
    if n % 2 == 1:
        return n / 2, n / 2
    else:
        return n / 2 , n / 2 -1

def solve(line):
    parts = line.split()
    k = int(parts[1])
    d = {}
    d[int(parts[0])] = 1
    while k > 0:
        kk = max(d.keys())
        vv = d.pop(kk)
        k -= vv
        if k <= 0:
            return "%d %d" % (lr(kk))
        l, r = lr(kk)
        d[l] = d.get(l, 0) + vv
        d[r] = d.get(r, 0) + vv

with open("c.in", "r") as fin:
    with open ("c.out", "w") as fout:
        t = int(fin.readline())
        for i in xrange(t):
            res = str(solve(fin.readline()))
            print i+1, res
            fout.write("Case #%d: %s\n" % (i+1, res))
