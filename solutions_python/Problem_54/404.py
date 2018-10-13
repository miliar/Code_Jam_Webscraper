import sys, fractions

num_cases = int( sys.stdin.readline() )

for case_num in range( 1, num_cases + 1 ):
    t = []
    diff = []

    numbers = sys.stdin.readline().split()
    N = int( numbers[0] );
    for i in range( N ):
        t.append( int( numbers[i+1] ) )

    t.sort()

    for i in range( N - 1 ):
        d = t[i+1] - t[i]
        if d != 0:
            diff.append( d )

    if len( diff ) > 1:
        gcd = diff[0]
        for i in range( 1, len( diff ) ):
            gcd = fractions.gcd( gcd, diff[i] )
    else:
        gcd = diff[0]

    rem = t[0] % gcd
    result = 0
    if rem != 0:
        result = gcd - rem
    print 'Case #{0}: {1}'.format( str(case_num), result )
