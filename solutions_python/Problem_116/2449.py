import sys

rl = lambda: sys.stdin.readline().strip()

num_cases = int(rl())

for i in range(1, num_cases + 1):
	lines = rl(), rl(), rl(), rl()
	ans = ""
	for line in lines:
		if line.replace("T", "X") == "XXXX":
			ans = "X won"
		if line.replace("T", "O") == "OOOO":
			ans = "O won"
	transpose = map(lambda a: str(a[0])+str(a[1])+str(a[2])+str(a[3]), list(zip(*lines)))
	for line in transpose:
		if line.replace("T", "X") == "XXXX":
			ans = "X won"
		if line.replace("T", "O") == "OOOO":
			ans = "O won"
	diag1 = lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3]
	diag2 = transpose[0][3] + transpose[1][2] + transpose[2][1] + transpose[3][0]
	if diag1.replace("T", "X") == "XXXX": ans = "X won"
	if diag1.replace("T", "O") == "OOOO": ans = "O won"
	if diag2.replace("T", "X") == "XXXX": ans = "X won"
	if diag2.replace("T", "O") == "OOOO": ans = "O won"
	
	if ans == "":
		dotleft = False
		for line in lines:
			if "." in list(line):
				dotleft = True
		if dotleft:
			ans = "Game has not completed"
		else:
			ans = "Draw"
			
	print "Case #" + str(i) + ":", ans
	rl() # blank
	