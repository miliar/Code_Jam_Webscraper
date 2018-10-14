import psyco
psyco.full()
import sys




def calc(rows, w,h):
    
    rlist = []
    for r in rows:
        rlist.append(list(r))
    
    r = lambda r,c: rlist[r][c]
    
    for ri in xrange(h-1):
        for ci in xrange(w-1):
            if r(ri,ci) == '#':
                t = r(ri,ci) +r(ri+1,ci) +r(ri,ci+1) +r(ri+1,ci+1)
                if t == '####':
                    rlist[ri][ci] = '/'
                    rlist[ri+1][ci] = '\\'
                    rlist[ri][ci+1] = '\\'
                    rlist[ri+1][ci+1] = '/'
    
    if '#' in ''.join([''.join(a) for a in rlist]):
        return "Impossible\n"
    else:
        s = ''
        for row in rlist:
            s += ''.join(row) + "\n"
        return s

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    
    h,w = [int(a) for a in line.split(' ')]
    rows = []
    for ri in xrange(h):
        rows.append(ig.next())
    
    v = calc(rows, w,h)
    print "Case #%d:\n%s" % (cn,v[:len(v)-1])
    cn += 1
