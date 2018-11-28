from __future__ import division

lines = open('input.txt').read().splitlines()
test = int(lines[0].strip())
out = open('output.txt', 'w')

lno = 0
for t in range(test):
    lno += 1
    d, n = map(int, lines[lno].strip().split())
    hs = []
    for i in range(n):
        lno += 1
        k, s = map(int, lines[lno].strip().split())
        hs.append((k,s))
    tmax = (d - hs[-1][0])/hs[-1][1]
    for h in hs:
        nt = (d-h[0])/h[1]
        if tmax<nt:
            tmax = nt
    case = "Case #%d: %.6f" %(t+1, d/tmax)
    print case
    out.write(case+'\n')

out.close()

