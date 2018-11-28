from shlex import split


def hmcpi(item):
	rL = []
	for i in range(4):
		for j in range(4):
			if (item[1][item[0]-1][i] == item[3][item[2]-1][j]):
				rL.append(item[1][item[0]-1][i])
	return rL

data = open("A-small-attempt0.in", "r").read().split("\n")

nC = eval(data[0])
del(data[0])


rL = []

for i in xrange(0, len(data) - 1, 10):
	tL = []
	tL.append(eval(data[i]))
	tL.append([])
	for j in xrange(1,5,1):
		tL[1].append([ eval(num) for num in data[i+j].split(" ")])
	tL.append(eval(data[i+5]))	
	tL.append([])
	for j in xrange(6,10,1):
		tL[3].append([ eval(num) for num in data[i+j].split(" ")])

	if (len(hmcpi(tL)) == 0):
		rL.append("Case #" + str((i/10)+1) +  ": " + "Volunteer cheated!")
	elif (len(hmcpi(tL)) == 1):
		rL.append("Case #" + str((i/10)+1) +  ": " + str(hmcpi(tL)[0]))
	else:
		rL.append("Case #" + str((i/10)+1) +  ": " + "Bad magician!")
	
ans = open("qualaans.txt", "w+")
ans.write('\n'.join(rL))
ans.close()



