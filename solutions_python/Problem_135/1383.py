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

def solve(f):
	global data
	
	line = f.readline().strip()
	index1 = int(line) - 1
	
	for i in range(0, 4):
		line = f.readline().strip().split(' ')
		if i == index1 : data.append(castToInt(line))
	
	line = f.readline().strip()
	index2 = int(line) - 1
	
	for i in range(0, 4):
		line = f.readline().strip().split(' ')
		if i == index2 : data.append(castToInt(line))
	
	result = list(set(data[0]) & set(data[1]))
	
	data = []
	
	if len(result) == 1 : return str(result[0])
	elif len(result) == 0 : return 'Volunteer cheated!'
	else : return 'Bad magician!'

data = []

filename = 'test.in'
filename = 'A-small-attempt0.in'

f = open(filename)

index = readindex(f)

for i in range(0, index):
	print 'Case #' + str(i + 1) + ': ' + solve(f)
