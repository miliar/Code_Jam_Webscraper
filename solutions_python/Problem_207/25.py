import numpy as np

inname = "input.txt"
outname = "output.txt"

def solver(r, y, b, rc, yc, bc):
	n = r+y+b
	ans = [0]*n
	if 2*r == n:
		i = 0
		for i in range(r):
			ans[2*i] = rc
		i = 1
		while y>0:
			ans[i] = yc
			y -= 1
			i += 2
		while b>0:
			ans[i] = bc
			b -= 1
			i += 2
		return ans
	elif 2*y == n:
		return solver(y, r, b, yc, rc, bc)
	elif 2*b == n:
		return solver(b, r, y, bc, rc, yc)
	else:
		i = 0
		while r>0:
			ans[i] = rc
			r -= 1
			i += 2
			if i >= n:
				i = 1
		while y>0:
			ans[i] = yc
			y -= 1
			i += 2
			if i >= n:
				i = 1
		while b>0:
			ans[i] = bc
			b -= 1
			i += 2
			if i >= n:
				i = 1
		return ans


with open(inname, 'r') as f:
	cases = int(f.readline())
	for tc in range(1,cases+1):
		line = f.readline().strip().split(' ')
		N = int(line[0])
		R = int(line[1])
		O = int(line[2])
		Y = int(line[3])
		G = int(line[4])
		B = int(line[5])
		V = int(line[6])

		rr = R - G
		yy = Y - V
		bb = B - O

		possible = True
		ans = []
		if G>0 and rr<1:
			if rr == 0 and Y+V+B+O==0:
				ans = ['RG'] * G
			else:
				possible = False
		elif V>0 and yy<1:
			if yy == 0 and R+G+B+O==0:
				ans = ['YV'] * V
			else:
				possible = False
		elif O>0 and bb<1:
			if bb == 0 and Y+V+R+G==0:
				ans = ['BO'] * O
			else:
				possible = False
		else:
			nn = rr + yy + bb
			if 2*rr > nn or 2*yy > nn or 2*bb > nn:
				possible = False
			else:
				ans = solver(rr, yy, bb, 'R', 'Y', 'B')
				if G>0:
					j = 0
					while ans[j] != 'R':
						j+=1
					ans.insert(j, 'RG'*G)
				if V>0:
					j = 0
					while ans[j] != 'Y':
						j+=1
					ans.insert(j, 'YV'*V)
				if O>0:
					j = 0
					while ans[j] != 'B':
						j+=1
					ans.insert(j, 'BO'*O)


		if possible:
			print("Case #%d: %s" % (tc, "".join(ans)))
		else:
			print("Case #%d: IMPOSSIBLE" % tc)
