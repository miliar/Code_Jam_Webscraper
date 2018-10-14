# Schuyler Smith
# 5/8/10

def gcd(a,b):
	while b != 0:
		a,b = b,a%b
	return a



infile = open("B-large.in", 'r')
outfile = open("B-large.out", 'w')

N = int(infile.next())

for n in xrange(1,N+1):
	line = infile.next().split(' ')
	num = int(line[0])
	events = []
	for i in xrange(num):
		events.append(int(line[i+1]))
	
	diffs = []
	for i in xrange(1,num):
		diffs.append(abs(events[i]-events[i-1]))
	
	if len(diffs)>1:
		step = gcd(diffs[0],diffs[1])
		for i in xrange(2,len(diffs)):
			step = gcd(step,diffs[i])
	else:
		step = diffs[0]
	
	outVal = (-events[0])%step
	print outVal
	outfile.write("Case #" + str(n) + ": " + str(outVal) + "\n")

infile.close()
outfile.close()
