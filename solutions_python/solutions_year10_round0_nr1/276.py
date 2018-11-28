'''
Codejam template

@author: alarobric
'''

def solve():
	n, k = [int(z) for z in infile.readline().split()]
	print "N, K:", n, k
	x = pow(2,n)
	num = x-1
	print num, x
	while (num < k):
		num += x
		
	if (num == k):
		return "ON"
	else:
		return "OFF"

filepath = '/home/alan/Downloads/'
fileprefix = 'A-large' #Change me!

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
