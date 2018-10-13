translations = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(input):
	output = ''
	for i in input:
		try:
			output += translations[i]
		except KeyError:
			print 'No translation for %s' % i
			output += i
	return output

fp = open('inputs.txt', 'r')
input = fp.readlines()
fp.close()
fp = open('output.txt', 'w')
cases = int(input[0].strip('\n'))
for i in range(1, cases+1):
	fp.write('Case #%d: ' % i  + translate(input[i].strip('\n')) + '\n')
