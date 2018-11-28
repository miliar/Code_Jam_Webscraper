import fractions

c = int(raw_input().strip())
c_index = 1
while c_index <= c:
	line = raw_input().strip().split(' ')
	numListSize = int(line[0])
	line = line[1:]
	numList = [int(num) for num in line]
	difList = list()
	i = 0
	while i < numListSize - 1:
		j = i + 1
		while j < numListSize:
			difList.append(abs(numList[i] - numList[j]))
			j = j + 1
		i = i + 1
	difListSize = len(difList)
	i = 1
	gcdVal = difList[0]
	while i < difListSize:
		gcdVal = fractions.gcd(gcdVal, difList[i])
		i = i + 1
	d, v = divmod(numList[0], gcdVal)
	if v != 0:
		d = d + 1
		
	print "Case #%d: %d" % (c_index, (gcdVal * d) - numList[0])
	c_index = c_index + 1

