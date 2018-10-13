def is_tidy( num ):
    num_str = str( num )
    passes = True

    for i in range( len( num_str ) - 1 ):
        if( int( num_str[i+1] ) < ( int( num_str[i] ) ) ):
            passes = False

    if( passes ):
        return( True )
    else:
        return( False )

def find_first( number ):
    num_str = str( number )

    for i in xrange( len(num_str)-1 ):
        if( int( num_str[i+1] ) <= int( num_str[i] ) ):
            return( i )

    return 0

def change_num( num, index ):
    num_str = str( num )
    num_str = list( num_str )
    x = int( num_str[index] )

    num_str[index] = x-1

    for i in xrange( len( num_str ) - index - 1 ):
        num_str[i+index+1] = "9"
    print( num_str )

    return( num_str )

def convert_list( num_str ):
    num = ""
    for i in num_str:
        num += str( i )

    return( int( num ))
    

infile = open("B-small-attempt0.in", "r")
outfile = open("output.txt", "w")

t = int( infile.readline() )

for i in xrange( t ):
    num = int( infile.readline() )

    if( is_tidy( num ) ):
        outfile.write("Case #" + str(i+1) + ": " +str(num) +"\n" )
    else:
        index = find_first( num )
        num_list = change_num( num, index )
        num = convert_list( num_list )
        outfile.write("Case #"+ str(i+1) +": "+ str( num ) +"\n" )

infile.close()
outfile.close()

index = find_first( 122222 )
change_num( 122222, index )
convert_list( ['1', '1', '9', '9', '9', '9'] )
