import sys
import string

def getline():
	return sys.stdin.readline()[:-1]
def testcase():
	line = getline()
	args = line.split(' ')
	m = int(args[0])
	s = int(args[1])
	r = int(args[2])
	t = float(args[3])
	n = int(args[4])
	speed = {}
	belt = 0
	output = 0.0
	for i in range(n):
		line = getline()
		args = line.split(' ')
		b = int(args[0])
		e = int(args[1])
		w = int(args[2])
		belt += e - b
		if not w in speed:
			speed[w] = 0
		speed[w] += e - b
	speed[0] = m - belt
	u = speed.keys()
	u.sort()
	for key in u:
		if t == 0:
			output += speed[key] / (0.0 + key + s)
			continue
		req = speed[key] / (0.0 + key + r)
		if t - req > 0:
			output += req
			t -= req
		else:
			output += t
			output += (speed[key] - t * (key + r)) / (0.0 + key + s)
			t = 0
	return output

n = int(getline())
for i in range(n):
	print('Case #{0}: {1}'.format(i+1, testcase()))
