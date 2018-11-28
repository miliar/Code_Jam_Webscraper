def lookup(DICT, D, L, pattern):
	letters = []
	pattern = pattern.strip()
	unclosed = False
	cand = []
	for i in range(len(pattern)):
		if pattern[i].islower():
			cand.append(pattern[i])
		if pattern[i] == '(':
			unclosed = True
		if pattern[i] == ')':
			unclosed = False
		if not unclosed:
			letters.append(cand[:])
			cand = []
	count = 0
	# print 'Lookup', pattern
	# print letters
	for i in range(D):
		match = True
		for j in range(L):
			if DICT[i][j] not in letters[j]:
				match = False
				break
		if match:
			count += 1
	return count

class NODE:
	"""Nodes on 2D plane"""
	def __init__(self, h, w, a):
		self.h = h #row
		self.w = w #column
		self.a = a #altitude
		self.l = None #basin label
		self.p = [] #parents
		self.c = None #child
		
	def __str__(self):
		return "(%d,%d):%d"%(self.h+1, self.w+1, self.a)
	
	def __cmp__(self, o):
		if type(o)!=NODE:
			return -1
		diff = self.a - o.a #compare alt
		if diff == 0:
			diff2 = self.h - o.h #compare row
			if diff2 == 0:
				return self.w - o.w #compare col
			else:
				return diff2
		else:
			return diff

def FindMin(list):
	n = len(list)
	if n == 0:
		return None
	min = list[0]
	for i in range(1,n):
		o = list[i]
		if o.a < min.a:
			min=o
		if o.a == min.a:
			if o.h < min.h:
				min = o
			if o.h == min.h:
				if o.w < min.w:
					min = o
	return min
	
def MapVisit(map, H, W):
	for row in map:
		for node in row:
			#visit its neighbors
			r = node.h
			c = node.w
			cand = []
			# print 'Find', node
			if r-1>= 0:
				cand.append(map[r-1][c])
			if c-1>= 0:
				cand.append(map[r][c-1])
			if c+1< W:
				cand.append(map[r][c+1])
			if r+1< H:
				cand.append(map[r+1][c])
			# print '---'
			# for cd in cand:
				# print cd
			# print '---'
			mc = FindMin(cand) #select the one with min alt
			# print "Min:",mc
			if mc != None and mc.a < node.a:
				node.c = mc
				mc.p.append(node)
				# print "(%d,%d):%d->(%d,%d):%d"%(node.h+1,node.w+1,node.a, mc.h+1,mc.w+1, mc.a)

def MapDfs(node, label):
	node.l = label
	if node.c != None:
		MapDfs(node.c, label)
	for v in node.p:
		if v.l == None:
			MapDfs(v, label)

				
def MapLabel(map):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	idx = 0
	for row in map:
		for node in row:
			if node.l == None:
			# if node.c == None: # this is a basin
				# print node
				label = alphabet[idx]
				idx+=1
				MapDfs(node,label)

def PrintMap(map):
	for row in map:
		for node in row:
			print node.l,
		print ''


if __name__ == '__main__':
	INFILE = 'B-large.in'
	IN = open(INFILE)
	LINE = IN.readline()
	DATA = LINE.split()
	T = int(DATA[0]) #number of tests
	for i in range(T):
		LINE = IN.readline()
		DATA = LINE.split()
		H = int(DATA[0]) #height
		W = int(DATA[1]) #width
		MAP = []
		ROW = []
		#construct map
		for j in range(H):
			LINE = IN.readline()
			DATA = LINE.split()
			for k in range(W):
				alt = int(DATA[k])
				node = NODE(j,k,alt)
				ROW.append(node)
			MAP.append(ROW[:])
			ROW=[]
		MapVisit(MAP, H, W)
		MapLabel(MAP)
		print 'Case #%d:'%(i+1)
		PrintMap(MAP)
