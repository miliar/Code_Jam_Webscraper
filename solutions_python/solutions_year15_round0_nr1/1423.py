# Open file
f = open('input.in', 'r')

# t = number of cases
t = int(f.readline())
print 'Number of cases = ', t

# d = dictionary to hold input
d = {}

# Read in Input to Dictionary
for x in xrange(1,t+1):
	d[x] = f.readline().split()

# Close input file
f.close()

# Open output file
f = open('output.txt','w')

print d

for x in d:
	sMax = int(d[x][0])
	numStanding = int(d[x][1][0])
	numNeeded = 0
	for y in xrange(1,sMax+1):
		s = int(d[x][1][y])
		if numStanding < y:
			numNeeded += (y-numStanding)
			numStanding += s + (y-numStanding)
		else:
			numStanding += s
	outStr = 'Case #' + str(x) + ': ' + str(numNeeded) 
	print outStr
	f.write(outStr + '\n')

f.close()