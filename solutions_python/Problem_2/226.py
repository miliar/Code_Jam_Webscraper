#f = open( "B-small-attempt0.in", "rt" )
f = open( "B-large.in", "rt" )

numcases = int( f.readline( ).strip( ) )

def to_mins( s ):
    h,m = s.split(":")
    h = int(h)
    m = int(m)
    t = (h*60) + m
#    print "%s - %s:%s - %s" % (s, h, m, t)
    return t

for i in xrange(numcases):
    T = int( f.readline( ).strip( ) )
    NA, NB = f.readline( ).strip( ).split( " " )
    NA,NB = int(NA), int( NB )
    asched, bsched = [],[]
    for j in xrange( NA ):
        s,e = f.readline( ).strip( ).split( " " )
        s,e = to_mins( s ), to_mins( e )
        asched.append( (s,1) ) # 0 means arriving
        bsched.append( (e+T,0) )

    for j in xrange( NB ):
        s,e = f.readline( ).strip( ).split( " " )
        s,e = to_mins( s ), to_mins( e )
        bsched.append( (s,1) ) # 0 means arriving
        asched.append( (e+T,0) )

    asched.sort( )
    bsched.sort( )
    numa, numb = 0,0
    numata, numatb = 0,0
    ap = 0
    bp = 0
    while ap < len(asched) and bp < len(bsched):
        (a,b) = asched[ap]
        (c,d) = bsched[bp]
        if a < c:
#            print "A: (%s,%s)" % (a,b)
            if b == 0:
                numata += 1
            if b == 1:
                if numata == 0:
                    numa += 1
                    numata += 1
                numata -= 1
            ap += 1
        else:
#            print "B: (%s,%s)" % (c,d)
            if d == 0:
                numatb += 1
            if d == 1:
                if numatb == 0:
                    numb += 1
                    numatb += 1
                numatb -= 1
            bp += 1
    print "Case #%s: %s %s" % (i+1, numa, numb)

            
