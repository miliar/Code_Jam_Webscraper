import psyco
psyco.full()

def whereFlow(mapa, i, j, H, W):
	minHeight = mapa[i][j]
	flowDir = (i, j)
	#North
	if i != 0:
		if mapa[i-1][j] < minHeight:
			minHeight = mapa[i-1][j]
			flowDir = (i-1, j)
	#West
	if j != 0:
		if mapa[i][j-1] < minHeight:
			minHeight = mapa[i][j-1]
			flowDir = (i, j-1)
	#East
	if j != W-1:
		if mapa[i][j+1] < minHeight:
			minHeight = mapa[i][j+1]
			flowDir = (i, j+1)
	#South
	if i != H-1:
		if mapa[i+1][j] < minHeight:
			minHeight = mapa[i+1][j]
			flowDir = (i+1, j)
	return flowDir

def isSink(mapa, i, j, H, W):
	flowDir = whereFlow(mapa, i, j, H, W)
	if flowDir == (i, j):
		return True
	return False

def replaceLabel(labels, oldC, newC):
	for i in range(H):
		for j in range(W):
			if labels[i][j] == newC:
				labels[i][j] = 'X'
			elif labels[i][j] == oldC:
				labels[i][j] = newC
	for i in range(H):
		for j in range(W):
			if labels[i][j] == 'X':
				labels[i][j] = oldC

def sortLabels(labels, H, W):
	Lnames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	Unames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	dictionar = {}
	currChar = 0
	for i in range(H):
		for j in range(W):
			if labels[i][j] not in dictionar.keys():
				dictionar[labels[i][j]] = Unames[currChar]
				currChar += 1
	for i in range(H):
		for j in range(W):
			labels[i][j] = dictionar[labels[i][j]].lower()

def labelSinks(mapa, labels, H, W):
	names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	currChar = 0
	for i in range(H):
		for j in range(W):
			if isSink(mapa, i, j, H, W):
				labels[i][j] = names[currChar]
				currChar += 1

def flow(mapa, labels, i, j, H, W):
	if labels[i][j] != ' ':
		return labels[i][j]
	flowDir = whereFlow(mapa, i, j, H, W)
	labels[i][j] = flow(mapa, labels, flowDir[0], flowDir[1], H, W)
	return labels[i][j]

data = open('maps.txt', 'r').read().split('\n')

T = int(data.pop(0))

for i in range(T):
	(H, W) = data.pop(0).split(' ')
	H = int(H)
	W = int(W)
	mapa = []
	labels = []
	for j in range(H):
		row = data.pop(0).split(' ')
		row = map(int, row)
		mapa.append(row)
		labels.append([' '] * W)
	
	labelSinks(mapa, labels, H, W)
	for j in range(H):
		for k in range(W):
			flow(mapa, labels, j, k, H, W)

	sortLabels(labels, H, W)
	
	print 'Case #' + str(i+1) + ':'
	for j in range(H):
		for k in range(W):
			print str(labels[j][k]),
		print ''
