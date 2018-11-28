def test(x, row, col):
	if x < max(lawnRows[row]) and x < max(lawnColumns[col]):
		return False
	return True

def checkLevel(i):
	for row in range(n):
		for col in range(m):
			if lawnRows[row][col] == i:
				if(not test(i, row, col)):
					return False
	return True


f = open("input.txt")
o = open("output.txt", "w+")
for case in range(int(f.readline())):
	n, m = [int(x) for x in f.readline().split()]
	lawnRows = []
	lawnColumns = []
	for i in range(n):
		lawnRows.append([int(x) for x in f.readline().split()])
	
	for i in range(m):
		lawnColumns.append([x[i] for x in lawnRows])

	tallest = max([max(x) for x in lawnRows])
	shortest = min([min(x) for x in lawnRows])
	possible = True

	for i in range(tallest-1, shortest-1, -1):
		if(not checkLevel(i)):
			possible = False

	if possible:
		o.write("Case #" + str(case+1) + ": YES\n")
	else:
		o.write("Case #" + str(case+1) + ": NO\n")
o.close()
