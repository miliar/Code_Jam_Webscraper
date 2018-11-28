from fractions import gcd
import sys

def time(l):
	l.sort()
	# compute the gcd of differences
	mul = l[1]-l[0]
	for i in range(2, len(l)):
		mul = gcd(mul, l[i]-l[i-1])
	d = l[0]%mul
	return 0 if d == 0 else mul-d

f = sys.argv[1]
fin = open(f)
fout = open(f.replace('in','out'), 'w')
C = int(fin.next())
for i in range(0, C):
	l = map(int, fin.next().split(' ')[1:])
	fout.write("Case #%d: %d\n"%(i+1, time(l)))
