def solve(cake):
	for i in range(len(cake)):
		for j in range(len(cake[i])):
			cur = cake[i][j]
			if i != 0 and cake[i-1][j] == cur:
				continue
			if j != 0 and cur == cake[i][j-1]:
				continue
			if cur == '?':
				continue
			cornery = i
			cornerx = j
			for cy in range(i, len(cake)):
				if (cake[cy][j] == cur):
					cornery = cy
				else:
					break
			for cx in range(j, len(cake[i])):
				if (cake[cornery][cx] == cur):
					cornerx = cx
				else:
					break
			#print("Expanding right...", cur, j, i, cornerx, cornery)
			cake = expandRight(cake, cur, j, i, cornerx, cornery)
			
			for cy in range(i, len(cake)):
				if (cake[cy][j] == cur):
					cornery = cy
				else:
					break
			for cx in range(j, len(cake[i])):
				if (cake[cornery][cx] == cur):
					cornerx = cx
				else:
					break
					
			cake = expandLeft(cake, cur, j, i, cornerx, cornery)
			
			
			for cy in range(i, len(cake)):
				if (cake[cy][j] == cur):
					cornery = cy
				else:
					break
			for cx in range(j, -1, -1):
				if (cake[cornery][cx] == cur):
					j = cx
				else:
					break
					
			cake = expandUp(cake, cur, j, i, cornerx, cornery)
			
			for cy in range(i, len(cake)):
				if (cake[cy][j] == cur):
					cornery = cy
				else:
					break
			for cx in range(j, len(cake[i])):
				if (cake[cornery][cx] == cur):
					cornerx = cx
				else:
					break
			cake = expandDown(cake, cur, j, i, cornerx, cornery)
			
			
	return cake

def expandRight(cake, symbol, fromx, fromy, tox, toy):
	minX = min(fromx, tox)
	minY = min(fromy, toy)
	maxX = max(fromx, tox)
	maxY = max(fromy, toy)
	
	if maxX == len(cake[0]) - 1:
		return cake
		
	for i in range(maxX+1, len(cake[0])):
		for j in range(minY, maxY+1):
			if cake[j][i] != '?':
				return cake
		cake = fillCake(cake, symbol, i, minY, i, maxY)
		#print("Filling cake...", i, minY, i, maxY)
		#printCake(cake)
	return cake

def expandLeft(cake, symbol, fromx, fromy, tox, toy):
	minX = min(fromx, tox)
	minY = min(fromy, toy)
	maxX = max(fromx, tox)
	maxY = max(fromy, toy)
	
	if minX == 0:
		return cake
		
	for i in range(minX-1, -1, -1):
		for j in range(minY, maxY+1):
			if cake[j][i] != '?':
				return cake
		cake = fillCake(cake, symbol, i, minY, i, maxY)
	return cake

def expandUp(cake, symbol, fromx, fromy, tox, toy):
	minX = min(fromx, tox)
	minY = min(fromy, toy)
	maxX = max(fromx, tox)
	maxY = max(fromy, toy)
	
	if minY == 0:
		return cake
		
	for i in range(minY-1, -1, -1):
		for j in range(minX, maxX+1):
			if cake[i][j] != '?':
				return cake
		cake = fillCake(cake, symbol, minX, i, maxX, i)
		#print("Filling cake...", i, minY, i, maxY)
		#printCake(cake)
	return cake	

def expandDown(cake, symbol, fromx, fromy, tox, toy):
	minX = min(fromx, tox)
	minY = min(fromy, toy)
	maxX = max(fromx, tox)
	maxY = max(fromy, toy)
	
	if maxY == len(cake) - 1:
		return cake
		
	for i in range(maxY+1, len(cake)):
		for j in range(minX, maxX+1):
			if cake[i][j] != '?':
				return cake
		cake = fillCake(cake, symbol, minX, i, maxX, i)
		#print("Filling cake...", i, minY, i, maxY)
		#printCake(cake)
	return cake
	
def fillCake(cake, symbol, fromx, fromy, tox, toy):
	minX = min(fromx, tox)
	minY = min(fromy, toy)
	maxX = max(fromx, tox)
	maxY = max(fromy, toy)
	
	for i in range(minY, maxY+1):
		for j in range(minX, maxX+1):
			cake[i][j] = symbol
	return cake
	
def main():
	f = open("A-large.in", "r")

	numCases = int(f.readline())

	for g in range(numCases):
		#parse line
		line = f.readline().split(' ')
		R = int(line[0])
		C = int(line[1])
		cake = [[0 for x in range(C)] for y in range(R)]
		leftCorners = dict()
		for i in range (R):
			row = f.readline()
			for j in range(C):
				cake[i][j] = row[j]
				if row[j] != '?' and row[j] not in leftCorners:
					leftCorners[row[j]] = (i, j)
				elif row[j] != '?' and row[j] in leftCorners:
					corner1 = leftCorners[row[j]]
					cake = fillCake(cake, row[j], j, i, corner1[1], corner1[0])
						
		#solve
		#print result
		print("Case #", g+1, ":", sep='')
		cake = solve(cake)
		printCake(cake)
		
def printCake(cake):
	for i in range (len(cake)):
		for j in range(len(cake[i])):
			print(cake[i][j], end='', sep='')
		print()

main()