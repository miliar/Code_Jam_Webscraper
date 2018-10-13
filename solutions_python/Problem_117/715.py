import sys

def patternpossible(lawn, n, m):
    # determine maximum cutting height in each direction
    m_max = []
    n_max = []
    for _n in xrange(n):
        n_max.append(max(lawn[_n]))
    for _m in xrange(m):
        m_max.append(max([lawn[_n][_m] for _n in xrange(n)])) 
    # print n_max
    # print m_max

    # check lawn
    for _n in xrange(n):
        for _m in xrange(m):
            # each field can only be as high as the max heights for n and m
            if not lawn[_n][_m] in [n_max[_n], m_max[_m]]:
                return False
    return True


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        n, m = f.readline().rstrip().split(' ')
        n = int(n); m = int(m)
        lawn = []
        for _n in xrange(n):
            lawn.append( [int(p) for p in f.readline().split()] ) 
        
        res = patternpossible(lawn, n, m)
        print "Case #%d: %s" % (_t+1, 'YES' if res else 'NO')

