'''
Codejam template

@author: alarobric
'''


def solve():
	print
	global n, m
	existing = []
	new = []
	n, m = [int(z) for z in infile.readline().split()]
	for i in range(n):
		existing.append(infile.readline().split()[0][1:])
	for i in range(m):
		new.append(infile.readline().split()[0][1:])
	print "n, m", n, m
	print existing
	print new

	root = node('root')
	for directory in existing:
		current = root
		for newWord in directory.split('/'):
			found = False
			for child in current.children:
				if child.name == newWord:
					current = child
					found = True
			if not found:
				current.children.append(node(newWord))
				current = current.children[len(current.children)-1]
				
	numInserts = 0
	
	for directory in new:
		current = root
		for newWord in directory.split('/'):
			found = False
			for child in current.children:
				if child.name == newWord:
					current = child
					found = True
			if not found:
				current.children.append(node(newWord))
				current = current.children[len(current.children)-1]
				numInserts += 1
	return numInserts
	
class node:
	def __init__(self, name):
		self.name = name
		self.children = []

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
