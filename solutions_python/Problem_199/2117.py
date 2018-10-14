import numpy as np

with open('in') as f:
	lines = f.readlines()

T = int(lines[0])

probs = list()
K = list()
for i in np.arange(1,T+1):
	line = lines[i].strip()
	line = line.split(' ')
	probs.append([1 if x == "+" else 0 for x in line[0]])
	K.append(int(line[1]))

t= 1
for a,b in zip(probs, K):
	count = 0
	pos = 0
	l = len(a)
	a = np.array(a)
	while pos < l - b + 1:
		if a[pos] == 0:
			a[pos:(pos + b)] = 1-a[pos:(pos+b)]
			count += 1
		pos+=1
	if 0 in a:
		print "Case #%s: IMPOSSIBLE"% t
	else:
		print "Case #%s: %s" %(t, count)
	t += 1
