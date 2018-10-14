
import psyco, sys
psyco.full()

def fact(x):
    if x == 0:
        return 1
    v = 1
    for m in xrange(1, x+1):
        v *= m
    
    return v


def gen_lexi_perms(objs, startN=1, currN=0, distinct=False):
    if len(objs) == 0:
        return  
    elif len(objs) == 1:
        yield objs
        return
    ol = len(objs)
    covered = set()
    for ci in xrange(ol):
        c = [objs[ci]]
        if distinct:
            if objs[ci] in covered:
                continue
            else:
                covered.add(objs[ci])
        s = objs[0:ci] + objs[ci+1:] # the rest
        sc = fact(ol-1)
        if (sc + currN) >= startN:
            sg = gen_lexi_perms(s, startN, currN, distinct)
            for sp in sg:
                yield c + sp
        currN += sc

def calc(sn):
    ssn = list(sorted([0]+sn))
    #print 'ssn', ssn
    g = gen_lexi_perms(ssn, distinct=True)
    
    def j(lst):
        return ''.join([str(a) for a in lst])
    
    n = g.next()
    #print 'drd', j(n)
    while int(j(n)) <= int(j([0]+sn)):
        n = g.next()
        #print 'drd', j(n)
    ret = j(n)
    #print 'rrr', ret
    #print j(g.next()),j(g.next()),j(g.next())
    return ret.lstrip('0')


def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cc = 1
for line in ig:
    print "Case #%d: %s" % (cc, calc(list(line)))
    cc += 1
