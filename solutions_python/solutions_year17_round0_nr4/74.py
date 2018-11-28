from sys import stdin

for cn in xrange(1,1+int(stdin.readline())):
    (n,m) = tuple(int(z) for z in stdin.readline().split())
    rows = {}
    cols = {}
    sums = {}
    diffs = {}
    models = {}
    newModelArmy = []
    for k in xrange(m):
        (i,r,c) = stdin.readline().split()
        (r,c) = (int(r),int(c))
        if i != '+':
            rows[r] = 1
            cols[c] = 1
        if i != 'x':
            sums[r+c] = 1
            diffs[r-c] = 1
        models[(r,c)] = i
    for p in xrange(1,n+1):
        for sq in [(p,q) for q in xrange(p,n+1)]+[(q,p) for q in xrange(p+1,n+1)]:
            addTimes = False
            addPlus = False
            if (sq[0] not in rows) and (sq[1] not in cols):
                addTimes = True
                rows[sq[0]] = 1
                cols[sq[1]] = 1
            if (sq[0]+sq[1] not in sums) and (sq[0]-sq[1] not in diffs):
                addPlus = True
                sums[sq[0]+sq[1]] = 1
                diffs[sq[0]-sq[1]] = 1
            if (addTimes and addPlus) or ((addTimes or addPlus) and sq in models):
                newModelArmy.append(('o',sq[0],sq[1]))
            elif addTimes:
                newModelArmy.append(('x',sq[0],sq[1]))
            elif addPlus:
                newModelArmy.append(('+',sq[0],sq[1]))
    sc = len(rows)+len(sums)
    print "Case #{}: {} {}".format(cn, sc, len(newModelArmy))
    for newModel in newModelArmy:
        print "{} {} {}".format(*newModel)
