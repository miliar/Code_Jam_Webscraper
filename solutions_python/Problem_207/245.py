import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

cnt_tests = int(input())



for test in range(cnt_tests):
	_pre = 'Case #%d:' % (test + 1)
	n, R, RY, Y, YB, B, RB = map(int, input().split())
	if RB * 2 > Y or RY * 2 > B or YB * 2 > R:
		print(_pre, 'IMPOSSIBLE')
		continue
	can = True
	ys = []
	rs = []
	bs = []

	for i in range(RB):
		ys.append('YVY')

	for i in range(Y - RB * 2):
		ys.append('Y')

	for i in range(YB):
		rs.append('RGR')

	for i in range(R - YB * 2):
		rs.append('R')

	for i in range(RY):
		bs.append('BOB')

	for i in range(B - RY * 2):
		bs.append('B')


	# print(ys)
	# print(rs)
	# print(bs)


	Y = len(ys)
	R = len(rs)
	B = len(bs)
	n = len(ys) + len(rs) + len(bs)
	rez = [None] * n
	def check(i, t):
		if rez[i]:
			return False
		elif rez[(i + 1) % n] and rez[(i + 1) % n][0] == t[0]:
			return False
		elif rez[(i - 1) % n] and rez[(i - 1) % n][0] == t[0]:
			return False
		return True

	all = [ys, rs, bs]
	all.sort(key=lambda x: len(x))

	rez[0] = all[-1].pop()

	def key(x):
		if not x: return (0, 0)
		return (len(x), x[0] == rez[0])

	for i in range(1, n):
		all.sort(key=key)
		if all[-1][-1] == rez[i - 1]:
			if not all[-2]:
				print(_pre, 'IMPOSSIBLE')
				can = False
				break
			rez[i] = all[-2].pop()
		else:
			rez[i] = all[-1].pop()

	if not can: continue

	for i in range(n):
		if rez[i][0] == rez[(i - 1) % n] or rez[i][0] == rez[(i + 1) % n]:
			print(_pre, 'IMPOSSIBLE')
			can = False
			break
	if not can: continue
	print(_pre, ''.join(rez))
		



	
