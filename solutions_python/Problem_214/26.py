ds = "LRUD"
d2l = {"L": "-", "R": "-", "U": "|", "D": "|"}
l2d = {"-": "LR", "|": "UD"}
no = {"-": "|", "|": "-"}
chi = {"L": 0, "R": 0, "U": -1, "D": 1}
chj = {"L": -1, "R": 1, "U": 0, "D": 0}
chd = {"/": {"L": "D", "R": "U", "U": "R", "D": "L"}, "\\": {"L": "U", "R": "D", "U": "L", "D": "R"}}

def traverse(i, j, d):
	while True:
		i += chi[d]
		j += chj[d]
		if i < 0 or i >= r or j < 0 or j >= c:
			return ("B", 0, 0, d)
		elif ls[i][j] in "#-|":
			return (ls[i][j], i, j, d)
		elif ls[i][j] in chd:
			d = chd[ls[i][j]][d]

def traverseTrue(i, j, d):
	global psbs, unlit, esq
	while True:
		i += chi[d]
		j += chj[d]
		if i < 0 or i >= r or j < 0 or j >= c or ls[i][j] == "#":
			return
		elif ls[i][j] == "." and psbs[i][j] != True:
			psbs[i][j] = True
			unlit -= 1
			if (i, j) in esq:
				esq.remove((i, j))

def traverseFalse(i, j, d):
	global psbs, esq
	fi = i
	fj = j
	fo = no[ls[i][j]]
	while True:
		i += chi[d]
		j += chj[d]
		if i < 0 or i >= r or j < 0 or j >= c or ls[i][j] == "#":
			return
		elif ls[i][j] == "." and psbs[i][j] != True and (fi, fj, fo) in psbs[i][j]:
			psbs[i][j].remove((fi, fj, fo))
			l = len(psbs[i][j])
			if l == 0:
				raise UnicodeError
			elif l == 1:
				esq.add((i, j))

def doSet(i, j, o, poped = False):
	global ls, bs
	ls[i][j] = o
	if not poped:
		bs.remove((i, j))
	for d in l2d[o]:
		traverseTrue(i, j, d)
	for d in l2d[no[o]]:
		traverseFalse(i, j, d)

def fillMap():
	global ls, bs, psbs, unlit, esq
	estmp = []
	bs = set()
	psbs = [[None] * c for i in range(r)]
	for i in range(r):
		for j in range(c):
			if ls[i][j] == ".":
				estmp.append((i, j))
			elif ls[i][j] in "-|":
				dirs = ""
				for d in ds:
					res = traverse(i, j, d)[0]
					if res in "B#":
						dirs += d
				psbs[i][j] = ""
				if "L" in dirs and "R" in dirs:
					psbs[i][j] += "-"
				if "U" in dirs and "D" in dirs:
					psbs[i][j] += "|"
				l = len(psbs[i][j])
				if l == 0:
					return False
				elif l == 1:
					ls[i][j] = psbs[i][j]
				else:
					bs.add((i, j))
	esq = set()
	unlit = 0
	for i, j in estmp:
		psbs[i][j] = set()
		for d in ds:
			res = traverse(i, j, d)
			if res[0] in "-|":
				if (res[1], res[2]) in bs:
					if (res[1], res[2], d2l[res[3]]) not in psbs[i][j]:
						psbs[i][j].add((res[1], res[2], d2l[res[3]]))
				elif ls[res[1]][res[2]] == d2l[res[3]]:
					psbs[i][j] = True
					break
		if psbs[i][j] != True:
			l = len(psbs[i][j])
			if l == 0:
				return False
			elif l == 1:
				esq.add((i, j))
			unlit += 1
	try:
		while True:
			while esq:
				i, j = esq.pop()
				ti, tj, to = psbs[i][j].pop()
				psbs[i][j] = True
				unlit -= 1
				doSet(ti, tj, to)
			if unlit > 0:
				i, j = bs.pop()
				doSet(i, j, "-", True)
			else:
				return True
	except UnicodeError:
		return False
			
for t in range(int(input())):
	r, c = (int(i) for i in input().split())
	ls = [list(input()) for i in range(r)]
	pos = fillMap()
	if pos:
		print("Case #%d: POSSIBLE" % (t + 1))
		for l in ls:
			print("".join(l))
	else:
		print("Case #%d: IMPOSSIBLE" % (t + 1))
	