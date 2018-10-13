import sys, os, re
ma = re.match
fo = open(sys.argv[1], "r")
out = open("sa.txt","w")
grid = [['','','',''],['','','',''],['','','',''],['','','','']]

def vw(g):
	iscompl = 1
	for y in range(4):
		xX = 0
		xO = 0
		yX = 0
		yO = 0
		for x in range(4):
			if g[x][y] == '.':
				iscompl = 0
			
			if   g[x][y] == 'T':
				xX += 1
				xO += 1
			elif g[x][y] == 'X':
				xX += 1
			elif g[x][y] == 'O':
				xO += 1
			
			if   g[y][x] == 'T':
				yX += 1
				yO += 1
			elif g[y][x] == 'X':
				yX += 1
			elif g[y][x] == 'O':
				yO += 1
			
			if xX==4 or yX==4:
				return "xwin"
			if xO==4 or yO==4:
				return "owin"

	xw = '[XT]'
	ow = '[OT]'
	#diagonal check
	if (ma(xw,g[0][0]) and ma(xw,g[1][1]) and ma(xw,g[2][2]) and ma(xw,g[3][3])):
		return "xwin"
	if (ma(ow,g[0][0]) and ma(ow,g[1][1]) and ma(ow,g[2][2]) and ma(ow,g[3][3])):
		return "owin"
	if (ma(xw,g[0][3]) and ma(xw,g[1][2]) and ma(xw,g[2][1]) and ma(xw,g[3][0])):
		return "xwin"
	if (ma(ow,g[0][3]) and ma(ow,g[1][2]) and ma(ow,g[2][1]) and ma(ow,g[3][0])):
		return "owin"
	
	if iscompl == 1:
		return 'draw'
	else:
		return 'nc'

ra = int(fo.readline()[:-1])

for cc in range(ra):
	count = 0
	for a in range(4):
		for c in fo.readline()[:-1]:
			if count <= 3:
				grid[0][count] = c
			elif count <= 7:
				grid[1][count - 4] = c
			elif count <= 11:
				grid[2][count - 8] = c
			elif count <= 15:
				grid[3][count - 12] = c
			count +=1
	fo.readline()

	#print(grid)
	r = vw(grid)
	
	cc+=1
	if r == "xwin":
		out.write("Case #"+str(cc)+": X won\n")
	elif r == "owin":
		out.write("Case #"+str(cc)+": O won\n")
	elif r == "draw":
		out.write("Case #"+str(cc)+": Draw\n")
	elif r == "nc":
		out.write("Case #"+str(cc)+": Game has not completed\n")

fo.close()
out.close()
