import fileinput

l=0
fLine = -1
sLine = -1
problem = []
problem2 = []
case = 1
nProblems = -1
for line in fileinput.input():
	if l==0:
		nProblems = int(line)
		l+=1
		continue
	if l==1:	
		fLine = int(line)
	elif l < 6:
		problem.append([int(li) for li in line.split() if li != '\n'])
	elif l==6:
		sLine = int(line)
	elif l < 11:
		problem2.append([int(li) for li in line.split() if li != '\n']) 
	else:
		interU = set(problem[fLine-1]).intersection(set(problem2[sLine-1]))
		if len(interU) == 1:
			print "Case #"+str(case)+": "+str(interU.pop())
		elif len(interU) > 1:
			print "Case #"+str(case)+": Bad magician!"
		else:
			print "Case #"+str(case)+": Volunteer cheated!"
		l=1
		case+=1
		problem = []
		problem2 = []
		fLine = int(line)
	l+=1

interU = set(problem[fLine-1]).intersection(set(problem2[sLine-1]))
if len(interU) == 1:
	print "Case #"+str(case)+": "+str(interU.pop())
elif len(interU) > 1:
	print "Case #"+str(case)+": Bad magician!"
else:
	print "Case #"+str(case)+": Volunteer cheated!"