# Katja Collier
# Code Jam 2012: Qualification round, problem A. Speaking in Tongues


# Note: I solved the cipher by hand, so this code simply reads the input and
# writes the encoded message


import sys

def decodeLine(line) :
	decoded = ""
	for ch in line :
		if ch == ' ' :
			decoded += ' '
		elif ch == 'y' :
			decoded += 'a'
		elif ch == 'n' :
			decoded += 'b'
		elif ch == 'f' :
			decoded += 'c'
		elif ch == 'i' :
			decoded += 'd'
		elif ch == 'c' :
			decoded += 'e'
		elif ch == 'w' :
			decoded += 'f'
		elif ch ==  'l' :
			decoded += 'g'
		elif ch ==  'b' :
			decoded += 'h'
		elif ch ==  'k' :
			decoded += 'i'
		elif ch ==  'u' :
			decoded += 'j'
		elif ch ==  'o' :
			decoded += 'k'
		elif ch ==  'm' :
			decoded += 'l'
		elif ch ==  'x' :
			decoded += 'm'
		elif ch == 's' :
			decoded += 'n'
		elif ch == 'e' : 
			decoded += 'o'
		elif ch == 'v' :
			decoded += 'p'
		elif ch == 'z' :
			decoded += 'q'
		elif ch == 'p' :
			decoded += 'r'
		elif ch == 'd' :
			decoded += 's'
		elif ch == 'r' :
			decoded += 't'
		elif ch == 'j' :
			decoded += 'u'
		elif ch == 'g' :
			decoded += 'v'
		elif ch == 't' :
			decoded += 'w'
		elif ch == 'h' :
			decoded += 'x'
		elif ch == 'a' :
			decoded += 'y'
		elif ch == 'q' :
			decoded += 'z'
			
	return decoded
		

input = sys.stdin
i = 0
for line in input :
	if i>0:
		print "Case #%d: %s" % (i, decodeLine(line))
	i+=1
