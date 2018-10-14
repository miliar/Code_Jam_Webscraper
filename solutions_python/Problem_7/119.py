
def getNumTri(vertices):
	val = 0
	for i in range(0, len(vertices)):
		for j in range(i + 1, len(vertices)):
			for k in range( j + 1, len(vertices)):
				if (vertices[i][0] + vertices[j][0] + vertices[k][0]) % 3 == 0 and (vertices[i][1] + vertices[j][1] + vertices[k][1]) % 3== 0:
					#center = ((vertices[i][0] + vertices[j][0] + vertices[k][0]) / 3, (vertices[i][1] + vertices[j][1] + vertices[k][1]) / 3)
					val += 1
	return val

def getInput(f):
	n, A, B, C, D, x0, y0, M = [int(i) for i in f.readline().strip().split(' ')] 
	x, y = x0, y0
	vertices = [(x, y)]
	#print x,y
	for i in range(0, n - 1):
		x = (A * x + B) % M
		y = (C * y + D) % M
		vertices.append((x,y))
		#print x, y
	return vertices
	
if __name__ =="__main__":
	infile = open('A-small-attempt0.in', 'r')
	numCases = int(infile.readline().strip())
	for i in range(1, numCases + 1):
		print "Case #%s: %s" % (i, getNumTri(getInput(infile)))
