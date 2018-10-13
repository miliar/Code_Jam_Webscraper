class mapping :
    def __init__( self ) :
        self.amap = {}

    def add( self , src , dest ) :
        for x,y in zip( src , dest ) :
            self.amap[ x ] = y

    def translate( self , src ) :
        res = ''.join( [ self.amap[ char ] for char in src ] )
        return res


def main():
    dest = []
    dest.append( 'ejp mysljylc kd kxveddknmc re jsicpdrysizq' )
    dest.append( 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' )
    dest.append( 'de kr kd eoya kw aej tysr re ujdr lkgc jv' )
    src = []
    src.append( 'our language is impossible to understandqz' )
    src.append( 'there are twenty six factorial possibilities' )
    src.append( 'so it is okay if you want to just give up' )
    m = mapping()
    for i in range( 3 ) :
        m.add( dest[ i ] , src[ i ] )

    print sorted( [ key for key in m.amap ] )
    print sorted( [ m.amap[ key ] for key in m.amap ] )
    fIn = open( "C:\\gjam\\googlorese\\in.txt" )
    fOut = open( "C:\\gjam\\googlorese\\out.txt" , 'w' )
    tasksCount = int( fIn.readline() )
    for task in range( 1 , tasksCount + 1 ) :
        fOut.write( 'Case #' + str( task ) + ': ' + m.translate( fIn.readline().strip( '\n' ) ) + '\n' )

if __name__ == '__main__':
    main()