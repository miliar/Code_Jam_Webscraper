# Eric Montijo
# Google Code Jam qualification round 4/7/2017

# Open input/output files
#fin = open('qB-small-input-test.txt','r')
#fin = open('B-small-attempt0.in','r')
fin = open('B-large.in','r')
fout = open('output.txt','w')
num_inputs = int(fin.readline())

for i in range (0, num_inputs): # Visit each input
	strInput = fin.readline().rstrip()
	outputLine = "Case #" + str(i+1) + ": "
	
	# Small input - brute force should work with no trouble, but for the large input,
	#    we need something more clever; counting down from 9.8E18 will take a while when the answer
	#    is clearly 8.99...E18
	
	# Break number into a list of digits
	digits = list(map(int, list(strInput)))
	
	# Find the first location where the number is not tidy
	prevDigit = digits[0] # Most recent digit
	prevDigitIndex = 0    # Index of last digit change
	for j in range(1, len(digits)):
		if(digits[j] < prevDigit): # Uh-oh!
			# To get the next lowest tidy number, decrease the last index of the curr digit by 1,
			#   and fill in everything after that with 9s
			digits[prevDigitIndex] -= 1
			for k in range(prevDigitIndex+1, len(digits)):
				digits[k] = 9
			break
		elif(digits[j] > prevDigit): # If digit increased, remember the new digit
			prevDigit = digits[j]
			prevDigitIndex = j

	outputLine += str(int("".join(str(n) for n in digits)))
	
	#print(outputLine)
	fout.write(outputLine + '\n')

fin.close()
fout.close()
