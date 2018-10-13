dictionary = {
'y': 'a',
'n': 'b',
'f': 'c',
'i': 'd',
'c': 'e',
'w': 'f',
'l': 'g',
'b': 'h',
'k': 'i',
'u': 'j',
'o': 'k',
'm': 'l',
'x': 'm',
's': 'n',
'e': 'o',
'v': 'p',
'z': 'q',
'p': 'r',
'd': 's',
'r': 't',
'j': 'u',
'g': 'v',
't': 'w',
'h': 'x',
'a': 'y',
'q': 'z'}

if __name__ == '__main__':
	num_test_cases = int(raw_input())

	n = 0
	while n < num_test_cases:
		line = list(raw_input())
		out = "Case #" + str(n+1) + ": "
		i = 0
		while i < len(line):
			if line[i] != ' ':
				line[i] = dictionary[line[i]]
			out += line[i]
			i += 1
		print out
		n += 1
			
