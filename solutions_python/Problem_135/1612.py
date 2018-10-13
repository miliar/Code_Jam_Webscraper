
import codecs

fp = codecs.open('input.in', 'r', 'utf-8')
test_cases = int( fp.readline() )

for x in xrange( test_cases ):
	f_answer, f_cards = int( fp.readline() ), []
	for y in xrange( 4 ):
		f_cards.append( map( int, fp.readline().split() ) )

	s_answer, s_cards = int( fp.readline() ), []
	for y in xrange( 4 ):
		s_cards.append( map( int, fp.readline().split() ) )

	result = list( set( f_cards[f_answer-1] ) & set( s_cards[s_answer-1] ) )
	if len( result ) == 1:
		status = str( result[0] )

	elif len( result ) == 0:
		status = 'Volunteer cheated!' 

	else:
		status = 'Bad magician!'

	print 'Case #%d: %s' % ( x+1, status )