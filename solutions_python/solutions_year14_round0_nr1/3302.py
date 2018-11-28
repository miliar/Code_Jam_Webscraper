f = open('A-small-attempt3.in')

def readint(f):
    return int(f.readline()[:-1])

def readints(f):
    return map(int, f.readline()[:-1].split())

ntests = readint(f)

for i in xrange(ntests):
    pick1 = readint(f)
    cards1 = [readints(f) for _ in xrange(4)]
    pick2 = readint(f)
    cards2 = [readints(f) for _ in xrange(4)]
    picked1 = set(cards1[pick1-1])
    picked2 = set(cards2[pick2-1])
    common = picked1 & picked2
    if len(common) == 1:
        print "Case #%d: %d" % (i+1, common.pop())
    elif len(common) > 1:
        print "Case #%d: Bad magician!" % (i+1)
    elif len(common) == 0:
        print "Case #%d: Volunteer cheated!" % (i+1)
