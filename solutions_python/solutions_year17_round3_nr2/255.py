from math import pi
import sys
sys.setrecursionlimit(1000*1001)

data = open('B-small-attempt1.in', 'r').readlines()
#data = open('B-large.in', 'r').readlines()
tn = int(data[0])
answ = []
dp = 1
for t in range(tn):
	n, m = data[dp].split()
	n, m = int(n), int(m)
	a, b = [], []
	for i in range(n):
		x, y = data[dp+i+1].split()
		a.append((int(x), int(y)))
	for i in range(m):
		x, y = data[dp+n+i+1].split()
		b.append((int(x), int(y)))
	dp += n + m + 1
	a.sort()
	b.sort()
	
	if n + m == 1:
		answ.append(2)
	elif n == 1 and m == 1:
		answ.append(2)
	else:
		if n == 2:
			if a[1][1] - a[0][0] <= 12*60 or (a[0][1] - a[1][0]) % (24*60) <= 12*60:
				answ.append(2)
			else:
				answ.append(4)
		else:
			if b[1][1] - b[0][0] <= 12*60 or (b[0][1] - b[1][0]) % (24*60) <= 12*60:
				answ.append(2)
			else:
				answ.append(4)

#with open('B-large.out', 'w') as f:
with open('B-small.out', 'w') as f:
    for i, o in enumerate(answ):
        f.write('Case #{}: {}\n'.format(i+1, o))
