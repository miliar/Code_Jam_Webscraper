import re

def checkRow(row, case):
	result = None
	result = re.search('([XT]{4}|[OT]{4})', row)
	if result is not None:
		if "X" in result.group(0):
			print("Case #%d: X won" % (case))
			return True
		if "O" in result.group(0):
			print("Case #%d: O won" % (case))
			return True
	return False

if __name__=="__main__":
	inputNum = int(raw_input())
	for i in range(1,inputNum+1):
		inp = []
		for x in range(4):
			inp.append(raw_input())

		raw_input()
		test = []
		for x in inp: 
			test.append(x)

		for x in range(4):
			test.append(inp[0][x]+inp[1][x]+inp[2][x]+inp[3][x])

		test.append(inp[0][0]+inp[1][1]+inp[2][2]+inp[3][3])
		test.append(inp[0][3]+inp[1][2]+inp[2][1]+inp[3][0])


		found = False
		for row in test:
			found = checkRow(row, i)
			if found: break
		if not found:
			dot = False
			for x in test:
				if "." in x:
					dot = True
					print("Case #%d: Game has not completed" % (i))
					break
			if not dot: print("Case #%d: Draw" % (i))