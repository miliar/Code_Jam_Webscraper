import re
filename = "A-large"
input = []
with open(filename + ".in") as f:
	for line in f:
		input.append(line)
		
LDN = input[0].split()
input[0:1] = []
wordLength = int(LDN[0])
numWords = int(LDN[1])
numCases = int(LDN[2])

# So we have a list of words, and a list of permutations.  
# let's define the list of words.
Words = [] #input[0:numWords]
for word in input[0:numWords]:
	Words.append(word.strip('\n'))
input[0:numWords] = []
print 'there are {0} words, they are: {1}'.format(numWords, Words)

# let's grab the cases
Cases = []
for case in input:
	Cases.append(case)
	
print 'There are {0} cases, they are: {1}'.format(numCases, Cases)

output = open(filename + ".out", "w")

counter = 1

for case in Cases:
	# all we need to do is transform the query, and do a match over all dictionarywords.
	case = case.strip('\n')
	case = case.replace('(','[')
	case = case.replace(')',']')
	occurences = 0
	prog = re.compile(case)
	for word in Words:
		if prog.match(word) != None:
			occurences += 1
	
	result = 'Case #{0}: {1}'.format(counter, occurences)
	output.write(result + '\n')
	print result
	counter += 1
	
output.close()