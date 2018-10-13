def product(a,b):
	s = 0
	for i in range(len(a)):
		s += a[i]*b[i]
	return s
	
input  = file("A-large.in")
totalNumber = int(input.readline())
for i in range(totalNumber):
	n = int((input.readline()))
	v1 = input.readline().split()
	v2 = input.readline().split()
	v1 = map(int,v1)
	v2 = map(int,v2)
	v1.sort()
	v2.sort(reverse = True)
	
	print 'Case #%i: %s' % (i+1, product(v1,v2))
	
