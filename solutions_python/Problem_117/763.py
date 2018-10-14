#Lawnmower

def mowRows(lawn, target, N, M):
	for i in range(N):
		maxHeight = max(target[i])
		for j in range(M):
			if lawn[i][j] > maxHeight:
				lawn[i][j] = maxHeight

def mowColumns(lawn, target, N, M):
	for i in range(M):
		column = [0]*N
		for j in range(N):
			column[j] = target[j][i]
		maxHeight = max(column)
		for j in range(N):
			if lawn[j][i] > maxHeight:
				lawn[j][i] = maxHeight


	return
def mowLawn(lawn, target, N, M):
	mowRows(lawn, target, N, M)
	mowColumns(lawn, target, N, M)
	return

f = open("B-large.in")
o = open("Out.out", "w+")
T = f.readline()
for i in range(int(T)):
	target = []
	lawn = []
	dim = f.readline().split(' ')
	N = int(dim[0])
	M = int(dim[1])
	#initialize the lawn
	for n in range(N):
		lawn.append([100]*M)
	for j in range(N):
		row = f.readline().strip('\n').split(' ')
		target.append(row)
	for k in range(N):
		for l in range(M):
			target[k][l] = int(target[k][l])

	mowLawn(lawn, target, N, M)
	if (lawn == target):
		o.write("Case #" + str(i + 1) + ": YES\n")
		print("Case #" + str(i + 1) + ": YES")
	else:
		o.write("Case #" + str(i + 1) + ": NO\n")
		print("Case #" + str(i + 1) + ": NO")

