import sys

def readline():
    return sys.stdin.readline().strip()

for t in range( int( readline() ) ):
    print 'Case #%i:' % ( t + 1 )
    H, W = ( int( x ) for x in readline().split() )
    altitudes = []
    for row in range( H ):
        altitudes.append( [ int( altitude ) for altitude in readline().split() ] )
    basins = [ [ None for column in range( W ) ] for row in range( H ) ]
    basin_index = 0
    for row in range( H ):
        for column in range( W ):
            flow_row = row
            flow_column = column
            basin = []
            while basins[ flow_row ][ flow_column ] is None:
                basins[ flow_row ][ flow_column ] = basin_index
                basin.append( ( flow_row, flow_column ) )
                altitude = altitudes[ flow_row ][ flow_column ]
                lower_row = None
                for test_row, test_column in ( ( flow_row - 1, flow_column ), ( flow_row, flow_column - 1 ), ( flow_row, flow_column + 1 ) , ( flow_row + 1, flow_column ) ):
                    if test_row == -1 or test_row == H or test_column == -1 or test_column == W:
                        continue
                    if altitudes[ test_row ][ test_column ] < altitude:
                        flow_row = test_row
                        flow_column = test_column
                        altitude = altitudes[ test_row ][ test_column ]
            if basins[ flow_row ][ flow_column ] != basin_index:
                for fix_row, fix_column in basin:
                    basins[ fix_row ][ fix_column ] = basins[ flow_row ][ flow_column ]
            basin_index += 1

    basin_set = set()
    for row in basins:
        for cell in row:
            basin_set.add( cell )
    lookup = dict( ( basin, chr( 97 + index ) ) for index, basin in enumerate( sorted( list( basin_set ) ) ) )
    for row in basins:
        print ' '.join( lookup[ basin ] for basin in row )
