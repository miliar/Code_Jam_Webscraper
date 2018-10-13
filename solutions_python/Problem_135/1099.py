from collections import defaultdict

with open('magic_trick.in') as f:
    t = int(f.readline())
    for m in range(1,t+1):
        sets = []
        for n in range(2):
            chosen = int(f.readline()) - 1
            for k in range(4):
                row = f.readline()
                if k == chosen:
                    sets.append(set(row.rstrip().split(" ")))
        inters = reduce(set.intersection,sets)
        if not inters:
            print "Case #%d: Volunteer cheated!" % m
        elif len(inters) == 1:
            print "Case #%d: %s" % (m,inters.pop())
        else:
            print "Case #%d: Bad magician!" % m
        t = t-1