
def token():
	return raw_input()
def tokens():
	return raw_input().strip().split()

def merge(ax, bx, cx):
	la, lb, lc = map(len, (ax, bx, cx))
	#print la, lb, lc
	# print ax, bx, cx
	res = [ax[i]+bx[i] for i in range(lb)]

	ld = la - lb
	res.extend([ax[lb + i]+cx[i] for i in range(ld)])
	for i in range(lc - ld):
		res[i] = res[i] + cx[ld + i]
	return ''.join(res)

def solve(N, R, O, Y, G, B, V):
	if not (G <= R and V <= Y and O <= B):
		return
	if G == R and G > 0:
		if N > G + R:
			return
		return 'GR' * G
	if V == Y and V > 0:
		if N > V + Y:
			return
		return 'VY' * V
	if O == B and O > 0:
		if N > O + B:
			return
		return 'OB' * O
	# G < R, V < Y, O < B
	r, y, b = R - G, Y - V, B - O
	if 2*max(r, y, b) > (r + y + b):
		return
	if r > 0:
		rs = ['R'] * (r-1)
		rs.append('R' + 'GR' * G)
	else:
		rs = []
	if y > 0:
		ys = ['Y'] * (y-1)
		ys.append('Y' + 'VY' * V)
	else:
		ys = []
	if b > 0:
		bs = ['B'] * (b-1)
		bs.append('B' + 'OB' * O)
	else:
		bs = []

	ax, bx, cx = rs, ys, bs
	la, lb, lc = r, y, b
	if la < lb:
		ax, bx = bx, ax
		la, lb = lb, la
	if la < lc:
		ax, cx = cx, ax
		la, lc = lc, la
	res = merge(ax, bx, cx)
	assert len(res) == N
	return res

for t in range(int(raw_input())):
	N, R, O, Y, G, B, V = map(int, tokens())
	sol = solve(N, R, O, Y, G, B, V)
	if sol is None:
		sol = 'IMPOSSIBLE'
	print "Case #{}: {}".format(t+1, sol)
