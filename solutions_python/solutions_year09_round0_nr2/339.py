f = open("B-large.in")
T = int(f.readline().strip("\n"))
maps = []

for t in range(T):
	H, W = map(int, f.readline().strip("\n").split(" "))
	m = []
	for row in range(H):
		m.append(map(int, f.readline().strip("\n").split(" ")))
	maps.append(m)
	
#print maps

class Node:
	def __init__(self, value, x=None, y=None):
		self.value = value
		self.sink = False
		self.letter = None
		self.x = x
		self.y = y
		self.from_node = []
		self.to_node = None
		
	def set_incoming(self, from_node):
		self.from_node.append(from_node)
	
	def set_outgoing(self, to_node):
		self.to_node = to_node
	
	def set_letter(self, letter):
		self.letter = letter
		
	def __str__(self):
		return "(%d,%d)" % (self.x, self.y)
	
	def is_sink(self):
		return self.sink
		

		
class GMap:
	def __init__(self, d_array):
		self.da = d_array #Numbers here
		self.na = [] # Node array
		self.w = 0
		self.h = 0
		self.sinks = []
		
		for i in range(len(self.da)):
			row_letters = []
			for j in range(len(self.da[i])):	
				n = Node(self.da[i][j], j, i)
				row_letters.append(n)
			self.na.append(row_letters)
			self.w = len(row_letters)
		self.h = len(self.na)
		
		#print "Height: ", self.h
		#print "Width: ", self.w
	

	def get_southern(self, n):
		if n.y < self.h - 1:
			return self.na[n.y+1][n.x]
		else:
			return None
		
		
	def get_northern(self, n):
		if n.y > 0:
			return self.na[n.y-1][n.x]
		else:
			return None
		
	
	def get_eastern(self, n):
		if n.x < self.w-1:
			return self.na[n.y][n.x+1]
		else:
			return None
		
	def get_western(self, n):
		if n.x > 0:
			return self.na[n.y][n.x-1]
		else:
			return None
		
	def scan_nodes(self):
		
		
		for y in range(self.h):
			for x in range(self.w):
				node = self.na[y][x] # Select node
				to_where = Node(10001)
				#print "Node (%d, %d): %d" % (y,x,node.value)
				#print self.get_northern(node)
				#print self.get_eastern(node)
				#print self.get_southern(node)
				#print self.get_western(node)
				
				# Go reverse so that North will override.
				try:
					# South
					neighbor = self.get_southern(node)
					if neighbor.value < node.value:
						to_where = neighbor
						#print "Tried south"
						#print "Goes to (%d, %d) : %d" % (to_where.x, to_where.y, to_where.value)
				except:
					pass
				
				try:
					# East
					neighbor = self.get_eastern(node)
					if neighbor.value < node.value and neighbor.value <= to_where.value:
						to_where = neighbor
						#print "Tried east"
						#print "Goes to (%d, %d) : %d" % (to_where.x, to_where.y, to_where.value)
				except:
					pass
				
				try:
					# West
					neighbor = self.get_western(node)
					if neighbor.value < node.value and neighbor.value <= to_where.value:
						to_where = neighbor
						#print "Tried west"
						#print "Goes to (%d, %d) : %d" % (to_where.x, to_where.y, to_where.value)
				except:
					pass
				
				try:
					# North
					neighbor = self.get_northern(node)
					if neighbor.value < node.value and neighbor.value <= to_where.value:
						to_where = neighbor
						#print "Tried north"
						#print "Goes to (%d, %d) : %d" % (to_where.x, to_where.y, to_where.value)
				except:
					pass
				
				if to_where.value == 10001:
					# This is a sink.
					node.sink = True
					self.sinks.append(node)
				
				else:
					#print "Goes to (%d, %d) : %d" % (to_where.x, to_where.y, to_where.value)
					#print
					node.set_outgoing(to_where)
					to_where.set_incoming(node)
					
	def show_directions(self):
		for y in range(self.h):
			for x in range(self.w):
				node = self.na[y][x] # Select node
				if not node.sink:
					print node.to_node,
				else:
					print "-----",
			print
	
	def start_labeling(self):
		character = "a"
		for y in range(self.h):
			for x in range(self.w):
				node = self.na[y][x]
				if not node.letter:
					self.label(node, character)
					character = chr(ord(character)+1)

	def label(self, node, letter):
		node.letter = letter
		if node.to_node and not node.to_node.letter:
			self.label(node.to_node, letter)
		for fn in node.from_node:
			if not fn.letter:
				self.label(fn, letter)
		#MULTIPLE FROMNODE!!!!!!!!
	def show_labels(self):
		for y in range(self.h):
			for x in range(self.w):
				node = self.na[y][x] # Select node
				print node.letter,
			print
	
	def print_labels(self, output):
		for y in range(self.h):
			for x in range(self.w):
				node = self.na[y][x] # Select node
				output.write("%c " % node.letter)
			output.write("\n")
gmaps = []
for m in maps:
	g = GMap(m)
	gmaps.append(g)


output = open("B-large.out", "w")
# From now on, we have an array, gmaps with maps in it. Each map has mxn array of Nodes.
i=1
for gmap in gmaps:
	#For each map:
	
	gmap.scan_nodes()
	gmap.start_labeling()
	output.write("Case #%d:\n" % i)
	gmap.print_labels(output)	
	i+=1
output.close()

