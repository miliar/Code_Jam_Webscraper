inName="B-large.in"
outName="out.txt"
tags = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class gMap:
	def __init__(self,width=0,height=0,mapNo=0):
		self.curTag=0
		self.mapNo=mapNo
		self.width=width
		self.height=height
		self.grid=[]
		self.labels=[]
		
		for i in xrange(0,self.height):
			self.grid.append([])
			self.labels.append([])
			for j in xrange(0,self.width):
				#self.grid[i].append(0)
				self.labels[i].append('-')
				
	def printMe(self):
		line = ""
		for i in xrange(self.height):
			for j in xrange(self.width):				
				line += str(self.grid[i][j]) + " "
			line += "\n"
		print line

	def getLabels(self):
		line = "Case #" + str(self.mapNo + 1) + ":\n"
		for i in xrange(self.height):
			for j in xrange(self.width):				
				line += self.labels[i][j] + " "
			line += "\n"
		return line
		
	def processCell(self,i,j):
		# if already labeled, don't process
		if(self.labels[i][j] != '-' ):
			return self.labels[i][j]
		
		dir='-'
		lowest = 10000		
		
		if( i<(self.height-1) and self.grid[i+1][j] <= lowest ):
			dir='S'
			lowest=self.grid[i+1][j]
		if( j<(self.width-1) and self.grid[i][j+1] <= lowest ):
			dir='E'
			lowest = self.grid[i][j+1]
		if( j>0 and self.grid[i][j-1] <= lowest ):
			dir='W'
			lowest = self.grid[i][j-1]
		if( i>0 and self.grid[i-1][j] <= lowest ):
			dir='N'
			lowest = self.grid[i-1][j]
			
		#determine if sink
		if( lowest >= self.grid[i][j] ):
			self.labels[i][j] = tags[self.curTag];
			self.curTag += 1
			return self.labels[i][j]
		else:
			if( dir=='S'):
				return self.processCell(i+1,j)
			elif( dir=='E' ):
				return self.processCell(i,j+1)
			elif( dir=='W' ):
				return self.processCell(i,j-1)
			else:
				return self.processCell(i-1,j)
				
	def processAll(self):
		for i in xrange(0,self.height):
			for j in xrange(0,self.width):
				if self.labels[i][j] == '-':
					self.labels[i][j] = self.processCell(i,j)
		
		
		
numMaps=0
curWidth=0
curHeight=0

mapList = []
# =============================================================================
# (STEP 1) LOAD ALL DATA
# =============================================================================
inFile = open(inName, 'r')
numMaps = map(int,inFile.readline().split())[0]

for i in xrange(0,numMaps):
	line = map(int,inFile.readline().split())
	m = gMap(line[1],line[0],i)
	
	#load each row of the map
	for j in xrange(m.height):
		 m.grid[j] = map(int,inFile.readline().split())
	
	mapList.append( m )

inFile.close()

# =============================================================================
#(STEP 2) PROCESS ALL DATA
# =============================================================================
for m in mapList:
	m.processAll()

# =============================================================================
#(STEP 3) OUTPUT ALL DATA
# =============================================================================
	outFile = open(outName,'w')
	for m in mapList:
		outFile.write(m.getLabels())
	outFile.close()
	


