
t = int(raw_input());


def g(z):
	l=len(z)/2
	if z[:1] == z[-1:][::-1]:
		return True
	return False
			
def f(x):
	x = x ** 0.5
	return g(str(int(x))) and int(x) == x


for i in xrange(1,t+1):
	count = 0
	list1 = raw_input()
	a, b = [int(k) for k in list1.split(' ')]
		
	for j in xrange(a,b+1):
		if f(j) and g(str(j)):
			count = count + 1

			
	print 'Case #' + str(i) + ': ' +  str(count)

