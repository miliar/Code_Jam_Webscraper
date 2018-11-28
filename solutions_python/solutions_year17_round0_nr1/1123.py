import math

def modify_pattern( pattern ):
    new_pattern = [];
    for i in pattern:
        if( i == '-' ):
            new_pattern.append( 0 )
        else:
            new_pattern.append( 1 )
    return( new_pattern )

def flip_pancake( pattern, k, case, fw ):
    pattern = modify_pattern( pattern )
    count = 0
    length = len( pattern )
    for i in range( 0, length - k + 1 ):
        if pattern[ i ] == 0:
            for j in range( i, i+k ):
                pattern[ j ] = ( pattern[ j ] + 1 ) % 2
            count = count + 1

    for i in range( length - k + 1, length ):
        if( pattern[ i ] == 0 ):
            count = "IMPOSSIBLE"
            break

    out = "Case #" + str(case) + ": " + str(count)
    fw.write(out)
    fw.write("\n")
    print( out )



f = open('C:\\Users\\nandi\\Desktop\\opf.txt', 'r')
lines = f.readlines()
i = 0
fw = open( 'C:\\Users\\nandi\\Desktop\\opf_output.txt', 'w' )

line = lines[0]
line = line.replace( '\n', '' )
count = int( line )

lines = lines[1:]
case = 1
for line in lines:
    [ pattern, k ] = line.split( " " )
    pattern = list( pattern )
    k = int( k )
    flip_pancake( pattern, k, case, fw )
    case += 1

