import sys

if not len(sys.argv):
	print '[>] No input file'
	sys.exit()
input = open(sys.argv[1], 'r+')
T = int(input.readline())
for t in range(1, T+1):
	C = input.readline().split()
	Smax = int(C[0])
	shyness = []
	for i in range(0, Smax+1):
		shyness.append(int(C[1][i]))
	# print 'Smax:', Smax
	# print 'Shyness:', shyness

	a = shyness[0]
	invites = 0
	for i in range(1, Smax+1):
		if (a < i) and shyness[i]:
			invites += (i-a)
			a += (i-a)		
		a += shyness[i]
	print 'Case #{}: {}'.format(t, invites)
