googlerese_2_english = { \
	'a': 'y', \
	'b': 'h', \
	'c': 'e', \
	'd': 's', \
	'e': 'o', \
	'f': 'c', \
	'g': 'v', \
	'h': 'x', \
	'i': 'd', \
	'j': 'u', \
	'k': 'i', \
	'l': 'g', \
	'm': 'l', \
	'n': 'b', \
	'o': 'k', \
	'p': 'r', \
	'q': 'z', \
	'r': 't', \
	's': 'n', \
	't': 'w', \
	'u': 'j', \
	'v': 'p', \
	'w': 'f', \
	'x': 'm', \
	'y': 'a', \
	'z': 'q', \
	' ': ' ', \
}

# h & z are missing

if __name__ == '__main__':
	input_file = open('A-small-attempt0.in', 'r')
	output_file = open('A-small-attempt0.out', 'w')
	
	test_cases_count = int(input_file.readline())
	
	for line_number in range(test_cases_count):
		line = input_file.readline().strip()
		output = ''
		
		for i in range(len(line)):
			output += googlerese_2_english[line[i]]
		
		output_file.write('Case #%d: %s\n' % (line_number+1, output))
	
	input_file.close()
	output_file.close()