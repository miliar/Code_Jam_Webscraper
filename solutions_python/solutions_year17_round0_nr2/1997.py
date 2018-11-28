# Rahul Butani
# April 8th, 2017

# Takes N a string.
# Returns last tidy number in a string.
def probC(testCase):
	# Get N, the number Tatiana will count until.
	N = int(testCase)
	count = 0

	print("{}".format(N))

	# Essentially, while we still have digits left...
	while( int(N // (10 ** (count + 1))) ):
		# Current digit at count:
		digit = int(N // (10 ** (count + 0))) % (10)
		# Next digit (is to be <= current):
		nextD = int(N // (10 ** (count + 1))) % (10)

		#print("{},{} | {},{}".format(count,N,digit,nextD))

		# Check if this digit needs to be adjusted:
		if digit is 0 or nextD > digit:
			# If so, turn it and all following digits into 9s
			#print("Subtracting {} + 1".format(((N % (10 ** count)))))
			N -= ((N % (10 ** (count+1))) + 1) #((digit + 1) * (10 ** count))

		# Move to the next digit, rinse, and repeat
		count += 1

	return "{}".format(N)
	
testCases = list()

with open('B-large.in', 'r', encoding='utf-8') as input:
	numCases = int(input.readline());
	print("Found {} cases.".format(numCases))

	for i in range(numCases):
		testCases.append(input.readline())

with open('B-large.out', 'w') as output:
	count = 0
	for test in testCases:
		count += 1

		out = "Case #{}: {}".format(count, probC(test))
		
		print(out)
		output.write(out + '\n')