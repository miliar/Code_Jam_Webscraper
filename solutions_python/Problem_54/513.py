'''
Codejam template

@author: alarobric
'''

def solve():
	events = [int(z) for z in infile.readline().split()]
	n = events.pop(0)
	#print "n", n
	#print "events", events
	events.sort()
	
	diff = []
	for i in range(len(events)-1):
		diff.append(events[i+1] - events[i])
	
	factor = reduce(Gcf, diff)
	print "factor", factor
	if events[0] % factor == 0:
		return 0
	if (events[0] > factor):
		return factor - (events[0] % factor)
	else:
		return factor - (events[0] % factor)
	'''
	num = 0
	while num < events[0]:
		num += factor
	return num - events[0]'''

def Gcf(a, b):
	if b == 0:
		return a
	else:
		return Gcf(b, a % b)

filepath = '/home/alan/Downloads/'
fileprefix = 'B-large' #Change me!

infilename = filepath + fileprefix + '.in'
outfilename = filepath + fileprefix + '.out'
infile = open(infilename, 'rU')
outfile = open(outfilename, 'w+')

numCases = int(infile.readline())
print numCases

for case in range(1, numCases+1):
	str = "Case #%d: %d" %(case, solve())
	print str
	outfile.write(str + "\n")

infile.close()
outfile.close()
