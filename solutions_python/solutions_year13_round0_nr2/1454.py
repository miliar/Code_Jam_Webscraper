
fr = open("B-small-attempt0.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()
curTest = 0
curLine = 1

def testGrid(grid, h, w):
	for row in range(w):
		for col in range(h):
			testVal = grid[col][row]
			success = True
			for i in range(w):
				if grid[col][i] > testVal:
					success = False
					break
					
			if success:
				continue

			for i in range(h):
				if grid[i][row] > testVal:
					return False
	return True

while curTest < int(numTests):
	h, w = lines[curLine].strip().split()
	
	curLine += 1
	
	grid = []
	for i in range(int(h)):
		grid.append(lines[curLine].strip().split())
		curLine += 1
		
	curTest += 1
	
	if testGrid(grid, int(h), int(w)):
		print "Case #%d: %s" % (curTest, "YES")
		fw.write("Case #%d: %s\n" % (curTest, "YES"))
	else:
		print "Case #%d: %s" % (curTest, "NO")
		fw.write("Case #%d: %s\n" % (curTest, "NO"))
					
fr.close()
fw.close()