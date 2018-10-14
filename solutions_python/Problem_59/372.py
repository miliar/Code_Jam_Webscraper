import sys

num_cases = int( sys.stdin.readline() )

for case_num in xrange(1,num_cases+1):
    (N,M) = map( int, sys.stdin.readline().split() )
    edirs = []
    for i in xrange(N):
        edirs.append( sys.stdin.readline()[:-1] )

    mkdircalls = 0
    for i in xrange(M):
        dirs = sys.stdin.readline()[1:-1].split("/")
        epath = ""
        for i,d in enumerate(dirs):
            epath += "/" + d
            if epath not in edirs:
                mkdircalls += 1
                edirs.append( epath )

    print "Case #%d: %d" % (case_num,mkdircalls)
