# Eric Montijo
# Google Code Jam qualification round 4/7/2017

# Open input/output files
#fin = open('qA-small-input-test.txt','r')
#fin = open('A-small-attempt1.in','r')
fin = open('A-large.in','r')
fout = open('output.txt','w')
num_inputs = int(fin.readline())

for i in range (0, num_inputs): # Visit each input
	strInput = fin.readline().rstrip()
	
	# Decipher input
	pancakes = list(strInput[:strInput.find(" ")])
	spatulaSize = int(strInput[strInput.find(" ")+1:])
	
	outputLine = "Case #" + str(i+1) + ": "
	
	# Travel from left to right.  Each time we find a -, we must flip that pancake (and those to
	#    its right).  If we reach the end and there are still unflipped pancakes, there's nothing
	# we can do to fix it - IMPOSSIBLE.
	numFlips = 0
	for j in range(0, len(pancakes)-spatulaSize+1):
		if(pancakes[j] == '-'): # Need to flip
			numFlips += 1
			#print("Before flipping at ", i, ":", pancakes)
			for k in range(j, j+spatulaSize): # Flip pancakes based on spatula size
				pancakes[k] = ('+' if pancakes[k] == '-' else '-')
			#print("After flipping:", pancakes)
	
	for j in range(len(pancakes)-spatulaSize+1, len(pancakes)):
		if(pancakes[j] == "-"): # We don't have space to flip!
			outputLine += "IMPOSSIBLE"
			break
	else: # The remaining pancakes are happy
		outputLine += str(numFlips)
	
	#print(outputLine)
	fout.write(outputLine + '\n')

fin.close()
fout.close()
