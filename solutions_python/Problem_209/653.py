from math import pi
import itertools
z = []
def calc(x):
	sum = 0
	for c,i in enumerate(x):
		if (c==0):
			sum+= i[-1]
		else:
			sum+= i[0]**2 - x[c-1][0]**2 + 2*i[0]*i[1]
	return sum
for lsadjlksd in range(int(input())):
	n,k = map(int, input().split())
	l = []
	for i in range(n):
		l.append(list(map(int, input().split())))
	for i in range(len(l)): l[i].append(l[i][0]**2 + 2*l[i][0]*l[i][1])
	x = list(itertools.combinations(l,k))
	x = [sorted(i,key = lambda x: x[0]) for i in x]
	y = []
	for i in x:
		y.append(calc(i))
	z.append(pi*max(y))
for c,i in enumerate(z): 
	print("Case #" + str(c+1) + ":", '{0:.9f}'.format(i))