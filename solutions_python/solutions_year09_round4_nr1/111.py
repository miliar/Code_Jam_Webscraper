
import psyco, sys
psyco.full()

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')





def ok(mat):
    d = len(mat)
    res = True
    for li in xrange(d):
        if mat[li] > (li+1):
            res = False
            break
    #print 'okmat: ', mat, res
    return res

def swap(mat, ia,ib):
    t = mat[ia]
    mat[ia] = mat[ib]
    mat[ib] = t

def calc(omat):
    if ok(omat):
        return 0
    
    cnt = 1
    nextMats = [omat]
    
    skips = set()
    skips.add(tuple(omat))
    
    while 1:
        mats = []
        for mat in nextMats:
            cmat = list(mat)
            for i in xrange(len(mat)-1):
                ca = i
                cb = i+1
                nmat = list(cmat)
                swap(nmat, ca,cb)
                if ok(nmat):
                    #print 'okmat', nmat, omat
                    return cnt
                else:
                    tm = tuple(nmat)
                    if not tm in skips:
                        mats.append(nmat)
                        skips.add(tm)
        cnt += 1
        nextMats = mats
            
    return cnt

ig = inGen()
ig.next()
cc = 1
for line in ig:
    d = int(line)
    mat = []
    for il in xrange(0,d):
        row = ig.next()
        rrow = ''.join(list(reversed(row)))
        i = rrow.find('1')
        if i != -1:
            v = d-i
        else:
            v = -1
        #print row, rrow, v
        mat.append(v)
    
    print "Case #%d: %s" % (cc, calc(mat))
    cc += 1
