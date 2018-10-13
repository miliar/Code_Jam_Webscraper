import sys
sys.setrecursionlimit(10000000)

def solveGood(naomi, ken):
	if len(namoi) == 0:
		return 0
	if namoi[0] > ken[0]:
		namoi.pop(0)
		ken.pop(0)
		return solveGood(namoi, ken) + 1
	else:
		namoi.pop(0)
		ken.pop(-1)
		return solveGood(namoi, ken)

def solveBad(namoi, ken):
	if len(namoi) == 0:
		return 0
	i = len(ken)-1
	while namoi[0] < ken[i] and i >= 0:
		i -= 1
	if i == -1:
		namoi.pop(0)
		ken.pop(0)
		return solveBad(namoi, ken)
	elif i == len(ken) - 1:
		namoi.pop(0)
		ken.pop(0)
		return solveBad(namoi, ken) + 1
	else:
		namoi.pop(0)
		ken.pop(i+1)
		return solveBad(namoi, ken)

for t in range(int(input())):
	input()
	namoi = sorted(float(s) for s in input().split(" "))
	ken = sorted(float(s) for s in input().split(" "))
	namoi1 = [f for f in namoi]
	ken1 = [f for f in ken]
	print("Case #" + str(t+1) + ": " + str(solveGood(namoi, ken)) + " " + str(solveBad(namoi1, ken1)))
