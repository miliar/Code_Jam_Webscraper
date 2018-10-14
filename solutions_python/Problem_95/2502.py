import sys
# key to the language,
key = {
	'a' : 'y',
	'b' : 'n',
	'c' : 'f', # f or z
	'd' : 'i',
	'e' : 'c',
	'f' : 'w',
	'g' : 'l',
	'h' : 'b',
	'i' : 'k',
	'j' : 'u',
	'k' : 'o',
	'l' : 'm',
	'm' : 'x',
	'n' : 's',
	'o' : 'e',
	'p' : 'v',
	'q' : 'z', # f or z
	'r' : 'p',
	's' : 'd',
	't' : 'r',
	'u' : 'j',
	'v' : 'g',
	'w' : 't',
	'x' : 'h',
	'y' : 'a',
	'z' : 'q'
}
key = dict((v,k) for k, v in key.iteritems())

def encode(letter):
	try:
		return key[letter]
	except KeyError, e:
		return ""
	
def stringify(x, y):
	return x + y
	
if __name__ == '__main__':
	inputFile = None
	with open(sys.argv[1]) as f:
		inputFile = f.readlines()
	with open("answer.out", 'w') as out:	
		# loop through this many test cases
		offset = 1
		for x in range(int(inputFile[0])):
			words = inputFile[offset].split(' ')
			encodedLine = ""
			for word in words:
				encodedLine += reduce(stringify, map(encode, list(word))) + " "
			
			out.write("Case #" + str(offset) + ": " + encodedLine + "\n")
			print "Case #" + str(offset) + ": " + encodedLine
			offset += 1
	# alphabet = []
	# for k,v in key.iteritems():
	# 	if v != "=":
	# 		alphabet.append(v)
	# 
	# print sorted(alphabet)