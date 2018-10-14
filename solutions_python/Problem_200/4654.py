def check( a ):

    a = str(a)

    maxu = int(a[0])

    for i in range( 1, len(a) ):
        if int( a[i] ) < maxu:
            return ( False )
        else:
            maxu = int( a[i] )

    return ( True )

p = []

i = 1

limit = 10**4

while i <= limit:

    if ( check(i) ):
        p.append( i )

    i += 1

t = int( input() )

for i in range( t ):
    n = int( input() )

    ans = 1

    for j in range( len(p) ):
        if n < p[j]:
            ans = p[j-1]
            break
        elif n == p[j]:
            ans = p[j]
            break

    print( "Case #%d: %d" % ( i+1, ans ) )
