import sys
sys.stdin = open("water.in","r")
sys.stdout = open("water.out","w")
al = [ chr(i) for i in range(ord('a'),ord('z')+1) ]
class amap:
	def __init__(self,_map,size):
		self._map = _map
		self._size = size
		self._cover = [ [ None for i in range(size[1]) ] for j in range(size[0]) ]
		self._basin = 0
	def cell(self,x,y):
		if x < 0 or y < 0:
			return None
		if x >= self._size[0] or y >= self._size[1]:
			return None
		return self._map[x][y]
	def flow(self,x,y):
		global al
		if self.cell(x,y) == None:
			return None
		if self._cover[x][y]:
			#print "%d,%d is connected to %s" % (x,y,self._cover[x][y])
			return self._cover[x][y]
		n = [ self.cell(x-1,y) , self.cell(x,y-1) , self.cell(x,y+1), self.cell(x+1,y)]
		m = 0
		for i in range(1,4):
			if ( n[i] < n[m] and n[i] != None ) or n[m] == None:
				m = i
		#print "From %d %d min is %s" % ( x,y,["North","West","East","South"][m] )
		if n[m] == None or n[m] >= self.cell(x,y):
			#print "Covering %d %d with %s" % (x,y,al[self._basin])
			self._cover[x][y] = al[self._basin]
			self._basin+=1
		else:
			nx,ny = 0,0
			if m == 0:
				nx=x-1
				ny=y
			if m == 1:
				nx=x
				ny=y-1
			if m == 2:
				nx=x
				ny=y+1
			if m == 3:
				nx=x+1
				ny=y
			self._cover[x][y] = self.flow(nx,ny)
			#print "Covering %d %d with %s" % (x,y,self._cover[x][y])
		return self._cover[x][y]
	def write(self):
		for i in range(self._size[0]):
			for j in range(self._size[1]):
				self.flow(i,j)
		for i in range(self._size[0]):
			for j in range(self._size[1]):
				print self._cover[i][j],
			print

t = int(raw_input())
for i in range(t):
	mm = {}
	line = raw_input().split()
	h,w = int(line[0]),int(line[1])
	for j in range(h):
		line = raw_input().split()
		mm[j] = {}
		for k in range(w):
			mm[j][k] = int(line[k])
	# got a map into mm with size ( h,w )
	x = amap(mm,(h,w))
	print "Case #%d:\n" % (i+1),
	x.write()
sys.stdout.close()