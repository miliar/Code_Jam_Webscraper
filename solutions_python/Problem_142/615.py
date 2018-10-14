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

def to_string(l):
	temp = []
	last = ''
	for i in l:
		if i != last:
			temp.append({'letter': i, 'count': 1})
		else:
			temp[len(temp) - 1]['count'] += 1
		last = i
	return temp
	
def match(a, b):
	a_str = to_string(a)
	b_str = to_string(b)
	diff = 0
	
	if len(a_str) != len(b_str) : return 'Fegla Won'
	
	for i in range(0, len(a_str)):
		if a_str[i]['letter'] != b_str[i]['letter']:
			return 'Fegla Won'
		else:
			diff += abs(a_str[i]['count'] - b_str[i]['count'])
	
	return str(diff)

def solve(f):
	cases = readindex(f)
	lines = []
	for i in range(0, cases):
		lines.append(f.readline().strip())

	a = lines[0]
	b = lines[1]
	
	result = match(a, b)
	return result

data = []

filename = 'test.in'
filename = 'A-small-attempt0.in'

f = open(filename)

index = readindex(f)

for i in range(0, index):
	print 'Case #' + str(i + 1) + ': ' + solve(f)
