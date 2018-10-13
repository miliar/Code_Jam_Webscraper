import sys

class node:
	def __init__(self, color, num):
		self.time = 0
		self.color = color
		self.num = num
		self.parents = []

dict = {}

def F(vertex):
	if(vertex in dict):
		return dict[vertex]
	max = 0
	for v in vertex.parents:
		if v.color == vertex.color:
			if max < F(v) + abs(v.num - vertex.num) + 1:
				max = F(v) + abs(v.num - vertex.num) +1
		else:
			if max < F(v) + 1:
				max = F(v) + 1
#	vertex.time = max
#	if not vertex in vertices:
#		vertices.append(vertex)
	dict[vertex] = max
	return max



def read_input(filename):
	try:
		fp = open(filename)
	except IOError:
		print "Error opening or reading input file: ", filename
		sys.exit()
	# Convert the input into words	
	numInputs = int(fp.readline())
	arrays = []
	for i in range(numInputs):
		nextLineContents = fp.readline().split()
		arrays.append(nextLineContents)
	return arrays




def makeGraph(array):
	nodes = []
	numNodes = array.pop(0)
	lastBlue = node('B', 1)
	lastOrange = node('O', 1)
	newNode = None
	while len(array) != 0:
		nextColor = array.pop(0)
		nextNum = array.pop(0)
		newNode = node(nextColor, int(nextNum))
		
		newNode.parents.append(lastBlue)
		newNode.parents.append(lastOrange)
		
		if newNode.color == 'B':
			lastBlue = newNode
		else:
			lastOrange = newNode
	return newNode



arrays = read_input('/Users/Arash/Documents/codejam/input.txt')
#print arrays

vertices= []
outputs = []
for array in arrays:
	dest = makeGraph(array)
	#print 'dest: ',  dest.color, dest.num
	outputs.append(F(dest))

for vertex in vertices: 
	pass
	#print 'vertex: ', vertex.color, vertex.num ,
	#print 'time: ', vertex.time,
	#print '   parents: ',
	for vert in vertex.parents:
		pass
	#	print '   ', vert.color, vert.num,
	#print 

for i in range(len(outputs)):
	print 'Case #', '\b', i+1, ':', outputs[i]














