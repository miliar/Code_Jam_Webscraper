from itertools import *

def max_tidy(s):
	for ch in s:
		a.append(int(ch))
	n = len(a) - 1
	#print a, n
	
	b = [a[0]]
	k = 1
	while (k < n + 1) and (a[k] >= a[k - 1]):
		b.append(a[k])
		k+= 1
		
	if k < n + 1:
		#print k
		for i in xrange(k, n + 1):
			b.append(9)
		i = k - 1
		while (i > 0) and (b[i] - 1 < b[i - 1]):
			b[i] = 9
			i -= 1
		b[i] = b[i] - 1			
	
	res = ""
	k = 0
	while (k <= n) and (b[k] == 0):
		k +=  1
	while (k <= n):
		res += str(b[k])
		k += 1		
	return res
		

inf = open("b.in", 'r')
outf = open("b.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	s = inf.readline().strip()
	a = []
	
	
	outf.write("Case #" + str(tc + 1) + ": ")	
	outf.write(max_tidy(s) + "\n")	
	
outf.close()
