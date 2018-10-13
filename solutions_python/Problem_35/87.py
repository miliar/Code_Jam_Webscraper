import sys
import operator

def _check_boundary(H, W, x, y):
	if (x < 0) or (y < 0):
		return False
	elif (x == H) or (y == W):
		return False
	return True

def move_one_step(each_map):
	H = len(each_map)
	W = len(each_map[0])
	directions = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]
	steps = {}
	sinks = []

	#initialize
	for i in range(len(each_map)):
		for j in range(len(each_map[i])):
			steps[(i, j)] = [ ]

	for i in range(len(each_map)):
		for j in range(len(each_map[i])):
			min = (i, j)
			minval = each_map[i][j]
			for direction in directions:
				x = i + direction[0]
				y = j + direction[1]
				if not _check_boundary(H, W, x, y):
					continue
				if each_map[x][y] < minval:
					min = (x, y)
					minval = each_map[x][y]

			if min == (i, j):
				sinks.append((i, j))
			else:
				steps[min].append((i, j))

	return steps, sinks

def find_drainage(sink, steps):
	drainage = [ sink ]
	for new_sink in steps[sink]:
		drainage.extend(find_drainage(new_sink, steps))
	return drainage

def color_drainage_basins(each_map):
	steps, sinks = move_one_step(each_map)
	drainages = [ find_drainage(sink, steps) for sink in sinks ]
	first_elements = {}
	for i, drainage in enumerate(drainages):
		drainage.sort()
		first_elements[i] = drainage[0]

	sorted_elements = sorted(first_elements.items(), key=operator.itemgetter(1))
	label = "a"
	label_dict = {}
	for drainage_num, element in sorted_elements:
		label_dict[drainage_num] = label
		label = chr(ord(label) + 1)

	labeled_map = {}
	for drainage_num, drainage in enumerate(drainages):
		for axis in drainage:
			labeled_map[axis] = label_dict[drainage_num]

	return labeled_map


if __name__ == "__main__":
	INPUT_FILE = "B-large.in"
	input_file = file(INPUT_FILE)
	T = int(input_file.readline())
	maps = []
	for i in range(T):
		(H, W) = map(int, input_file.readline().split())
		each_map = []
		for j in range(H):
			each_map.append(tuple(map(int, input_file.readline().split())))
		maps.append(tuple(each_map))
	
	for i, each_map in enumerate(maps):
		print "Case #%d:" % (i + 1)
		labeled_map = color_drainage_basins(each_map)
		H = len(each_map)
		W = len(each_map[0])
		for x in range(H):
			row = []
			for y in range(W):
				row.append(labeled_map[(x, y)])
			if i == (T - 1) and x == (H - 1):
				sys.stdout.write(" ".join(row))
			else:
				print " ".join(row)

