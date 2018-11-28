a = input()
for j in range(a) :
	b = map(int,raw_input().split(' '))
	l = []
	for i in range(b[1]) :
		c = map(int,raw_input().split(' '))
		l.append(float(b[0]-c[0])/float(c[1]))
	k = max(l)
	z = float(b[0])/float(k)
	print 'Case #'+str(j+1)+':',
	print("%.6f" % z)

