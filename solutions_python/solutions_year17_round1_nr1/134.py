
f = open('alarge.in')
fout = open('alarge.out', 'w')

numCases = int(f.readline().strip())


def ok1(bd, target, f, t, c):
	for i in range(f, t+1):
		if bd[target][i] not in (c, '?'):
			return False

	return True

def ok2(bd, target, f, t, c):
	for i in range(f, t+1):
		if bd[i][target] not in (c, '?'):
			return False

	return True

def hasQ(bd):
	for l in bd:
		if '?' in l:
			return True

	return False

def fill1(bd, target, f, t, c):
	for i in range(f, t+1):
		bd[target][i] = c

def fill2(bd, target, f, t, c):
	for i in range(f, t+1):
		bd[i][target] = c

for numCase in range(numCases):
	ss = f.readline().strip().split(' ')
	R = int(ss[0])
	C = int(ss[1])

	ll = []
	for i in range(R):
		ll.append(f.readline().strip())

	bd = []
	for i in range(R):
		l = ll[i]
		bd.append([])
		for c in l:
			bd[i].append(c)

	cmap = {}
	for i in range(R):
		for j in range(C):
			c = bd[i][j]
			if c == '?':
				continue

			if c not in cmap:
				cmap[c] = [i,j, i,j]
			else:
				if i < cmap[c][0]:
					cmap[c][0] = i
				if i > cmap[c][2]:
					cmap[c][2] = i
				if j < cmap[c][1]:
					cmap[c][1] = j
				if j > cmap[c][3]:
					cmap[c][3] = j

	while hasQ(bd) == True:
		changed = False
		for c in cmap:
			pos = cmap[c]


			target = pos[2] + 1
			while target < R and ok1(bd, target, pos[1], pos[3], c):
				fill1(bd, target, pos[1], pos[3], c)
				pos[2] = target
				target += 1
				changed = True

			target = pos[0] - 1
			while target >= 0 and ok1(bd, target, pos[1], pos[3], c):
				fill1(bd, target, pos[1], pos[3], c)
				pos[0] = target
				target -= 1
				changed = True

		for c in cmap:
			pos = cmap[c]
			target = pos[3] + 1

			while target < C and ok2(bd, target, pos[0], pos[2], c):
				fill2(bd, target, pos[0], pos[2], c)
				pos[3] = target
				target += 1
				changed = True

			target = pos[1] - 1
			while target >= 0 and ok2(bd, target, pos[0], pos[2], c):
				fill2(bd, target, pos[0], pos[2], c)
				pos[1] = target
				target -= 1
				changed = True


		if changed == False:
			break

	if hasQ(bd) == False:
		fout.write('Case #{}:\n'.format(numCase + 1))
		for l in bd:
			fout.write('{}\n'.format(''.join(l)))
		continue


	bd = []
	for i in range(R):
		l = ll[i]
		bd.append([])
		for c in l:
			bd[i].append(c)

	cmap = {}
	for i in range(R):
		for j in range(C):
			c = bd[i][j]
			if c == '?':
				continue
			if c not in cmap:
				cmap[c] = [i,j, i,j]
			else:
				if i < cmap[c][0]:
					cmap[c][0] = i
				if i > cmap[c][2]:
					cmap[c][2] = i
				if j < cmap[c][1]:
					cmap[c][1] = j
				if j > cmap[c][3]:
					cmap[c][3] = j

	while hasQ(bd) == True:
		changed = False

		for c in cmap:
			pos = cmap[c]
			print pos, c
			target = pos[1] - 1
			while target >= 0 and ok2(bd, target, pos[0], pos[2], c):
				fill2(bd, target, pos[0], pos[2], c)
				pos[1] = target
				print c, target
				target -= 1
				changed = True

			target = pos[3] + 1
			while target < C and ok2(bd, target, pos[0], pos[2], c):
				fill2(bd, target, pos[0], pos[2], c)
				pos[3] = target
				print c, target
				target += 1
				changed = True

		for c in cmap:
			pos = cmap[c]
			target = pos[0] - 1
			while target >= 0 and ok1(bd, target, pos[1], pos[3], c):
				fill1(bd, target, pos[1], pos[3], c)
				pos[0] = target
				target -= 1
				changed = True

			target = pos[2] + 1
			while target < R and ok1(bd, target, pos[1], pos[3], c):
				fill1(bd, target, pos[1], pos[3], c)
				pos[2] = target
				target += 1
				changed = True

		if changed == False:
			break
		fout.write('Case #{}:\n'.format(numCase + 1))
		for l in bd:
			fout.write('{}\n'.format(''.join(l)))



fout.close()

"""
Input 
 	
Output 
 
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE

Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE

"""

