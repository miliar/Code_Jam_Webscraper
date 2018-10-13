import sys


infile = sys.stdin

def convert(blues):
    reds = {}
    #print blues
    while blues:
        tl = min(blues)
        tr = (tl[0], tl[1]+1)
        bl = (tl[0]+1, tl[1])
        br = (tl[0]+1, tl[1]+1)
        #print tl,tr,bl,br
        if (tr in blues) and (bl in blues) and (br in blues):
            blues.remove(tl)
            blues.remove(tr)
            blues.remove(bl)
            blues.remove(br)
            reds[tl] = '/'
            reds[tr] = '\\'
            reds[bl] = '\\'
            reds[br] = '/'
        else:
            #print "Failed"
            return None
    return reds
    

T = int(infile.readline())
for i in xrange(T):
    R,C = map(int, infile.readline().split())
    blues = set()
    for r in xrange(R):
        row = infile.readline().strip()
        for c in xrange(C):
            if row[c]=='#':
                blues.add((r,c))

    reds = convert(blues)          
    print("Case #%d:" % (i+1))
    if reds is not None:
        for r in xrange(R):
            row = []
            for c in xrange(C):
                row.append(reds.get((r,c), '.'))
            print(''.join(row))
    else:
        print("Impossible")
