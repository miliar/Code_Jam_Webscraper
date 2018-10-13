import sys

f = open(sys.argv[1])
T = int(f.readline())

def readFloats():
	return list(map(float, f.readline().strip().split(' ')))

for t in range(T):
	floats = readFloats()
	C = floats[0]
	F = floats[1]
	X = floats[2]
	
	total = X / 2.0
	N = 1
	while True:
		velocity = 2.0
		times = []
		for n in range(N):
			times.append(C / velocity)
			velocity += F
			
		newTotal = X / velocity + sum(times)
		if total > newTotal:
			total = newTotal
			N += 1
		else:
			break
	
	print 'Case #%d:' % (t + 1), total
