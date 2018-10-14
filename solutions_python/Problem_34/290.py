import re

if __name__ == '__main__':
	#in_filename = "A-small.in"
	#in_filename = "A-dummy.in"
	in_filename = "A-large.in"
	#out_filename = "A-small.out"
	out_filename = "A-large.out"
	
	in_file = open(in_filename, 'r')
	out_file = open(out_filename, 'w')

	L,D,num_cases  = [int(x) for x in in_file.readline().split(' ')]

	# Read the dictionary
	words = []	
	for i in range(0,D):
		words.append(in_file.readline())
	
	
	for c in range(0,num_cases):
		# Clone a list
		ws = words[:]
		s = in_file.readline()
		clues = re.findall('(\([a-z]+\)|[a-z])',s)
		#print clues
		for k in range(0,len(clues)):
			ws = filter(lambda x: clues[k].find(x[k]) != -1, ws)
		out_file.write("Case #%d: %d\n" % (c+1, len(ws)))

	out_file.close()

