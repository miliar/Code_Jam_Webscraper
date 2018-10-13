import psyco
psyco.full()

import sys

def cmpt(idx, sign):
    def acmp(x,y):
        if x[idx] < y[idx]:
            return -1 *sign
        elif x[idx] > y[idx]:
            return 1 *sign
        else:
            return 0
    return acmp

def calc(N,A,B):
    w = {}
    for i in xrange(N):
        w[i] = (A[i], B[i], i)
    
    sa = sorted(w.values(), cmp=cmpt(0,1))
    sb = sorted(w.values(), cmp=cmpt(1,1))
    
    # wa0 leikkaa kaikkia wa>0 joilla wb<wab
    ic = 0
    for sai,aw in enumerate(sa):
        la,lb,li = aw # w1
        for sai2 in xrange(sai+1, N):
            la2,lb2,li2 = sa[sai2] # w2
            # jos w2:n b < w1:n b, ic+=1
            if lb2 < lb:
                ic += 1
            #print 'RRRRR', li,la,lb, '------', li2,la2,lb2
    
    return ic



def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    N = int(line)
    A,B = [],[]
    for n in xrange(N):
        a,b = [int(s) for s in ig.next().split(' ')]
        A.append(a)
        B.append(b)
        
    v = calc(N,A,B)
    print "Case #%d: %d" % (cn,v)
    cn += 1
