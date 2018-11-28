from sys import argv

key = {' ': ' ',
       'a': 'y',
       'b': 'h',
       'c': 'e',
       'd': 's',
       'e': 'o',
       'f': 'c',
       'g': 'v',
       'h': 'x',
       'i': 'd',
       'j': 'u',
       'k': 'i',
       'l': 'g',
       'm': 'l',
       'n': 'b',
       'o': 'k',
       'p': 'r',
       'q': 'z',
       'r': 't',
       's': 'n',
       't': 'w',
       'u': 'j',
       'v': 'p',
       'w': 'f',
       'x': 'm',
       'y': 'a',
       'z': 'q'}

def pairs(plain, cypher):
	assert len(plain) == len(cypher)

	result = {}
	for i in xrange(len(plain)):
		if not plain[i].isalpha():
			continue
		if result.has_key(cypher[i]):
			assert result[cypher[i]] == plain[i]
		else:
			result[cypher[i]] = plain[i]

	return result

def decrypt(text):
	return "".join([key[c] for c in text])

if __name__ == "__main__":
	filename = argv[1]
	with open(filename, 'r') as f:
		lines = f.readlines()
	assert int(lines[0]) == len(lines) - 1
	lines = lines[1:]
	i = 1
	for line in lines:
		print "Case #{}: {}".format(i, decrypt(line.rstrip()))
		i += 1
