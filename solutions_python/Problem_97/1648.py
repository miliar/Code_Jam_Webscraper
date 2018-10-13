import sys

rl = lambda : sys.stdin.readline().strip()

ncase = int( rl() )

for caseno in xrange(1,ncase+1):
    A, B = map( int, rl().split() )
    sz = len(str(A))
    ret = 0
    for i in xrange(A,B+1):
        s = str(i)
        for j in xrange(sz-1):
            s = s[1:] + s[:1]
            if i < int(s) and int(s) <= B:
                #print i, s
                ret += 1


    print "Case #%d: %d" %( caseno, ret )
