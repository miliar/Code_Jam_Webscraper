import re

f = open( "./A-large.in" , "r" )
out = open("./a.out" , 'w' )
t = int( f.readline() )
res = ['X won' , 'O won' , 'Draw' , 'Game has not completed']
r1 = re.compile( '(XXX[TX])|([TX]XXX)|(X[TX]XX)|(XX[TX]X)' )
r2 = re.compile( '(OOO[TO])|([TO]OOO)|(O[TO]OO)|(OO[TO]O)' )

def sol():
    s = []
    for i in range( 0 , 4 ):
        s.append( str( f.readline() ).replace( '\n' , '' ) )
    f.readline()
    #print( s )
    
    for i in range( 0 , 4 ):
        if r1.search( s[ i ] ) != None:
            return 0
        elif r2.search( s[ i ] ) != None:
            return 1

    for i in range( 0 , 4 ):
        cs = ''
        for j in range( 0 , 4 ):
            cs += s[ j ][ i ]
        #print( cs )
        if r1.search( cs ) != None:
            return 0
        elif r2.search( cs ) != None:
            return 1

    cs = ''
    for i in range( 0 , 4 ):
        cs += s[ i ][ i ]
    if r1.search( cs ) != None:
        return 0
    elif r2.search( cs ) != None:
        return 1

    cs = ''
    for i in range( 0 , 4 ):
        cs += s[ i ][ 3 - i ]
    if r1.search( cs ) != None:
        return 0
    elif r2.search( cs ) != None:
        return 1
    #print( '------')
    for ss in s:
        #print( ss )
        if ss.find('.') != -1:
            return 3
    return 2

for i in range( 0 , t ):
    #print( sol() )
    #print( "Case" , "#{0}:".format( i + 1 ) , res[ sol() ] )
    out.write( "Case " + "#{0}: ".format( i + 1 ) + res[ sol() ] + '\n' )
