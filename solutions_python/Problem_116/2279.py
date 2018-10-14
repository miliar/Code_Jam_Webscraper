def getResp(arr):
	arr.sort()
	st = "".join()
	if st == "OOOT":
		return 3
	elif st == "TXXX":
		return 2
	elif "." in st:
		return 1
	else:   
		return 0

def solve(arr):
	s = 0
	pos = [
		# vertical
		[(0,0),(0,1),(0,2),(0,3)],
		[(1,0),(1,1),(1,2),(1,3)],
		[(2,0),(2,1),(2,2),(2,3)],
		[(3,0),(3,1),(3,2),(3,3)],
		# horizantal
		[(0,0),(1,0),(2,0),(3,0)],
		[(0,1),(1,1),(2,1),(3,1)],
		[(0,2),(1,2),(2,2),(3,2)],
		[(0,3),(1,3),(2,3),(3,3)],
		# diagonals
		[(0,0),(1,1),(2,2),(3,3)],
		[(0,3),(1,2),(2,1),(3,0)]
	]

	for p in pos:
		a = []
		for (x,y) in p:
			a.append(arr[x][y])
		a.sort()
		b = "".join(a)
		if b == "OOOT" or b == "OOOO":
			return "O won"
		elif b == "TXXX" or b == "XXXX":
			return "X won"
		elif "." in a:
			s += 1
	if s > 0:
		return "Game has not completed"
	else:
		return "Draw"


input_text = [line.strip() for line in open('a.txt')]
CASE_COUNT = int(input_text[0])
for CASE_NUM in range(1,CASE_COUNT+1):
	start = (CASE_NUM-1)*5+1
	end = start + 4
	arr = [list(x) for x in input_text[start:end]]
	print "Case #%d: %s" % (CASE_NUM,solve(arr))
