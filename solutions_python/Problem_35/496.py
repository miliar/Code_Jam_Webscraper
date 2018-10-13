import sys
import string

height = 0
width = 0
inmap = []
outmap = []
stream = [] #keeps positions of current stream
counter = 0
alpha = map(chr, range(97, 123))

def findEmpty():
	for hi in range(height):
		for wi in range(width):
			if outmap[hi][wi] == "none":
				return (hi, wi)
	return 'DONE'

def getAlt(hi, wi):
	if (0 <= hi < height) and (0 <= wi < width):
		return inmap[hi][wi]
	else:
		return 20000

def findLow(hi, wi):
	north = getAlt(hi-1, wi)
	west =  getAlt(hi, wi-1)
	east = getAlt(hi, wi+1)
	south = getAlt(hi+1, wi)
	themin = min(north, west, east, south)
	if themin >= inmap[hi][wi]:
		return ('sink', hi, wi)
	if north == themin:
		return (hi-1, wi)
	if west == themin:
		return (hi, wi-1)
	if east == themin:
		return (hi, wi+1)
	if south == themin:
		return (hi+1, wi)
	
####################
fin = open(sys.argv[1])
out = open("waterout.txt", "w")

ncase = int(fin.readline())

for c in range(ncase):
	height = 0
	width = 0
	inmap = []
	outmap = []
	stream = [] #keeps positions of current stream
	counter = 0
	
	intro = "Case #%d:" % (c+1)
	#print intro
	out.write(intro+"\n")
	height, width = [int(x) for x in fin.readline().split()]
	
	# Make map
	for h in range(height):
		newRow = [int(x) for x in fin.readline().split() ] 
		inmap.append( newRow )
		outmap.append( ["none"]*len(newRow) )
	
	square = (0,0)
	while square != 'DONE':
		stream.append(square)
		thelow = findLow(square[0], square[1]) #square's low
		while thelow[0] != 'sink':
			stream.append(thelow)
			square = thelow
			thelow = findLow(square[0], square[1])
		#when thelow = 'sink'
		if outmap[thelow[1]][thelow[2]] == "none":
			letter = alpha[counter]
			counter +=1
		else: #hit a formal letter
			letter = outmap[thelow[1]][thelow[2]]
		for i in range(len(stream)):
			outmap[stream[i][0]][stream[i][1]] = letter
		stream = [] #reset stream
	
		square = findEmpty()
		
	#printing
	for h in range(height):
		row = string.join( outmap[h], ' ')
		#print row
		out.write(row+"\n")