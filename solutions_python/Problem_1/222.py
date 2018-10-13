f = open( "A-large.in", "rt" )
#f = open( "A-small-attempt2.in", "rt" )
numcases = int( f.readline( ).strip( ) )

def count_next( qs, e ):
    count = 0
    for q in qs:
        if q == e:
            return count, e
        count += 1
    return count, e

def min_switches( qs, es, cur, cum=0 ):
#    print qs
    # Count the number of queries until we need to change
    count = 0
    switches = 0
    minv = 99999999
    for count in xrange(len(qs)):
        if qs[count] == cur:            
            sw = [ count_next( qs[count:], e ) for e in es if e != cur]
            m = 0
            be = None
            for c,e in sw:
                if c > m:
                    m = c
                    be = e
            switches += 1
            cur = be
#            return 1 + min_switches( qs[count+c:], es, be )
    return switches

    

for i in xrange(numcases):
    numengines = int( f.readline( ).strip( ) )
    engines = {}
    for j in xrange(numengines):
        engines[ f.readline( ).strip( ) ] = 1
#    print engines
    numqueries = int( f.readline( ).strip( ) )
    queries = [ f.readline( ).strip( ) for q in xrange(numqueries) ]
    mv = 9999999999
    for e in engines:
        m = min_switches( queries, engines, e )
        if m < mv:
            mv = m
#            print "Minimum ", mv, " for ", e
    print "Case #%s: %s" % (i+1, mv)

    
