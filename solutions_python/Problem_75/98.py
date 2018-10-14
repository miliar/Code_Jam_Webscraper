from collections import defaultdict
input = open("Magicka.in")
output = open("Magicka.out", "w")
T = int(input.readline())
for t in range(T):
	line = input.readline()[:-1]
	line = line.split(" ")
	C = int(line[0])
	c = line[1:C + 1]
	combine = defaultdict(dict)
	for i in c:
		combine[i[0]][i[1]] = i[2]
		combine[i[1]][i[0]] = i[2]
	line = line[C + 1:]
	
	D = int(line[0])
	d = line[1:D + 1]
	opposed = defaultdict(list)
	for i in d:
		opposed[i[0]].append(i[1])
		opposed[i[1]].append(i[0])
	line = line[D + 1:]
	
	string = line[1]
	result = [None]
	for s in string:
		if s in combine[result[-1]] and combine[result[-1]][s]:
			result[-1] = combine[result[-1]][s]
		else:
			for o in opposed[s]:
				if o in result:
					result = [None]
					break
			else:
				result.append(s)
	print("Case #{case}: {result}".format(case = t + 1, result = str(result[1:]).replace("'", "")), file = output)
output.close()
