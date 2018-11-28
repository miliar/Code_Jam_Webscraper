

for case in xrange(input()):
	N = int(input())
	naomi = map(float, raw_input().split(' '))
	ken = map(float, raw_input().split(' '))

	sol_y = 0
	sol_z = 0

	na = naomi[:]
	na.sort()
	ke = ken[:]
	ke.sort()
#	for n in na:
#		print '%0.5f' % (n),
#	print ''
#	for k in ke:
#		print '%0.5f' % (k),
#	print ''
	for i in xrange(N-1, -1, -1):
		if (na[i] > ke[i]):
			sol_z += 1
			na.pop(i)
			ke.pop(0)
		else:
			na.pop(i)
			ke.pop(i)

	na = naomi[:]
	na.sort()
	ke = ken[:]
	ke.sort()
	for i in xrange(N-1, -1, -1):
		if (na[i] > ke[i]):
			na.pop(i)
			ke.pop(i)
			sol_y += 1
		else:
			na.pop(0)
			ke.pop(i)

	print 'Case #%d: %d %d' % ((case+1), sol_y, sol_z)

