import sys
f = sys.argv[1]
lines = open(f, 'r').readlines()



def non_sur(x):
	if x == 0:
		return 0
	if x % 3 == 0:
		return x / 3
	if x % 3 == 1:
		return x / 3 + 1
	if x % 3 == 2:
		return x / 3 + 1

def sur(x):
	if x == 0:
		return 0
	if x % 3 == 0:
		return x / 3 + 1
	if x % 3 == 1:
		return x / 3 + 1
	if x % 3 == 2:
		return x / 3 + 2


for i, line in enumerate(lines):
	if i == 0: continue
	data = map(int, line.split(' '))
	
	N, S, p, T = data[0], data[1], data[2], data[3:]
	
	c = 0
	for t in T:
		if non_sur(t) >= p:
			c += 1
		else:
			if S > 0:
				if sur(t) >= p:
					c += 1
					S -= 1
	
	print 'Case #%i: %i' %(i, c)


