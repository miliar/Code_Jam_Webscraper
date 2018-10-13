
MAXSIZE = 100
filename = "C-small-2.in"

data = [map(lambda x: int(x), line.rstrip().split()) for line in open(filename, "r")]
ll = 1
qc = 1

while ll < len(data):

	size = data[ll][0]
	ll += 1
	max = [0, 0]
	min = [MAXSIZE, MAXSIZE]
	cells = [[0 for x in range(MAXSIZE)] for y in range(MAXSIZE)]
	for i in range(size):
		for x in range(data[ll][0], data[ll][2] + 1):
			for y in range(data[ll][1], data[ll][3] + 1):
				cells[x - 1][y - 1] = 1
		if data[ll][0] < min[0]: min[0] = data[ll][0]
		if data[ll][1] < min[1]: min[1] = data[ll][1]
		if data[ll][2] > max[0]: max[0] = data[ll][2]
		if data[ll][3] > max[1]: max[1] = data[ll][3]
		ll += 1
	min[0] -= 1
	min[1] -= 1
	max[0] -= 1
	max[1] -= 1

	time = 0
	while True:
		time += 1
		newcells = [line[:] for line in cells]
		for x in range(min[0], max[0] + 1):
			for y in range(min[1], max[1] + 1):
				if cells[x][y] == 1:
					if x == 0 and y == 0:
						newcells[x][y] = 0
					elif x == 0:
						if cells[x][y - 1] == 0:
							newcells[x][y] = 0
					elif y == 0:
						if cells[x - 1][y] == 0:
							newcells[x][y] = 0
					elif cells[x][y - 1] == 0 and cells[x - 1][y] == 0:
						newcells[x][y] = 0
				else:
					if cells[x][y - 1] == 1 and cells[x - 1][y] == 1:
						newcells[x][y] = 1
		flag = True
		while flag:
			for i in range(min[1], max[1] + 1):
				if cells[min[0]][i] == 1:
					flag = False
					break
			if flag:
				min[0] += 1
				if min[0] > max[0]: break
		if min[0] > max[0]: break
		flag = True
		while flag:
			for i in range(min[1], max[1] + 1):
				if cells[max[0]][i] == 1:
					flag = False
					break
			if flag:
				max[0] -= 1
				if min[0] > max[0]: break
		if min[0] > max[0]: break
		flag = True
		while flag:
			for i in range(min[0], max[0] + 1):
				if cells[i][min[1]] == 1:
					flag = False
					break
			if flag:
				min[1] += 1
				if min[1] > max[1]: break
		if min[1] > max[1]: break
		flag = True
		while flag:
			for i in range(min[0], max[0] + 1):
				if cells[i][max[1]] == 1:
					flag = False
					break
			if flag:
				max[1] -= 1
				if min[1] > max[1]: break
		if min[1] > max[1]: break
		cells = newcells

	print "Case #%d: %d" % (qc, time - 1)
	qc += 1

