def start(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	numTest = int(lines[0])
	pancakeTest(numTest, lines[1:])


def pancakeTest(numTest, inputs):
	output = open('pancake_large_output.in', 'w')
	for i in xrange(numTest):

		res = pancake(i, inputs[i])
		output.write(res + '\n')
	output.close()



def pancake(l, inpt):
	string, k = inpt.split(' ')
	k = int(k)
	count = 0
	string = prune(string)	 
	while '-' in string:
		string = prune(string)
		if len(string) < k:
			return 'Case #' + str(l + 1) + ': IMPOSSIBLE'
		if string.find('-') >= 0:
			index = string.find('-')
			if len(string) - index < k:
				index = index - (k - (len(string) - index))
			string = list(string)
			for i in range(index, index + k):
				if string[i] == '+':
					string[i] = '-'
				else:
					string[i] = '+'
			count += 1
			string = ''.join(string)
			#print('swap - ##  ' + string)
	#print 'final: ' + string
	return 'Case #' + str(l + 1) + ': ' + str(count)




def prune(string):
	ind = string.find('-')
	if ind >= 0 :
		return string[ind:]
	else:
		return string



start('A-large.in')


