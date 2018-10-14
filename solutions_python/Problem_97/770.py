import sys

T = int(sys.stdin.readline().strip())
for cs in xrange(1,T+1):
    A,B = map(int, sys.stdin.readline().strip().split())

    N = len(str(A))
    res = 0
    for n in xrange(A,B):
        s = str(n)
        mm = []
        for i in xrange(1,N):
            m = int(s[i:] + s[0:i])
            if n < m and m<=B:
                if m not in mm:
                    res +=  1
                mm.append(m)

    print 'Case #%d: %d' % (cs,res)
