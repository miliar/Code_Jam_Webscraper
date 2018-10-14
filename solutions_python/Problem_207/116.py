def arrange3(manes):
	manes = sorted(manes)
	if manes[-1][0] <= manes[0][0] + manes[1][0]:
		exceed = (manes[0][0] + manes[1][0]) - manes[-1][0]
		stall = ""
		for i in range(exceed):
			stall += (manes[-1][1] + manes[0][1] + manes[1][1])
		for i in range(manes[0][0] - exceed):
			stall += (manes[-1][1] + manes[0][1])
		for i in range(manes[1][0] - exceed):
			stall += (manes[-1][1] + manes[1][1])
		return stall
	return 'IMPOSSIBLE'

def arrange6(R, O, Y, G, B, V):
	N = R + O + Y + G + B + V
	if O > B or G > R or V > Y:
		return 'IMPOSSIBLE'
	if O==B and O > 0:
		if N > O+B:
			return 'IMPOSSIBLE'
		return 'OB'*(N/2)
	if G==R and G > 0:
		if N > G+R:
			return 'IMPOSSIBLE'
		return 'GR'*(N/2)
	if Y==V and Y > 0:
		if N > V+Y:
			return 'IMPOSSIBLE'
		return 'VY'*(N/2)

	b = B - O
	r = R - G
	y = Y - V

	breplace = 'B' + 'OB'*O
	rreplace = 'R' + 'GR'*G
	yreplace = 'Y' + 'VY'*V

	stall = arrange3([(b,'B'), (r,'R'), (y,'Y')]) 
	if stall!= 'IMPOSSIBLE':
		stall = stall.replace('B', breplace, 1)
		stall = stall.replace('R', rreplace, 1)
		stall = stall.replace('Y', yreplace, 1)

	return stall


def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		N, R, O, Y, G, B, V = map(int, raw_input().strip().split())
		print "Case #" + str(caseno+1) + ": " + arrange6(R, O, Y, G, B, V)

run()