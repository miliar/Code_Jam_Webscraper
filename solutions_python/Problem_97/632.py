import sys
f = open(sys.argv[1])
n = int(f.readline())

for case in range(n):
    a,b = map(int, f.readline().strip().split())
    t = 0

    astr = str(a)
    for m in range(a, b+1):
        mstr = str(m)
        seen = set()
        for i in range(1, len(mstr)):
            if mstr[i]=="0": continue
            nstr = mstr[i:]+mstr[:i]
            if nstr >= mstr: continue
            if nstr < astr: continue
            if nstr in seen: continue
            seen.add(nstr)
            t += 1
    print "Case #%d: %d" % (case+1, t)
