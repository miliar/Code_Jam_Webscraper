import string

f=open(r'A_smallinput.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
for i in range(1, n+1) :
	line=f.readline()
	line=line.rstrip("\n\r ")
	t = line.translate(string.maketrans("ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz"))
	print 'Case #{0}: {1}'.format(i, t)
