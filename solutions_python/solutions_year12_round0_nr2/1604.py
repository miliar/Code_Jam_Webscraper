f = file("test.txt", "r")
fout = file("output.txt", "w")
input = f.read().split("\n");
myString = ""



tests = int(input[0]) 
case = 1

def surprising(lst):
	lst.sort()
	if max(lst) < 10 and lst[-2] > 0:
		lst[-1] += 1
		lst[-2] -= 1
		return lst
	else:
		return [0,0,0]

while case <= tests:

	line 			= input[case].split(" ")
	numOfGooglers 	= int(line[0])
	numOfSur 		= int(line[1])
	maxScore		= int(line[2])
	seq				= map(int, line[3:])
	
	maxMap = [None] * numOfGooglers
	maxSurMap = [None] * numOfGooglers
	i = 0
	while i < numOfGooglers:
		tmp = [seq[i]/3,]
		seq[i] -= seq[i]/3
		tmp.append(seq[i]/2)
		seq[i] -= seq[i]/2
		tmp.append(seq[i])
		maxMap[i] = max(tmp)
		maxSurMap[i] = max(surprising(tmp))
		i += 1

	j = 0
	i = 0
	print " Before: %s %s" % (maxMap, maxSurMap)
	while j < numOfSur and i < len(maxMap):
		m = maxSurMap[i]
		if m >=	maxScore and maxMap[i] < maxScore:
			maxMap[i] = m
			j += 1
		i += 1
	counter = 0
	print "After: %s %s" % (maxMap, maxSurMap)
	for i in maxMap:
		counter += i>=maxScore and 1
		
	myString += "Case #%d: %d\n" % (case, counter)
	case += 1





print(myString)
fout.write(myString)