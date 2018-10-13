##    repeat k - 1 times:
##        identify longest string of unoccupied stalls
##
##        if( longest string % 2 == 0 ):
##            choose 1 to left of middle
##        else:
##            choose middle
##
##    for last k:
##        if( len of str of stalls is odd ):
##            y & z = len of str of stalls / 2 rounded down
##        else:
##            y = len of str of stalls / 2
##            z = y - 1

def get_longest_str( current_stalls ):
    actual_max = 0
    current_max = 0
    current_index = 0
    actual_index = 0

    for i in xrange( len( current_stalls )):
        if( current_stalls[i] == "." ):
            current_max += 1
        elif( current_stalls[i] == "o" ):
            if( current_max > actual_max ):
                actual_max = current_max
                actual_max_index = current_index
            current_max = 0
            current_index = i + 1
        else:
            print( "You done messed up AAron" )

    return( [actual_max_index, actual_max] )

def make_stalls( n ):
    stalls = ["o"]

    for i in xrange( n ):
        stalls.append(".")

    stalls.append("o")

    return( stalls )
        

infile = open("C-small-1-attempt1.in", "r")
outfile = open("output.txt", "w")

t = int( infile.readline() )

for i in xrange( t ):
    inputs = infile.readline().rstrip()
    input_parts = inputs.split(" ")
    n = int( input_parts[0] )
    k = int( input_parts[1] )

    stalls = make_stalls( n )

    for j in xrange( k - 1 ):
        info = get_longest_str( stalls )
        index = info[0]
        length = info[1]
        if( length % 2 == 0 ):
            point = index + length/2 - 1
        else:
            point = index + int( (length)/2 )

        stalls[point] = "o"

    info = get_longest_str( stalls )
    index = info[0]
    length = info[1]

    if( length % 2 == 0 ):
        y = length/2
        z = y - 1
    else:
        y = int( length / 2 )
        z = y
        
    outfile.write( "Case #"+ str(i+1) +": "+ str(y) +" "+ str(z) +"\n" )

    

infile.close()
outfile.close()

##get_longest_str( ["o",".",".",".",".",".","o"] )
##get_longest_str( ["o",".",".",".","o",".",".","o"] )
##get_longest_str( ["o",".",".","o",".",".",".","o"] )
