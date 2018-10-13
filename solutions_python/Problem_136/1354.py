def readblock(f):
	line = f.readline().strip()
	cases = int(line)
	global data
	for i in range(0, cases):
		line = f.readline().strip()
		data.append(line.split(' '))

def readLineData(f):
	global data 
	data = f.readline().strip().split(' ')

def castToInt(l):
	return [int(float(x)) for x in l]

def castToFloat(l):
	return [float(x) for x in l]

def readindex(f):
	return int(f.readline().strip())

def solve(d):
	C = d[0]
	F = d[1]
	X = d[2]
	
	return int(X / C - 2 / F)

def calcTime(d, n):
	C = d[0]
	F = d[1]
	X = d[2]
	
	temp = 0
	for i in range(1, n + 1):
		temp += C / (2 + F * (i - 1))
	
	temp += X / (2 + F * n)
	return temp

data = []

filename = 'test.in'
filename = 'B-small-attempt0.in'
filename = 'B-large.in'

f = open(filename)

index = readindex(f)

for i in range(0, index):
	readLineData(f)
	data = castToFloat(data)

	n = solve(data)
	if n < 0 : n = 0

	time = calcTime(data, n)
	print 'Case #' + str(i + 1) + ': ' + str(time)
