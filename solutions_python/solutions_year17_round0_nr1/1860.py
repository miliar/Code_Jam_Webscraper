# Rahul Butani
# April 8th, 2017

# Takes a character; either '-' or '+'
# Returns the other character
def flip(pancake):
	return '-' if pancake is '+' else '+'

# Takes a string of '-'s and '+'s of length S followed by K (space separated)
# Returns the number of flips required or IMPOSSIBLE as a string
def probA(testCase):
	(In, K) = testCase.split(' ')
	In = list(In)
	K  = int(K)
	S  = len(In)

	#print("{} {}".format("".join(In), K))

	Idx   = 0
	Count = 0

	while Idx <= (S - K):
		# If we encounter an unhappy pancake...
		if In[Idx] is '-':
			Count += 1
			
			# ...flips the next K pancakes.
			for i in range(K):
				In[Idx+i] = flip(In[Idx+i])
		Idx += 1

	# Check the last K-1 pancakes to see if they're happy
	# Anything prior to K-1 will be happy since it's been the index previously
	for i in range(K):
		#print("Checking {}: {}".format((S - K + i),In[S - K + i]))
		if In[S - K + i] is '-':
			return "IMPOSSIBLE"

	return "{}".format(Count)
	
testCases = list()

with open('A-large.in', 'r', encoding='utf-8') as input:
	numCases = int(input.readline());
	print("Found {} cases.".format(numCases))

	for i in range(numCases):
		testCases.append(input.readline())

with open('A-large.out', 'w') as output:
	count = 0
	for test in testCases:
		count += 1

		out = "Case #{}: {}".format(count, probA(test))
		
		print(out)
		output.write(out + '\n')