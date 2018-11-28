import sys
sin = sys.stdin
T = int(sin.readline().strip())
for p in xrange(T):
    out = []
    m = {}
    R, C = map(int, sin.readline().strip().split())
    for j in xrange(R):
        r = sin.readline().strip()
        out.append(list(r))
        for idx, k in enumerate(r):
            if k != '?':
                m[k] = [j, idx, j, idx]

    #print out
    #print m
    for c in m:
        range = m[c]
        minr, minc, maxr, maxc = range
        # find min-row
        skip = False
        for i in reversed(xrange(minr)):
            if skip:
                break
            for j in xrange(range[1], range[3]+1):
                if out[i][j] not in ['?', c]:
                    skip = True
                    break
            if not skip:
                #range[0] -= 1
                range[0] = i
                #print 'extending minr to: {0}'.format(range[0])

        # find max-row
        skip = False
        for i in xrange(maxr, R):
            if skip:
                break
            for j in xrange(range[1], range[3]+1):
                #print 'checking {0} {1}: {2}'.format(j, i, out[i][j])
                if out[i][j] not in ['?', c]:
                    skip = True
                    break
            if not skip:
                #range[2] += 1
                range[2] = i
                #print 'extending maxr to: {0}'.format(range[2])

        # find min-col
        skip = False
        for i in reversed(xrange(minc)):
            if skip:
                break
            #print 'starting loop from {0} to {1}'.format(minr, maxr)
            for j in xrange(range[0], range[2]+1):
                #print 'checking {0} {1}: {2}'.format(j, i, out[j][i])
                if out[j][i] not in ['?', c]:
                    skip = True
                    break
            if not skip:
                #range[1] -= 1
                range[1] = i
                minc = i
                #print 'extending minc to: {0}'.format(range[1])
                
        # find max-col
        skip = False
        for i in xrange(maxc, C):
            #print 'checking col#{0}'.format(i)
            if skip:
                break
            for j in xrange(range[0], range[2]+1):
                #print 'checking row#{0}, val:{1}'.format(j, out[j][i])
                if out[j][i] not in ['?', c]:
                    skip = True
                    break
            if not skip:
                #range[3] += 1
                range[3] = i
                #print 'extending maxc to: {0}'.format(range[3])

        #print '{0}: {1}'.format(c, range)
        for i in xrange(range[0], range[2]+1):
            for j in xrange(range[1], range[3]+1):
                out[i][j] = c
        #print 'out after assinging {0} is {1}'.format(c, out)
            
    print 'Case #{0}:'.format((p+1))
    for r in out:
        print ''.join(r)
    