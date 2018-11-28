import math

def minmax( n, k ):
    level = math.floor( math.log( k, 2 ) )
    top_levels_count = 2**level - 1
    average_size = ( n - top_levels_count ) / 2**level
    max_size = math.ceil( average_size )
    no_of_max_size = ( n - top_levels_count ) % 2**level

    if( no_of_max_size == 0 ):
        no_of_max_size = 2**level


    if( k - top_levels_count <= no_of_max_size ):
        size = max_size
    else:
        size = max_size - 1

    min = math.floor( ( size - 1 ) / 2 )
    max = math.ceil( ( size - 1 ) / 2 )

    return( [ max, min ] )


f = open('C:\\Users\\nandi\\Desktop\\stalls.txt', 'r')
lines = f.readlines()
i = 0
fw = open( 'C:\\Users\\nandi\\Desktop\\stalls_output.txt', 'w' )

line = lines[0]
line = line.replace( '\n', '' )
count = int( line )

lines = lines[1:]

points = []
case = 1
for line in lines:
    line = line.replace( '\n', '' )
    [ n, k ] = line.split( ' ' )
    n = int( n )
    k = int( k )
    [max,min] = minmax( n,k)
    out = "Case #" + str(case) + ": " + str( max ) + " " + str( min )
    case += 1
    fw.write(out)
    fw.write("\n")
    print( out )


"""
print( minmax( 4,2 ) )
print( minmax( 5,2 ) )
print( minmax( 6,2 ) )
print( minmax( 1000,1000 ) )
print( minmax( 1000,1 ) )


for i in range( 1 , 11 ):
    out = minmax( 10, i )
    print( out )
"""