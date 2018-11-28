# recycled.py

def generate_possibilities ( pair, sizes ) :
    output = set()
    size = sizes[0]
    counter = 1
    pair[1] = pair[0]
    while counter < sizes[0] :
        move_to_front = pair[0] % 10
        pair[0] = int ( pair[0] / 10 )
        pair[0] += move_to_front * ( 10**( size - 1 ) )
        tup = ( pair[1], pair[0] )
        output.add( tup ) 
        counter += 1

    return output

num_cases = int( input() )
counter = 0

while counter < num_cases :
    line = input()
    sizes = []
    possibilities = set()

    pair = line.split( ' ' )
    
    for x in range( 2 ) :
        pair[x] = int( pair[x] )
        sizes.append( len( str( pair[x] ) ) )

    upper_limit = pair[1]
    lower_limit = pair[0]
    while( pair[0] < upper_limit ):
        new_pair = [ pair[0], pair[1] ]
        possibilities |= generate_possibilities( new_pair, sizes )
        pair[0] += 1

    total = 0
    display = set()
    for x in possibilities :
        if ( len( str( x[0] ) ) == len ( str( x[1] ) ) ) and ( x[0] >= lower_limit ) and ( x[0] < x[1] ) and ( x[0] <= upper_limit ) and ( x[1] <= upper_limit ) and ( x[0] != x[1] ):
            display.add ( x )
            total += 1

    #print( display )
    counter += 1
    print( "Case #", counter, ": ", total, sep = '' )

