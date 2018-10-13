import sys

def snaps(n, k):
	k += 1
	if k != 0:
		return k % (2 ** n) == 0
	return False

lines = file(sys.argv[1], 'r').readlines()

for i in range(1, int(lines[0].strip())+1):
	if not lines[i].strip():
		continue
	n, k = map(int, lines[i].strip().split(' '))
	
	print 'Case #%i: %s' % (i, 'ON' if snaps(n, k) else 'OFF')
