x = open("B-small-attempt0.in","r")

def fails(lawn, i, j, maxi, maxj):
	for x in range(maxi):
		if lawn[x][j] == '2':
			for y in range(maxj):
				if lawn[i][y] == '2':
					return True
	return False

numYards = int(x.readline().strip())
for z in range(int(numYards)):
	xy = x.readline().strip().split()
	lawn = []
	for n in range(int(xy[0])):
		lawn.append(x.readline().strip().split())
		
	failed = False
	for i,r in enumerate(lawn):
		for j,e in enumerate(r):
			if e == '1' and fails(lawn, i, j, int(xy[0]), int(xy[1])):
				failed = True
				break
		if failed:
			break
	if failed:
		print("Case #" + str(z+1) + ": NO")
	else:
		print("Case #" + str(z+1) + ": YES")