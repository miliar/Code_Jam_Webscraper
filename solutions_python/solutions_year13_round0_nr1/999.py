import re

def test(gd):
	gd_reversed = ["","","","",""]
	draw = True
	for i in gd:
		if(re.match('[XT]+$', i)):
			return "X won"
		elif(re.match('[OT]+$',i)):
			return "O won"
		elif('.' in i):
			draw = False
		gd_reversed[0] += i[0]
		gd_reversed[1] += i[1]
		gd_reversed[2] += i[2]
		gd_reversed[3] += i[3]
	for i in gd_reversed:
		if(re.match('[XT]+$', i)):
			return "X won"
		elif(re.match('[OT]+$',i)):
			return "O won"
	crosses = [gd[0][0]+gd[1][1]+gd[2][2]+gd[3][3],gd[0][3]+gd[1][2]+gd[2][1]+gd[3][0]]
	for i in crosses:
		if(re.match('[XT]+$', i)):
			return "X won"
		elif(re.match('[OT]+$',i)):
			return "O won"
	if(draw):
		return "Draw"
	else:
		return "Game has not completed"
	

if __name__ == "__main__":
	CT = raw_input()
	for j in range(int(CT)):
		grid = []
		for i in range(4):
			grid.append(raw_input())
		raw_input()
		print "Case #"+str(j+1)+": "+test(grid)