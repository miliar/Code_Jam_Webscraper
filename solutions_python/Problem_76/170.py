import sys

sys.stdin.readline() #skip number of tests
for d,line in enumerate( sys.stdin.readlines()[1::2] ):
    values = map( int, line.strip().split() )
    C = [0 for _ in range(19)]
    for v in values:
        bits = map(lambda x: (v & (1<<x)) >> x, range(19))
        for i,bit in enumerate(bits): C[i] += bit
        #print >>sys.stderr, bits

    if all( map(lambda x:x&1 == 0, C) ):
        res = str(sum(values) - min(values))
    else:
        res = "NO"

    print "Case #%d: %s" % (d+1, res)
