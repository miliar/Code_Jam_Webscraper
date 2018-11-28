


data = [line.strip() for line in open("A-small-attempt0.in", 'r')] #change file name
x = int(data.pop(0))
count = 0
while data != []:
	count += 1
	case = data[:11]
	data = data[10:]
	case = [line.split() for line in case]
	val1 = int(case[0][0])
	val2 = int(case[5][0])
	res = []
	for elem in case[val1]:
		if elem in case[val2+5]: res.append(elem)
	if len(res)==1: print "Case #" + str(count) + ": " + res[0]
	if len(res)>1: print "Case #" + str(count) + ": Bad magician!"
	if res==[]: print "Case #" + str(count) +": Volunteer cheated!"

