#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def each_combo(L,n):
    if n == 0:
        yield []
    elif n > len(L):
        # can't be done
        pass
    else:
        h = L[0]

        # combos containing h:
        for sub in each_combo( L[1:], n-1 ):
            yield [h] + sub

        # combos not containing h:
        for sub in each_combo( L[1:], n ):
            yield sub
        
if 0:
    for x in each_combo( range(100), 3 ): print x
    sys.exit()

def each_rem_3_pair():
    yield (0,0)
    yield (0,1)
    yield (0,2)

    yield (1,0)
    yield (1,1)
    yield (1,2)

    yield (2,0)
    yield (2,1)
    yield (2,2)

# for x in each_rem_3_pair(): print x

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    (n_trees,A,B,C,D,x0,y0,M) = map(int, getline().split() )
    trace(n_trees,A,B,C,D,x0,y0,M)

    bins = [[0]*3, [0]*3, [0]*3]
    def bins_add(X,Y): bins[X%3][Y%3] += 1

    if 0:
        bins = {}
        def bins_add(X,Y):
            k = (X % 3, Y % 3)
            if k in bins:
                bins[k] += 1
            else:
                bins[k] = 1

    # trees = []
    X = x0; Y = y0
    # trees.append( (X, Y) )
    bins_add(X,Y)
    for i in range( 1, n_trees ):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        # trees.append( (X, Y) )
        bins_add(X,Y)

    # assert len(trees) == n_trees
    # trace('trees at:', trees)

    assert sum(bins[0]) + sum(bins[1]) + sum(bins[2]) == n_trees
    # assert sum(bins.values()) == n_trees
    trace('bins:', bins)

    if 0:
        count = 0
        for combo in each_combo(trees,3):
            # trace(combo)
            # too much tracing slows it down!
            [(x1,y1),(x2,y2),(x3,y3)] = combo
            # trace(x1+x2+x3, (x1+x2+x3) %3)
            if (x1+x2+x3) % 3 == 0 and (y1+y2+y3) % 3 == 0:
                count += 1
                # trace('incr count to', count)
    else:
        t = False
        count = 0
        n_combos = n_trees * ( n_trees - 1 ) * (n_trees - 2) / (1*2*3)
        trace(n_combos)
        trace(bins)
        # for xm in range(3): for ym in range(3): trace(xm,ym)
        # binsi = bins.items()
        # trace(binsi)
        for (xm_a,ym_a) in each_rem_3_pair():
            k_a = bins[xm_a][ym_a]
            if t: trace('a',(xm_a,ym_a),k_a)
            if k_a == 0: continue
            bins[xm_a][ym_a] -= 1

            for (xm_b,ym_b) in each_rem_3_pair():
                k_b = bins[xm_b][ym_b]
                if t: trace('   b',(xm_b,ym_b),k_b)
                if k_b == 0: continue
                bins[xm_b][ym_b] -= 1

                for (xm_c,ym_c) in each_rem_3_pair():
                    k_c = bins[xm_c][ym_c]
                    if t: trace('      c',(xm_c,ym_c),k_c)
                    if k_c == 0: continue
                    bins[xm_c][ym_c] -= 1

                    if (xm_a + xm_b + xm_c) % 3 == 0 and (ym_a + ym_b + ym_c) % 3 == 0:
                        # We've got a choice of k_a for point a,
                        # k_b for point b
                        # k_c for point c
                        # and their center will be integral
                        if t: trace('                   ', k_a,k_b,k_c)
                        incr = k_a * k_b * k_c
                        if t: trace('                   ', 'incr count by', incr)
                        count += incr
                        # (but remember that's ordered)
                    else:
                        if t: trace('                   ', 'non-integral center')

                    bins[xm_c][ym_c] += 1

                bins[xm_b][ym_b] += 1

            bins[xm_a][ym_a] += 1

        trace(bins)

    # for each set of 3 distinct points,
    # we have counted it 6 times due to permutations
    # undo that
    assert count % 6 == 0
    count = count / 6

    print 'Case #%d: %s' % (case_num, count)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
