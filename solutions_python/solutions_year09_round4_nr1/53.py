import sys

if __name__ == '__main__':
    s = sys.stdin.readline()
    C = int(s)
    for c in xrange(1,C+1):
        N = int(sys.stdin.readline())
        l = [0 for i in xrange(N)]
        for i in xrange(N):
            r = sys.stdin.readline()
            for j in xrange(N):
                if r[j] == '1':
                    l[i] = j
        #print l
        swaps = 0
        for i in xrange(N):
            #print 'i', i
            j = i
            while j < N and l[j] > i:
                j += 1
            assert j < N
            for k in xrange(j, i, -1):
                swaps += 1
                t = l[k-1]
                l[k-1] = l[k]
                l[k] = t
                #print 'swap:', l
        print 'Case #%d: %d' % (c, swaps)

                
