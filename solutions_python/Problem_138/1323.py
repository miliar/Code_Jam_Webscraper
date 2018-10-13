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

def remove(l, e):
	for element in l:
		if element == e:
			l.remove(element)
			break

def checkN(n, num):
	for i in n:
		if i > num : return i
	return None

data = []

filename = 'test.in'
filename = 'D-small-attempt0.in'
filename = 'D-large.in'

f = open(filename)

index = readindex(f)

for i in range(0, index):
	pieces = int(readindex(f))
	#deceitful war
	n = sorted([float(x) for x in f.readline().strip().split(' ')])
	k = sorted([float(x) for x in f.readline().strip().split(' ')])

	#war
	n2 = list(n)
	k2 = list(k)

	#deceitful war
	np1 = 0
	kp1 = 0

	#war
	np2 = 0
	kp2 = 0

	while len(n) > 0:
		a = checkN(n, min(k))
		if a != None:
			remove(k, min(k))
			remove(n, a)
			np1 += 1
		else:
			remove(k, min(k))
			remove(n, min(n))
			kp1 += 1
		if max(n2) > max(k2):
			remove(n2, max(n2))
			remove(k2, min(k2))
			np2 += 1
		else:
			remove(n2, max(n2))
			remove(k2, max(k2))
			kp2 += 1

	print 'Case #' + str(i + 1) + ': ' + str(np1) + ' ' + str(np2)
