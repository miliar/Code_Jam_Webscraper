IMP = "IMPOSSIBLE"
def do_case():
	# input()
	# int(input())
	n, r, o, y, g, b, v = list(map(int, input().split()))

	nr = r - g
	ny = y - v
	nb = b - o
	# special case... damn.
	# RGRGRG works
	if all(color == 0 for color in (nr, ny, nb)):
		# ???
		# only works with RGRG like stuff
		if sum(color == 0 for color in (r, y, b)) == 2:
			# special case
			if r:
				return "RG" * r
			if y:
				return "YV" * y
			if g:
				return "BO" * b
		else:
			return IMP
	if sum(color == 0 for color in (nr, ny, nb)) == 2:
		return IMP
	if any(color == 0 for color in (nr, ny, nb)):
		if r == g and g:
			return IMP
		if y == v and v:
			return IMP
		if b == o and b:
			return IMP
	if any(color < 0 for color in (nr, ny, nb)):
		return IMP
	# if max((nr, ny, nb)) > sum((nr, ny, nb))/2:
	# 	return IMP
	# need to split evenly
	out = []
	aa, bb, cc = sorted((nr, ny, nb))
	one, two, three = sorted("RYB", key=lambda x:{"R":nr, "Y":ny, "B":nb}[x])
	while aa + bb > cc:
		out += [three, two, one]
		cc -= 1
		aa -= 1
		bb -= 1
		if aa < 0:
			return IMP

	while cc:
		if aa:
			out += [three, one]
			aa -= 1
			cc -= 1
		else:
			out += [three, two]
			bb -= 1
			cc -= 1

	if bb or aa:
		return IMP
		print(out)
		print(aa, bb, cc)
		assert False

	if o:
		# add "OB" onto an b
		# guaranteed that there is one
		out[out.index("B"):out.index("B")] = "BO"*o
	if g:
		# print(out)
		# print(n, r, o, y, g, b, v )
		# add "GR" onto a r
		out[out.index("R"):out.index("R")] = "RG"*g
	if v:
		# add "VY" onto a y
		out[out.index("Y"):out.index("Y")] = "YV"*v



	assert len(out) == n

	return "".join(out)

T = int(input())
for case in range(T):
	ans = do_case()
	print("Case #{}: {}".format(case+1, ans))
