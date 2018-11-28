test = """5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8"""

test = file( "B-small-attempt0.in" ).read()

Lines = test.split( "\n" )
T = int( Lines[0] )

offset = 0
index = 1
for i in range( T ):
    H, W = map( int, Lines[offset + 1].split( " " ) )
    maps = []
    for j in Lines[offset + 2: offset + 2 + H]:
        maps.append( map( int, j.split( " " ) ) )

#    print maps
    offset = offset + 2 + H - 1

    directions = {}
    sink = []

    for j in range( H ):
        for i in range( W ):
            v = maps[j][i]
            dir = [( i, j - 1 ), ( i - 1, j ), ( i + 1, j ), ( i, j + 1 )]

            direction = None

            for d in dir:
                x, y = d
                if x < 0 or y < 0 or x >= W or y >= H:
                    continue
                x, y = d
                vv = maps[y][x]

                if vv < v:
                    direction = d
                    v = vv


            if not direction:
                sink.append( ( i, j ) )
            else:
                if direction in directions:
                    directions[direction].add( ( i, j ) )
                else:
                    directions[direction] = set( [( i, j )] )

    marks = {}
    def refmark( root, s ):
        if root not in directions:
            return
        for child in directions[root]:
            marks[child] = s
            refmark( child, s )

    for s in sink:
        refmark( s, s )


    sinkmark = {}
    o = 97

    sinks = sink
    print "Case #%s" % index
    index += 1

#    print marks, sinks
    for j in range( H ):
        for i in range( W ):
            if ( i, j ) in sinks:
                sink = ( i, j )
            else:
                sink = marks[( i, j )]
            if sink in sinkmark:
                print sinkmark[sink],
            else:
                sinkmark[sink] = chr( o )
                print chr( o ),
                o += 1
        print
#        print "\n"










