def solve(n, m, lawn):
	#minimum
	minimum = 100
	for i in range(n):
		for j in range(m):
			if lawn[i][j] < minimum:
				minimum = lawn[i][j]

	for k in range(minimum,101):
		#line and columns
		for i in range(n):
			for j in range(m):
				if lawn[i][j] == k:
					#check if column or row is complete
					rowOk = 1
					for r in range(n):
						if lawn[r][j] != k:
							rowOk = 0
							break
					columnOk = 1
					for c in range(m):
						if lawn[i][c] != k:
							columnOk = 0
							break
					if columnOk + rowOk == 0:
						return "NO"

		#increment
		for i in range(n):
			for j in range(m):
				if lawn[i][j] == k:
					lawn[i][j] = k+1

		#check finish
		el = lawn[0][0]
		count = 0
		for i in range(n):
			for j in range(m):
				if lawn[i][j] == el:
					count+=1
		if count == n*m:
			return "YES"


lines = [line.strip() for line in open('B-large.in.txt')]
nTest = int(lines[0])
lineDim = 1
n = int(lines[lineDim].split()[0])
m = int(lines[lineDim].split()[1])
start = lineDim + 1
end = start + n
for i in range(nTest):
	lawn = []
	for j in range(n):
		row = lines[start:end][j].split()
		for k in range(len(row)):
			row[k] = int(row[k])
		lawn.append(row)
	print "Case #" + str(i+1) + ": " + solve(n, m, lawn)
	if i == nTest - 1:
		break
	lineDim = end
	n = int(lines[lineDim].split()[0])
	m = int(lines[lineDim].split()[1])
	start = lineDim + 1
	end = start + n


