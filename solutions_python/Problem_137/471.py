import fileinput
import copy

def createMine(width, height, mines, recur = True):
	if mines != width * height - 1 and (mines > width * height - 1 - (1 if width > 1 else 0) - (1 if height > 1 else 0) - (1 if width > 1 and height > 1 else 0)):
		return "Impossible"
	else:
		mine = []
		for row in range(height):
			mine.append([])
			for column in range(width):
				mine[row].append("*")
		mine[0][0] = "c"
		left = width * height - mines - 1
		radius = 1
		while left > 0:
			for row in range(height):
				for column in reversed(range(width)):
					if max(row, column) == radius:
						mine[row][column] = "."
						left -= 1
					if left == 0:
						break
				if left == 0:
						break
			radius += 1
		valid = testMine(copy.deepcopy(mine))
		# valid = testMine(mine)
		if not valid:
			mine = []
			for row in range(height):
				mine.append([])
				for column in range(width):
					mine[row].append(".")
			mine[0][0] = "c"
			left = mines
			pos = (width - 1, height - 1)
			while left > 0:
				mine[pos[1]][pos[0]] = "*"
				left -= 1
				if pos[0] < width - 1 and pos[1] > 0:
					pos = (pos[0] + 1, pos[1] - 1)
				else:
					pos = (pos[0] - (height - pos[1]), height - 1)
					while pos[0] < 0:
						pos = (pos[0] + 1, pos[1] - 1)
			valid = testMine(copy.deepcopy(mine))
			# valid = testMine(mine)
		if not valid:
			mine = []
			for row in range(height):
				mine.append([])
				for column in range(width):
					mine[row].append(".")
			mine[0][0] = "c"
			left = mines
			for row in reversed(range(height)):
				for column in reversed(range(width)):
					mine[row][column] = "*"
					left -= 1
					if left == 0:
						break
				if left == 0:
					break
			valid = testMine(copy.deepcopy(mine))
		if not valid:
			mine = []
			for row in range(height):
				mine.append([])
				for column in range(width):
					mine[row].append(".")
			mine[0][0] = "c"
			left = mines
			for column in reversed(range(width)):
				for row in reversed(range(height)):
					mine[row][column] = "*"
					left -= 1
					if left == 0:
						break
				if left == 0:
					break
			valid = testMine(copy.deepcopy(mine))
		if not valid:
			mine = []
			for row in range(height):
				mine.append([])
				for column in range(width):
					mine[row].append("*")
			mine[0][0] = "c"
			left = width * height - mines - 1
			radius = 1
			while left > 0:
				nxt = []
				for row in range(height):
					for column in reversed(range(width)):
						if max(row, column) == radius:
							nxt.append((row, column))
				def comp (a, b):
					sub = min(a[0], a[1]) - min(b[0], b[1])
					if sub == 0:
						sub = max(a[0], a[1]) - max(b[0], b[1])
					return sub
				nxt.sort(cmp = comp)
				for el in nxt:
					mine[el[0]][el[1]] = "."
					left -= 1
					if left == 0:
						break;
				radius += 1
			valid = testMine(copy.deepcopy(mine))
		minestr = ""
		for row in range(height):
			for column in range(width):
				minestr += mine[row][column]
			if row < height - 1:
				minestr += "\n"
		if not valid:
			# print("Invalid Case:")
			# print("INVALID BELOW")
			# print(minestr)
			# raise Exception("This solution is invalid.")
			if recur == True:
				swapped = createMine(height, width, mines, False)
				if swapped != "Impossible" and swapped != "Impossible (due to numbers)" and swapped != "Impossible (due to positioning)":
					newmine = []
					for column in swapped[0]:
						newmine.append([])
					for row in swapped:
						cn = 0
						for column in row:
							newmine[cn].append(row[cn])
							cn += 1
					swapstr = ""
					for row in range(height):
						for column in range(width):
							swapstr += newmine[row][column]
						if row < height - 1:
							swapstr += "\n"
					return swapstr
			return "Impossible"
		if not recur:
			return mine
		else:
			return minestr

def testMine(mine):
	testMinePos(mine, 0, 0)
	dotstill = False
	for row in range(len(mine)):
		for column in range(len(mine[0])):
			if mine[row][column] == ".":
				dotstill = True
				break
	return not dotstill

def testMinePos(mine, x, y):
	if y >= len(mine) or y < 0 or x < 0 or x >= len(mine[y]):
		return
	if mine[y][x] in (".", "c"):
		count = mineCount(mine, x, y)
		if mine[y][x] == "c":
			mine[y][x] = "0"
		else:
			mine[y][x] = str(count)
		if count == 0:
			testMinePos(mine, x + 1, y)
			testMinePos(mine, x + 1, y + 1)
			testMinePos(mine, x, y + 1)
			testMinePos(mine, x - 1, y + 1)
			testMinePos(mine, x - 1, y)
			testMinePos(mine, x - 1, y - 1)
			testMinePos(mine, x, y - 1)
			testMinePos(mine, x + 1, y - 1)

def mineCount(mine, x, y):
	return mineAtPos(mine, x + 1, y) + mineAtPos(mine, x + 1, y + 1) + mineAtPos(mine, x, y + 1) + mineAtPos(mine, x - 1, y + 1) + mineAtPos(mine, x - 1, y) + mineAtPos(mine, x - 1, y - 1) + mineAtPos(mine, x, y - 1) + mineAtPos(mine, x + 1, y - 1)

def mineAtPos(mine, x, y):
	if y >= len(mine) or y < 0 or x < 0 or x >= len(mine[y]):
		return 0
	return 1 if mine[y][x] == "*" else 0

i = -1
for line in fileinput.input("codejam3.in"):
	i += 1
	if i == 0:
		continue
	R, C, M = line.split()
	print("Case #" + str(i) + ":\n" + createMine(int(C), int(R), int(M)))