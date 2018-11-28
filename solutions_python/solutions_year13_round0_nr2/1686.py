
r = open("B-small-attempt0.in", 'r')
w = open("B-small.out", 'w')

n = int(r.readline()) # num cases

def checkLawn(lawn, lw, lh):
	for y in range(lw):
		for x in range(lh):
			if lawn[x][y] == m:
				if sum(lawn[x]) != m*lw and sum([thing[y] for thing in lawn]) != m*lh:
					return False

	return True

for tc in range(n):
	dim = r.readline().strip().split()
	lh = int(dim[0])
	lw = int(dim[1])

	lawn = []

	m = 1000

	for i in range(lh):
		row = r.readline().strip().split()
		rowList = []

		for rs in row:
			ri = int(rs)
			m = min(m, ri)
			rowList.append(ri)

		lawn.append(rowList)

	w.write("Case #"+str(tc+1)+": ")
	if checkLawn(lawn, lw, lh):
		w.write("YES\n")
	else:
		w.write("NO\n")


r.close()
w.close()
