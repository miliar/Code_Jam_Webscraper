import sys

T = int( raw_input( ) )
strings = [ raw_input( ) for i in xrange( T ) ]

input = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
output = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

reverseMap = {
    'z': 'q',
    'q': 'z',
    ' ': ' '
}
for i in xrange( len( input ) ) :
    c = input[ i ]
    if c != ' ' and not( c in reverseMap ) :
        reverseMap[ c ] = output[ i ]

#missingLetters = [ c for c in 'abcdefghijklmnopqrstuvwxyz' if not( c in reverseMap ) ]
#print 'Missing letters: ' + str( ' '.join( missingLetters ) )
#antecedents = set( [ reverseMap[ c ] for c in 'abcdefghijklmnopqrstuvwxyz' if c in reverseMap ] )
#missingAntecedents = [ c for c in 'abcdefghijklmnopqrstuvwxyz' if not( c in antecedents ) ]
#print 'Missing letters: ' + str( ' '.join( missingAntecedents ) )

print '\n'.join(
    [ 'Case #' + str( i + 1 ) + ': ' + str( ''.join( [ reverseMap[ c ] for c in strings[ i ] ] ) ) for i in xrange( T ) ]
)
