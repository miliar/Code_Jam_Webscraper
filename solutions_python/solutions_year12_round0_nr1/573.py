charmap = { 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o',
	'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u',
	'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
	'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w',
	'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a',
	'z':'q', ' ':' '}

def getTranslated( str ):
	res = []
	for i in range( len(str) ):
		res.append( charmap[ str[i] ] )
	return ''.join( res )


import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open( fileNameIn, 'r' )
lines = fileIn.readlines()

testcnt = int( lines[0] )
lineIdx = 1

fileOut = open( fileNameOut, 'w' )

for test in range( testcnt ):
	line = lines[lineIdx]
	lineIdx += 1

	res = getTranslated( line.rstrip() )

	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
