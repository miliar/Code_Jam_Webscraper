import numpy as np

with open('in') as f:
	lines = f.readlines()

T = int(lines[0])

K = list()
for i in np.arange(1,T+1):
	K.append(int(lines[i]))

def tidy(x):
	l = [int(i) for i in str(x)]
	rev = np.array(l[::-1])
	for i in np.arange(len(rev) - 1):
		if rev[i] < rev[i+1]:
			rev[0:(i+1)] = 9
			rev[i+1] -= 1
	return int(''.join(map(str,rev[::-1])))
	
for i, a in enumerate(K):
	print "Case #%s: %s" % (i+1, tidy(a))

