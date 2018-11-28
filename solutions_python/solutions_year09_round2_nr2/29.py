import sys
import psyco
psyco.full()

test = """3
115
1051
6233
"""
#test = sys.stdin.read()

test = open( "B-small-attempt2.in" ).read()


lines = test.split( "\n" )
offset = 0

N = int( lines[0] )


for i in range( N ):
    print "Case #%s:" % ( i + 1 ),
#    print lines[i + 1]
    number = map( int, lines[i + 1] )
#    number = [5, 1, 1]
#    number = [8, 0, 0, 0, 0]
#    number = lines[i + 1]
#    number = [6, 0, 0, 5, 9, 5]
    max = 0
    ns = []
    o = None
    for j in range( len( number ) ):
        index = len( number ) - j - 1
        if number[index] >= max:
            max = number[index]
            ns.append( number[index] )
        else:
#            print number[index], index
            ns.append( number[index] )
            o = int( number[index] )
            break

    if o == None:
        number.sort()
        b = filter( lambda i: i > 0 , number )
        number.remove( b[0] )
        number.insert( 0, b[0] )

        number.insert( 1, 0 )
        print ''.join( map( str, number ) )
#        for p in number:
#            print p,
#        print
    else:

        ns = map( int, ns )
        ns.sort()
    #    print ns, o, ns.index( o )
        offset = 0

        ox = ns.index( o )
        while( True ):
            if ns[ox + 1] == o:
                ox += 1
            else:
                break


        ns = [ns[ox + 1]] + ns[:ox + 1] + ns[ox + 2:]
        n = number[:-len( ns )] + ns
        print ''.join( map( str, n ) )
#    break


