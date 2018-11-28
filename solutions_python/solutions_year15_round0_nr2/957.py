def countPancakesAndDiners(d):
	numOfPancakes = 0
	numOfDiners = 0
	for y in xrange(0,d['a']):
		z = d['b'][y]
		if z > 0:
			numOfPancakes += z
			numOfDiners += 1
	return [numOfPancakes, numOfDiners]

# Open file
f = open('input.in', 'r')

# t = number of cases
t = int(f.readline())
print 'Number of cases = ', t

# d = dictionary to hold input
d = {}

# Read in Input to Dictionary
for x in xrange(1,t+1):
	d[x] = {}
	# Line 1 = Number of non empty plates
	d[x]['a'] = int(f.readline())
	# Line 2 = Number of pancakes on their plates
	d[x]['b'] = [int(item) for item in f.readline().split()]
	d[x]['b'].sort(reverse=True)

# Close input file
f.close()
# Open output file
f = open('output.txt','w')
numOfOptimized = 0
for x in d:
	a = d[x]['a']
	b = list(d[x]['b'])
	#print a, b
	maxTime = b[0]
	optimizedTime = maxTime
	optimalInt = 2
	numOfMinues = 0
	c = []
	for y in xrange(2,maxTime):
		b = list(d[x]['b'])
		numOfMinutes = y
		while(b[0] > y):
			b[0] -= y
			b.append(y)
			b.sort(reverse=True)
			numOfMinutes += 1
		if numOfMinutes < optimizedTime:
			c = list(b)
			optimizedTime = numOfMinutes
			optimalInt = y
	#print c
	#print 'OptimizedTime = ' + str(optimizedTime)
	#print 'OptimalInt = ' + str(optimalInt)
	outStr = 'Case #' + str(x) + ': ' + str(optimizedTime) 
	print 'Max Time = ' + str(maxTime)
	print outStr
	f.write(outStr + '\n')
#print numOfOptimized
f.close()
