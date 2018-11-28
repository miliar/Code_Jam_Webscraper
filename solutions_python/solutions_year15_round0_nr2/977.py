fileIn = 'B-small-attempt7.in'
fileOut = 'output.txt'

f = open(fileOut, 'w')

def minutes(x):
	minutes = [max(x)]
	for i in range(2,max(x)):
		y = x[:]
		count = 0
		while max(y) > i:
			m = max(y)
			y.remove(m)
			y.append(m - i)
			count += 1

		minutes.append(i + count)
	# print x, min(minutes)
	return min(minutes)

lines = []
samples = None;
case = 1;
with open(fileIn, 'r') as f1: 
	for line in f1:
		if not samples:
			samples = [int(x) for x in line.split()]
		else:
			lines.append([int(x) for x in line.split()])
			if len(lines) == 2:
				f.write("Case #" + str(case) + ": "+ str(minutes(lines[1])) + "\n")
				lines = []
				case += 1


f.close()
