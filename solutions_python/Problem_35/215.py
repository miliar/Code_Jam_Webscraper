import sys

f = sys.stdin

c = int(f.readline())
for c in range(1, c+1):
	l = f.readline()
	h, w = [int(s) for s in l.split()]
	m = []
	for i in range(h):
		l = f.readline()
		m.append([int(s) for s in l.split()])

	sl = []
	for i in range(h):
		for j in range(w):
			if (i<1 or m[i][j]<=m[i-1][j]) and (j<1 or m[i][j]<=m[i][j-1]) and (j>=w-1 or m[i][j]<=m[i][j+1]) and (i>=h-1 or m[i][j]<=m[i+1][j]):
				sl.append((i, j))

	sd = {}
	for s in sl:
		l = sd[s] = [s]
		i = 0
		while i < len(l):
			p = l[i]
			if (p[0]>0 and m[p[0]][p[1]]<m[p[0]-1][p[1]]):
				pc = (p[0]-1, p[1])
				if (pc[0]>0 and m[p[0]][p[1]]>=m[pc[0]-1][pc[1]]) or (pc[1]>0 and m[p[0]][p[1]]>=m[pc[0]][pc[1]-1]) or (pc[1]<w-1 and m[p[0]][p[1]]>=m[pc[0]][pc[1]+1]):
					pass
				else:
					l.append(pc)
			if (p[1]>0 and m[p[0]][p[1]]<m[p[0]][p[1]-1]):
				pc = (p[0], p[1]-1)
				if (pc[0]>0 and m[p[0]][p[1]]>=m[pc[0]-1][pc[1]]) or (pc[1]>0 and m[p[0]][p[1]]>=m[pc[0]][pc[1]-1]) or (pc[0]<h-1 and m[p[0]][p[1]]>m[pc[0]+1][pc[1]]):
					pass
				else:
					l.append(pc)
			if (p[1]<w-1 and m[p[0]][p[1]]<m[p[0]][p[1]+1]):
				pc = (p[0], p[1]+1)
				if (pc[0]>0 and m[p[0]][p[1]]>=m[pc[0]-1][pc[1]]) or (pc[1]<w-1 and m[p[0]][p[1]]>m[pc[0]][pc[1]+1]) or (pc[0]<h-1 and m[p[0]][p[1]]>m[pc[0]+1][pc[1]]):
					pass
				else:
					l.append(pc)
			if (p[0]<h-1 and m[p[0]][p[1]]<m[p[0]+1][p[1]]):
				pc = (p[0]+1, p[1])
				if (pc[1]>0 and m[p[0]][p[1]]>m[pc[0]][pc[1]-1]) or (pc[1]<w-1 and m[p[0]][p[1]]>m[pc[0]][pc[1]+1]) or (pc[0]<h-1 and m[p[0]][p[1]]>m[pc[0]+1][pc[1]]):
					pass
				else:
					l.append(pc)
			i += 1

	r = []
	for i in range(h):
		l = []
		for j in range(w):
			l.append(0)
		r.append(l)

	ca = ord('a')
	for i in range(h):
		for j in range(w):
			if r[i][j] == 0:
				for l in sd.items():
					if (i, j) in l[1]:
						for s in l[1]:
							r[s[0]][s[1]] = chr(ca)
						ca += 1
						del sd[l[0]]
						break

	print "Case #%s:" % c
	for i in range(h):
		print ' '.join([str(s) for s in r[i]])

