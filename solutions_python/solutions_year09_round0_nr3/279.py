
def match( line, word ):

	if len( word ) == 0:
		return 1;
	
	if len( line ) == 0:
		return 0;

	if line[0] == word[0]:
		return (match( line[1:], word[1:] ) + match( line[1:], word )) % 1000;
	else:
		return match( line[1:], word );


f = open("C-small-attempt0.in");

N = int(f.readline()[:-1]);

word = "welcome to code jam";

for i in xrange( N ):
	line = f.readline()[:-1];
	print "Case #" + str( i+1 ) + ": " + str( match( line, word ) ).zfill(4);
	
	

