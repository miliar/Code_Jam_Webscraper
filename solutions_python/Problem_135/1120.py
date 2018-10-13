f = open('A-small-attempt2.in', 'r')
numTest = int(f.readline())
print numTest

fAns = open('ansQ1.txt', 'w')

for i in range(numTest):
	firstAns = int(f.readline())
	
	for j in range(4):
		if j == firstAns - 1:
			firstLine = f.readline().strip().split()
			#print first_line
		else:
			f.readline()
	secondAns = int(f.readline())
	for j in range(4):
		if j == secondAns - 1:
			secondLine = f.readline().strip().split()
		else:
			f.readline()
	findAns = list(set(firstLine).intersection(secondLine))
	if len(findAns) == 1:
		
		fAns.write('Case #'+str(i + 1) + ': ' + str(findAns[0]) + '\n')
	elif len(findAns) > 1:
		fAns.write('Case #'+str(i + 1) + ': Bad magician!\n')
	elif len(findAns) == 0:
		fAns.write('Case #'+str(i + 1) + ': Volunteer cheated!\n')
fAns.close()
f.close()