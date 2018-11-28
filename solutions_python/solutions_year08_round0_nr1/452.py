#!/usr/bin/python

FILE_NAME = "A-small-attempt5.in"

def get_cases( file_name ) :
	cases = []
	file_in = open(file_name , "r").read().split('\n')
	i = 0
	ncases = int(file_in[i])
	i+=1
	for c in range(ncases):
		line = file_in[i]
		nseng = int(line)
		i+=1
		seng = []
		for aux in range(nseng) :
			seng.append( file_in[i+aux] )
		i+=nseng
		line = file_in[i]
		nword = int(line)
		i+=1
		word = []
		for aux  in range(nword) :
			word.append( file_in[i+aux] )
		i+=nword
		cases.append( ( seng , word ) )
	return cases	

"""
def changes( l_seng , l_words ) :
	if len( l_words ) == 0 :
		return 0
	cchan = []
	for seng in l_seng :
		if seng != l_words[0] and seng in l_words :
			cchan.append( 1 + changes( l_seng , l_words[l_words.index(seng):] ) )
		elif seng != l_words[0] :
			return 0

	return min( cchan ) 	
"""


def changes( l_seng , l_words ) :
	if len( l_words ) == 0 :
		return 0
	index = 0
	for seng in l_seng :
		if seng != l_words[0] and seng in l_words :
			if l_words.index(seng) > index :
				index = l_words.index(seng)
		elif seng != l_words[0] :
			return 0
	print index , 
	return 1 + changes( l_seng , l_words[index:] )

cases = get_cases(FILE_NAME)
print cases
output = ""
for i in range( len( cases ) ) :
	print i
	cc = changes( cases[i][0] , cases[i][1] )
	output += "Case #%d: %d\n" % ( i+1 , cc )
	print "\n"

file_out = file( "test.out" , "w" )

file_out.write( output )

file_out.close()

