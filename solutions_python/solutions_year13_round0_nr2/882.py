import sys
import numpy as np

f= open(sys.argv[1])
cases = int(f.readline())
of = open(sys.argv[2],'w') #sys.stdout

for case in xrange(1, cases+1):
    N, M = [int(i) for i in f.readline().split()]
    a = []
    for i in xrange(0,N):
        heights = [int(i) for i in f.readline().split()]
        a.append(heights)
    a = np.array(a)
    row_maxs = np.max(a,axis=1)
    col_maxs = np.max(a,axis=0)

    def test_cuttable():
        for i in xrange(0,N):

            for j in xrange(0,M):
                if a[i][j] < row_maxs[i] and a[i][j] < col_maxs[j]:
                    return False
        return True
    of.write("Case #%s: %s\n"% (case, "YES" if test_cuttable() else "NO"))



