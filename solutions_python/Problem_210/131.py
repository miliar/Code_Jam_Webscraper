import sys

def onesolve(xam):
	if len(xam) == 1:
		return 2
	xam = sorted(xam)
	if xam[1][0] - xam[0][1] >= 720:
		return 2
	if (xam[0][0] + 24*60) - xam[1][1] >= 720:
		return 2
	return 4

def solve(cam,jam):
	if len(cam) == 0:
		"""
		if min(j[0] for j in jam) >= 720 or max(j[1] for j in jam) <= 720:
			return 2
		"""
		return onesolve(jam)
	elif len(jam) == 0:
		"""
		if min(c[0] for c in cam) >= 720 or max(c[1] for c in cam) <= 720:
			return 2
		"""
		return onesolve(cam)
	else:
		return 2

T = int(input())
for case in range(T):
	Ac,Aj = map(int, input().split())
	cam = [list(map(int, input().split())) for _ in range(Ac)]
	jam = [list(map(int, input().split())) for _ in range(Aj)]
	op = "Case #{}: {}".format(case+1, solve(cam,jam))
	print(op)
	sys.stderr.write(op + "\n")
