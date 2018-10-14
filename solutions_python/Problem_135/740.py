"""
Written for Google Code Jam 2014
Kolijn Wolfaardt
kolijn.wolfaardt@gmail.com
"""

f = open('magic/A-small-attempt0.in','r')


#First, read the number of test cases
T = int(f.readline())

for t in range(T):

	#Read the line the card is in
	L1 = int (f.readline())-1 #stupid google, arrays start at 0
	for a in range(4):
		#The rest of the data is useless, read the line the card is in
		if (a==L1):
			line1 = [int(a) for a in f.readline().split()]
		else:
			f.readline()

	#Read the second line the card is in
	L2 = int (f.readline())-1
	for a in range(4):
		#The rest of the data is useless, read the line the card is in
		if (a==L2):
			line2 = [int(a) for a in f.readline().split()]
		else:
			f.readline()

	#Now we need to get the matches from each array
	#This will always be 2 arrays with 4 values, so lets just loop
	matching = []
	for i in range(4):
		for j in range(4):
			if line1[i] == line2[j]:
				matching.append(line1[i])

	if (len(matching)==1):
		print ("Case #{}: {}".format(t+1,matching[0]))
	if (len(matching)==0):
		print ("Case #{}: Volunteer cheated!".format(t+1))
	if (len(matching)>1):
		print ("Case #{}: Bad magician!".format(t+1))