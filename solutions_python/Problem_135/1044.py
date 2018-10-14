tests = int(raw_input())

def get_grid():
	grid = [[] for x in range(4)]
	for i in range(4):
		row = raw_input().split(" ")
		for x in row:
			grid[i].append(int(x))
	return grid

def get_similar(l1, l2):
	l = []
	for x in l1:
		for y in l2:
			if x == y and x not in l:
				l.append(x)
	return l


for i in range(tests):
	first_row = input() - 1
	first_grid = get_grid()
	second_row = input() - 1
	second_grid = get_grid()

	a = get_similar(first_grid[first_row], second_grid[second_row])
	
	answer = ""
	if len(a) == 1:
		answer = str(a[0])
	elif len(a) > 1:
		answer = "Bad magician!"
	else:
		answer = "Volunteer cheated!"

	print "Case #" + str(i+1) + ": " + answer
