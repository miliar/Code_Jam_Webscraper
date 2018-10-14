import sys

for d,line in enumerate( sys.stdin.readlines()[2::2] ):
    values = map( int, line.strip().split() )
    unsorted = [i for i,v in enumerate(values) if i+1 != v]
    E = float(len(unsorted))
    print "Case #%d: %.6f" % (d+1, E)
