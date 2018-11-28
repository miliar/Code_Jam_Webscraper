import sys

if len(sys.argv) == 2:
	inp = sys.argv[1]
	assert(inp[-3:] == '.in')
	outp = inp[:-3] + '.out'
	
	sys.stdin = open(inp, 'r')
	sys.stdout = open(outp, 'w')
	

T = int(sys.stdin.readline())
for case_number in range(1, T+1):
	N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split(' '))
	
	r = R - G
	y = Y - V
	b = B - O

	if B == O and N == B + O:
		ans = "BO" * (N//2)
	elif V == Y and N == V + Y:
		ans = "VY" * (N//2)
	elif R == G and N == R + G:
		ans = "RG" * (N//2)
	elif r < 0 or y < 0 or b < 0:
		ans = "IMPOSSIBLE"
	elif (r == 0 and R > 0) or (y == 0 and Y > 0) or (b == 0 and B > 0):
		ans = "IMPOSSIBLE"
	else:
		
		n = r + y + b
		
		if r == 0:
			if y == b:
				ans = "YB" * (n//2)
			else:
				ans = "IMPOSSIBLE"
		elif y == 0:
			if r == b:
				ans = "RB" * (n//2)
			else:
				ans = "IMPOSSIBLE"
		elif b == 0:
			if r == y:
				ans = "RY" * (n//2)
			else:
				ans = "IMPOSSIBLE"
		elif max(r, y, b) > n//2:
			ans = "IMPOSSIBLE"
		else:
			#all are > 0
			l = []
			for i in range(r-1):
				l.append("R")
				if (b > y):
					l.append("B")
					b -= 1
				else:
					l.append("Y")
					y -= 1
				
			l.append("R")
			
			#last group
			if b > y:
				assert b == y+1
				l += "BY" * y + "B"
			elif y > b:
				assert y == b+1
				l += "YB" * b + "Y"
			else:
				l += "BY" * y
		
			ans = "".join(l)
			
			if G > 0:
				ans = ans.replace("R", "R" + "GR"*G, 1)
			if O > 0:
				ans = ans.replace("B", "B" + "OB"*O, 1)
			if V > 0:
				ans = ans.replace("Y", "Y" + "VY"*V, 1)

	print("Case #{}: {}".format(case_number, ans))
