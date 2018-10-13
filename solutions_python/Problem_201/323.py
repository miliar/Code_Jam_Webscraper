import sys

mem = {0:[], 1:[(1, 0, 0)], 2:[(1, 0, 1), (1, 0, 0)]}

def merge(ini, l1, l2):
	i, j = 0, 0
	occ = [ini]
	while i<len(l1) and j<len(l2):
		if l1[i][1] == l2[j][1]:
			if l1[i][2] == l2[j][2]:
				ntup = (l1[i][0] + l2[j][0], l1[i][1], l1[i][2])
				occ.append(ntup)
				i += 1
				j += 1
			elif l1[i][2] > l2[j][2]:
				occ.append(l1[i])
				i += 1
			else:
				occ.append(l2[j])
				j += 1
		elif l1[i][1] > l2[j][1]:
			occ.append(l1[i])
			i += 1
		else:
			occ.append(l2[j])
			j += 1
	while i<len(l1):
		occ.append(l1[i])
		i += 1
	while j<len(l2):
		occ.append(l2[j])
		j += 1
	return occ

def getlist(n):
	if n in mem.keys():
		return mem[n]
	mem[n] = merge((1, n/2-1+n%2, n/2), getlist(n/2-1+n%2), getlist(n/2))
	return mem[n]

def solve():
	n, nk = [int(x) for x in sys.stdin.readline().split()]
	# print(n, nk)
	occ = getlist(n)
	# print(occ)
	nk -= 1
	for x in occ:
		if nk < x[0]:
			break
		nk -= x[0]
	return x[1], x[2]

ntest = int(sys.stdin.readline())
for i in range(1, ntest+1):
	ans1, ans2 = solve()
	print("Case #%d: %d %d"%(i, ans2, ans1))