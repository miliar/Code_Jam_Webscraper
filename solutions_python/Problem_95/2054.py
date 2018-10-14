from collections import defaultdict

googlerese_mapping = defaultdict()

googlerese_mapping['a'] = 'y'
googlerese_mapping['b'] = 'h'
googlerese_mapping['c'] = 'e'
googlerese_mapping['d'] = 's'
googlerese_mapping['e'] = 'o'
googlerese_mapping['f'] = 'c'
googlerese_mapping['g'] = 'v'
googlerese_mapping['h'] = 'x'
googlerese_mapping['i'] = 'd'
googlerese_mapping['j'] = 'u'
googlerese_mapping['k'] = 'i'
googlerese_mapping['l'] = 'g'
googlerese_mapping['m'] = 'l'
googlerese_mapping['n'] = 'b'
googlerese_mapping['o'] = 'k'
googlerese_mapping['p'] = 'r'
googlerese_mapping['q'] = 'z'
googlerese_mapping['r'] = 't'
googlerese_mapping['s'] = 'n'
googlerese_mapping['t'] = 'w'
googlerese_mapping['u'] = 'j'
googlerese_mapping['v'] = 'p'
googlerese_mapping['w'] = 'f'
googlerese_mapping['x'] = 'm'
googlerese_mapping['y'] = 'a'
googlerese_mapping['z'] = 'q'



count = input()

count = count + 1

original_line = ""
transformed_line = ""
for line_index in xrange(0, count-1):
	case_index = (line_index+1) #adjust since cases aren't zero-indexed
	
	original_line = raw_input()
	transformed_line = list(original_line)

#	print googlerese_mapping[original_line[1]]
	
	for char_index in xrange(0, len(transformed_line)):
		if (transformed_line[char_index] != ' '):
#			print original_line[char_index] + " > " +  googlerese_mapping[original_line[char_index]]
			transformed_line[char_index] = googlerese_mapping[original_line[char_index]]

	print "Case #" + str(case_index) + ": " + "".join(transformed_line)
