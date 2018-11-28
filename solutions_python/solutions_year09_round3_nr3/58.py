
import psyco, sys
psyco.full()

#
#
#   1    2    3    4    5    6    7    8    9    10    11    12    13    14    15    16    17    18    19    20
#
#  
#             x              x                                           x
#
#
#

def gen_combinations(objs, combLen=None):
    if combLen==None:
        combLen = len(objs)
    lastObj = objs[-1]
    lastComb = [lastObj] * combLen
    comb = [objs[0]] * combLen
    yield comb
    while comb != lastComb:
        for oi in xrange(combLen):
            o = comb[oi]
            if o != lastObj:
                comb[oi] = objs[objs.index(o) + 1]
                break
            else:
                comb[oi] = objs[0]
        yield comb

def gen_orders(objs):
    gc = gen_combinations(objs)
    for c in gc:
        uniques = set()
        for ac in c:
            uniques.add(ac)
        if len(uniques) == len(c):
            #print 'uni',uniques
            #print c
            yield c


def calc(p,q,cns):
    s = None
    sord = None
    
    go = gen_orders(cns)
    for order in go:
        #print 'ord',order
        state = [1] * p # all prisoned
        #print state
        price = 0
        for r in order:
            state[r-1] = 0
            lr = range(r-2,-1,-1)
            #print 'llllll', r-1, lr
            for left in lr:
                if state[left] == 1:
                    price += 1
                else:
                    break
            rr = xrange(r,len(state))
            #print 'rrrr', r-1, range(r,len(state))
            for right in rr:
                if state[right] == 1:
                    price += 1
                else:
                    break
        if s == None or price < s:
            s = price
            #print 'sord assi', order
            sord = list(order)
    #print 'sord',sord
    return str(s)

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cc = 1
for line in ig:
    p,q = [int(a) for a in line.split(' ')]
    cns = [int(a) for a in ig.next().split(' ')]
    print "Case #%d: %s" % (cc, calc(p,q,cns))
    cc += 1
