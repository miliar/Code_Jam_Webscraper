import sys, numpy

def possible(m):
    min_ = m.min()
    max_ = m.max()
    while (min_ != max_):
        btable = m == min_
        indices = numpy.where(btable)
        for i, j in zip(indices[0], indices[1]):
            doable = False
            if numpy.array(map(lambda x,y: x or y, m[i,:] == min_, m[i,:] > max_)).all():
                doable = True
                #btable[i,:] = False
                m[i,:] = max_ + 1
                m[i,j] = min_
            if numpy.array(map(lambda x,y: x or y, m[:,j] == min_, m[:,j] > max_)).all():
                doable = True
                #btable[:,j] = False
                m[:,j] = max_ + 1
                m[i,j] = min_
            if not doable:
                return "NO"
            else:
                m[i,j] = max_ + 1
            #print >> sys.stderr, m
            min_ = m.min()
            if min_ == max_:
                break
            btable = m == min_
            indices = numpy.where(btable)
    return "YES"


N = int(sys.stdin.readline().rstrip('\n'))
n = 1
while n <= N:
    dim_x, dim_y = map(int, sys.stdin.readline().rstrip('\n').split())
    mat = numpy.ndarray((dim_x, dim_y), dtype='int')
    for i in xrange(dim_x):
        mat[i] = map(int, sys.stdin.readline().rstrip('\n').split())
    #print mat
    #print >> sys.stderr, n
    print "Case #" + str(n) + ": " + possible(mat)
    n += 1


