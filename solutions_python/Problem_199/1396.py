def checkHappy(pancake):
	if "-" in pancake:
		return False
	return True

def flipPancake(side):
	if (side == "-"):
		return "+"
	if (side == "+"):
		return "-"

with open('A-large.in') as f:
	t = int(f.readline())  # read a line with a single integer
	case = 0
	for line in f:
		case+=1
		numFlip = 0
		pancakeStr, flipperStr = [s.rstrip() for s in line.split(' ')]
		pancakeArr = list(pancakeStr.split(' ')[0])
		k = int(flipperStr)
		possible = True
		for pancakeIndex in range(0,len(pancakeArr)):
			if pancakeArr[pancakeIndex] == "-":
				if pancakeIndex + k > len(pancakeArr):
					possible = False
					break
				numFlip += 1
				for pancake in range(pancakeIndex,pancakeIndex + k):
					pancakeArr[pancake] = flipPancake(pancakeArr[pancake])
		finalPancakes = ''.join(pancakeArr)
		if (checkHappy(finalPancakes)) and possible:
			print("Case #{}: {}".format(case, numFlip))
		else:
			print("Case #{}: {}".format(case, "IMPOSSIBLE"))