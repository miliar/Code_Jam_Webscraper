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
	inputs = [int(x) for x in f.readline().strip().split(' ')]
	
	a = inputs[0]
	b = inputs[1]
	k = inputs[2]

	wins = 0
	nums = []
	#print inputs, a, b, k, max(a, b)
	for i in range(0, max(a, b)):
		nums.append(0)

	for i in range(0, a):
		for j in range(0, b):
			nums[i & j] += 1
	k1 = min(k, max(a, b))
	for i in range(0, k1):
		wins += nums[i]
	
	return str(wins)

data = []

filename = 'test.in'
filename = 'B-small-attempt0.in'
filename = 'B-small-attempt1.in'

f = open(filename)

index = readindex(f)

for i in range(0, index):
	print 'Case #' + str(i + 1) + ': ' + solve(f)
