from re import match

def alien(filename):
	dictionary = []
	tests = []
	
	with open(filename) as f:
	
		# Get codes
		L, D, N = map(int, f.next().strip().split(' ', 3))
		
		# Get words into dictionary
		for i in range(D):
			word = f.next().strip()
			if len(word) == L:
				dictionary.append(word)
			else:
				print '[!!!] Word %s length != %i ' % (word, L)
		
		# Create patterns.
		for i in range(N):
			test = f.next().strip()
			test = test.replace('(', '[')
			test = test.replace(')', ']')
			tests.append(test)
	
	# Run the patterns against the dictionary and print result.
	for i, test in enumerate(tests, 1):
		occurrences = 0
		for word in dictionary:
			if match(test, word):
				occurrences += 1
		print 'Case #%i: %i' % (i, occurrences)

if __name__ == "__main__":
    alien('A-large.in')