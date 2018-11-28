import os
import sys
import fractions

n = int( sys.stdin.readline().strip() )

for i in range( n ):
    ln = [ int(a) for a in sys.stdin.readline().strip().split(' ') ]
    ln = ln[1:]
    #ln.append( 0 )
    ln.sort()
    diffs = []
    for a in range( len(ln) ):
        if a < ( len(ln) - 1 ):
            d = abs( ln[a] - ln[a+1] )
            if d != 0:
                diffs.append( d )

    #print ln
    m_curr = 0
    for a in range( len( diffs ) ):
        m_curr = fractions.gcd( m_curr, diffs[ a ] )

    m = m_curr

        
    #print diffs, m
    if m == 1:
        m = 0
        y = 0
    elif m != 0:
        y = ln[0] % m
        if y == 0:
            m = 0
    else:
        y = 0
    #print y
    print 'Case #%d: %s' % ( i+1, m - y, )
