import sys
f = open("B-large.in")
n = f.readline()
for (lineNum,line) in enumerate(f):
    ints = [int(i) for i in line.split()]
    S = ints[1]
    p = ints[2]
    lowerBound = 0 - sys.maxint
    y = 0
    spFn = [lambda x: (x + 3) / 3, lambda x:(x + 2) / 3, lambda x:(x + 4) / 3]
    nspFn = [lambda x:x / 3, lambda x:(x + 2) / 3, lambda x: (x + 1) / 3]
    for k in sorted(ints[3:]):
        if S > 0 and k > 1 and k % 3 != 1:
            if spFn[k % 3](k) >= p:
                y += 1
                S -= 1
        elif nspFn[k % 3](k) >= p:
            y += 1
    print "Case #%d: %d" % (lineNum+1,y)
