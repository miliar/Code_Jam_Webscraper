import fileinput

lines = fileinput.input()
lines_i = 0

def read(conv=str, sep=None):
	global lines
	global lines_i
	line = lines[lines_i].strip()
	lines_i += 1
	if sep is None:
		return conv(line)
	else:
		return [conv(token) for token in line.split(sep)]


def solve(AC, AJ, NC, NJ):
	AC = sorted(AC)
	AJ = sorted(AJ)
	split = True
	if NC + NJ == 1:
		A = AC if NC == 1 else AJ
		if A[0][1] <= 12*60 or A[0][0] >= 12*60:
			return 2
		else:
			return 2
	elif NC + NJ == 2:
		if NC == 2 or NJ == 2:
			A = AC if NC == 2 else AJ
			if A[-1][1] <= 12*60 or A[0][0] >= 12*60:
				return 2
			elif A[-1][1] - A[0][0] <= 12*60:
				return 2
			elif A[0][1] + (24*60-A[-1][0]) <= 12*60:
				return 2
			else:
				return 4
		elif NC == 1 and NJ == 1:
			if (AC[0][1] <= 12*60 and AJ[0][0] >= 12*60) or (AJ[0][1] <= 12*60 and AC[0][0] >= 12*60):
				return 2
			else:
				return 2
	return 0

T = read(int)
for t in range(1, T + 1):
	NC, NJ = read(int, ' ')
	AC = [None] * NC
	AJ = [None] * NJ
	for i in range(NC):
		AC[i] = read(int, ' ')
	for i in range(NJ):
		AJ[i] = read(int, ' ')
	print("Case #{0}: {1}".format(t, solve(AC, AJ, NC, NJ)))
