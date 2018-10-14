import sys
import math
t = int(sys.stdin.readline())
for i in range(0,t):
	line = sys.stdin.readline().split()
	r = int(line[0])
	k = int(line[1])
	n = int(line[2])
	line = sys.stdin.readline().split()
	total = 0
	g = [None]*n
	print 'Case #'+str(i+1)+':',
	for j in range(0,n):
		g[j] = int(line[j])
		total += g[j]
	if k >= total:
		print r*total
	else:
		flag = True
		tmp = [None]*n
		value = [None]*n
		tmp[0] = 0
		s = 0
		j = 0
		cur = 0
		while flag and j < r:
			total = 0
			x = tmp[s]
			while total<=k:
				total += g[x]
				x = (x+1)%n
			x = (x+n-1)%n
			total -= g[x]
			for p in range(0,s):
				if tmp[p] == x:
					flag = False
					break
			value[s] = total
			s += 1
			cur += total
			if flag:
				tmp[s] = x
			else:
				repeat = 0
				for l in range(p,s):
					repeat += value[l]
				cur += (r-s)/(s-p)*repeat
				rest = (r-s)%(s-p)
				for l in range(0,rest):
					cur += value[(p+l)%s]
			j += 1
		print cur
