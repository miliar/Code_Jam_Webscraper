import sys

def solve(rowA, gridA, rowB, gridB):

	cnt = 0
	num = 0
	for i in range(4):
		if gridA[rowA-1][i] in gridB[rowB-1]:
			cnt += 1
			num = gridA[rowA-1][i]

	if cnt == 1:
		return num
	elif cnt > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"


res = []
with open(sys.argv[1], 'r') as fin:
	caseNo = int(fin.readline())

	for i in range(caseNo):
		rA = int(fin.readline())

		gA = []
		for j in range(4):
			gA.append([int(k) for k in fin.readline().split(' ')])

		rB = int(fin.readline())
		
		gB = []
		for j in range(4):
			gB.append([int(k) for k in fin.readline().split(' ')])

		res.append(solve(rA, gA, rB, gB))


with open(sys.argv[1] + ".out", 'w') as fout:
	for i in range(len(res)):
		fout.write("Case #" + str(i+1) + ": " + str(res[i]) + "\r\n")
