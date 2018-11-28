
import sys
import numpy as np


def loadinput():
	def readintline(): return [int(x) for x in f.readline().split()]
	fn = sys.argv[1]
	f = open(fn,'r')
	T = int(f.readline())
	
	probs = []
	for i in range(T):
		H,W = readintline()
		map = []
		for rw in range(H):
			map.append(readintline())
		npmap = np.array(map)
		probs.append((H,W,npmap))
	
	return T,probs


# Algorithm:
# Run left to right from the top to the bottom of the map
# Trace down to the bottom
# If you hit a cell with a label, trace backwards and set that label

# Opt - fuse list construction/destruction

def listnext(map,rw,cl):
	dir = []

	def add_dir(nrw,ncl):
		#dir.append((nrw,ncl))
		if map[nrw,ncl] < map[rw,cl]:
			dir.append((nrw,ncl))

	if rw > 0:		# North
		add_dir(rw-1,cl)
	if cl > 0:		# West
		add_dir(rw,cl-1)
	if cl < len(map[0])-1:	# East
		add_dir(rw,cl+1)
	if rw < len(map)-1:	# South
		add_dir(rw+1,cl)
	
	return dir

def picknext(nextdirs,map):
	def getcell(idir):
		return map[nextdirs[idir][0],nextdirs[idir][1]]
	min = getcell(0)
	mini = 0
	for i in range(1,len(nextdirs)):
		if getcell(i) < min:
			min = getcell(i)
			mini = i

	return nextdirs[mini]



# North,west,east,south is order when tied
def trace(labels,map,rw,cl,label):
	# Exit case
	# If I'm already labelled, then you've run into a previously seen drain
	if labels[rw,cl] != 0: return labels[rw,cl]

	# Assign the label on the return trip

	# Generate list of possible next directions, ordered only by N,W,E,S
	nextdirs = listnext(map,rw,cl)

	if nextdirs == []:			# Hit a sink, return
		labels[rw,cl] = label
	else:						# Continue recursing
		# Pick the one that's most down hill
		nextrw,nextcl = picknext(nextdirs,map)

		# Trace down it, and get the label at the bottom
		label = trace(labels,map,nextrw,nextcl,label)

		labels[rw,cl] = label

	return label
	


# zero -> unlabeled
def solvemap((H,W,map)):
	labels = np.zeros((H,W),dtype='int')

	label = 1			# first label

	for rw in range(H):
		for cl in range(W):
			if labels[rw,cl] == 0:
				# newlabel will be different if we ran into and old drain basin
				newlabel = trace(labels,map,rw,cl,label)
				if newlabel == label:
					label += 1
	
	return labels

def solveall(T,probs):
	alph = 'abcdefghijklmnopqrstuvwxyz'

	def tochar(labels):
		return [[alph[i-1] for i in row] for row in labels]

	for i in range(T):
		print "Case #%d:"%(i+1)
		labels = solvemap(probs[i])
		clabels = tochar(labels)
		for rw in range(len(clabels)):
			print " ".join(clabels[rw])

T,probs = loadinput()
solveall(T,probs)
#h,w,m = probs[2]
