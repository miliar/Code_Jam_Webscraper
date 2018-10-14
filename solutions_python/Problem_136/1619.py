file = open('input.txt')
n = int(file.next())

for i in range(1,n+1):
	vals = map(float, file.next().split(' '))
	C = vals[0]
	F = vals[1]
	X = vals[2]
	rate = 2.0
	minimum = X/rate
	while True:
		rate += F
		temp = X/rate
		temp_rate = 2
		while temp_rate < rate:
			temp += C/temp_rate
			temp_rate += F
		
		if temp < minimum: minimum = temp
		else: break
	
	print 'Case #%s: %.7f' % (i, minimum)
		