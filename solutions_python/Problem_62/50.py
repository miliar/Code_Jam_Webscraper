'''
Codejam template

@author: alarobric
'''


def solve():
	print
	global n, m
	n = int(infile.readline())
	print "n", n
	wires = []
	for i in range(n):
		wires.append([int(z) for z in infile.readline().split()])
	#print wires
	
	crossings = 0
	#for each wire, test if it intersects with any wires after it (n log n?)
	for i in range(n):
		for j in range(i+1, n):
			#print i, j
			if wires[j][0] < wires[i][0] and wires[j][1] > wires[i][1]:
				crossings += 1
			elif wires[j][0] > wires[i][0] and wires[j][1] < wires[i][1]:
				crossings += 1
			#else no intersection
	return crossings


filepath = '/home/alan/Downloads/'
fileprefix = 'A-test' #Change me!
fileprefix = 'A-small-attempt0'
fileprefix = 'A-large'

infilename = filepath + fileprefix + '.in'
outfilename = filepath + fileprefix + '.out'
infile = open(infilename, 'rU')
outfile = open(outfilename, 'w+')

numCases = int(infile.readline())
print numCases

for case in range(1, numCases+1):
	str = "Case #%d: %s" %(case, solve())
	print str
	outfile.write(str + "\n")

infile.close()
outfile.close()
