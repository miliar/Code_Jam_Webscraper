# Eric Montijo
# Google Code Jam qualification round 4/7/2017
import queue

# Open input/output files
#fin = open('C-small-input-test.txt','r')
fin = open('C-small-1-attempt0.in','r')
#fin = open('C-large.in','r')
fout = open('output.txt','w')
num_inputs = int(fin.readline())

for i in range (0, num_inputs): # Visit each input
	strInput = fin.readline().rstrip()
	outputLine = "Case #" + str(i+1) + ": "
	
	[numStalls, numPeople] = strInput.split(" ")
	(numStalls, numPeople) = (int(numStalls), int(numPeople))
	
	# List of groups of consecutive stalls, ordered by largest to smallest
	stallGroupList = queue.PriorityQueue()
	stallGroupList.put((-numStalls, numStalls))
	
	# min(Ls, Rs) where Ls+Rs = N will always be largest where N is as large as possible and
	#   Ls and Rs are equal/off by one, so the person will always split the largest group of
	#   empty stalls in half
	
	# Each person, one at a time
	leftSpace = 0
	rightSpace = 0
	for j in range(0, numPeople):
		(_, largestGroup) = stallGroupList.get()
		largestGroup -= 1 # new person
		if(largestGroup % 2 == 1): # odd num: left/right sides are off by one
			rightSpace = int(largestGroup/2)
			leftSpace = rightSpace + 1
		else: # even sum: left/right sides are equal
			leftSpace = int(largestGroup/2)
			rightSpace = int(leftSpace)
		# add new groups to the group list
		stallGroupList.put((-leftSpace, leftSpace))
		stallGroupList.put((-rightSpace, rightSpace))
	
	outputLine += str(leftSpace) + " " + str(rightSpace)
	
	#print(outputLine)
	fout.write(outputLine + '\n')

fin.close()
fout.close()
