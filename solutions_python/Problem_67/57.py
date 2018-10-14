import psyco
psyco.full()

name = 'C-small-attempt0'
f = open(name+'.in')
fo = open(name + '.out','w')

def gint():
    return int(f.next().strip())
    
def gints():
    return [int(x) for x in f.next().strip().split()]
    
    
N = gint()

for n in xrange(N):
    R = gint()
    pts = set()
    for i in xrange(R):
        x1,y1,x2,y2 = gints()
        for x in xrange(x1,x2+1):
            for y in xrange(y1,y2+1):
                pts.add((x,y))
    tot = 0
    while pts:
        newpts = set()
        for x,y in pts:
            if (x-1,y) in pts or (x,y-1) in pts:
                newpts.add((x,y))
            if (x-1,y+1) in pts:
                newpts.add((x,y+1))
        pts = newpts
        tot += 1
    fo.write('Case #%d: %d\n'%(n+1,tot))
        






f.close()
fo.close()
