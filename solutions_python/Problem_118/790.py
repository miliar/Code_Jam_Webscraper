
import math

def is_fair(n):
	m = str(n)
	l = len(m)
	for i in range(int(math.floor(l/2))):
		if m[i] != m[l-i-1]:
			return False
	return True

	
fin = open('c.in', 'r')
fout = open('c.out', 'w')

n = int(fin.readline().strip())

for i in range(1, n+1):
	a, b = fin.readline().strip().split(' ')
	aa = math.ceil(int(a)**(0.5))
	bb = math.floor(int(b)**(0.5))

	c = 0
	for j in range(int(aa), int(bb)+1):
		if is_fair(j) and is_fair(j*j):
			c += 1
	fout.write('Case #%d: %d\n' % (i, c))
	
fout.close()