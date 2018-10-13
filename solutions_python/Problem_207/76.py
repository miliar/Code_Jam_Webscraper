T = int(raw_input())

def doprob():
	N, R, O, Y, G, B, V = map(int, raw_input().split())
	if R < G or B < O or Y < V:
		return "IMPOSSIBLE"
	if R == G and R > 0:
		if R+G == N:
			return "RG" * R
		return "IMPOSSIBLE"
	if B == O and B > 0:
		if B+O == N:
			return "BO" * B
		return "IMPOSSIBLE"
	if Y == V and Y > 0:
		if Y+V == N:
			return "YV" * Y
		return "IMPOSSIBLE"
	r = R-G
	b = B-O
	y = Y-V
	n = r+b+y
	if r > b+y or b > r+y or y > b+r:
		return "IMPOSSIBLE"
	out = ""
	m = max([r,b,y])
	if m == r:
		x = b+y-r
		out = 'RBY'*x + "RB"*(b-x) + "RY"*(y-x)
	elif m == b:
		x = r+y-b
		out = 'BRY'*x + "BR"*(r-x) + "BY"*(y-x)
	else:
		x = r+b-y
		out = 'YBR'*x + "YB"*(b-x) + "YR"*(r-x)

	fr = out.find('R')
	fb = out.find('B')
	fy = out.find('Y')
	out = out[:fr] + "RG"*G + out[fr:]
	out = out[:fb] + "BO"*O + out[fb:]
	out = out[:fy] + "YV"*V + out[fy:]
	return out

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())