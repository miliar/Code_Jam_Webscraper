#! /usr/bin/env python

from itertools import *

def generate_grid(height, width):
	rows = []

	for y in range(height):
		row = [""] * width

		rows.append(row)

	return rows

def prev_point(x, y, height, width):
	if x == 0 and y == 0:
		return (0, 0)

	if x == 0:
		return (width - 1, y - 1)
	else:
		return (x - 1, y)

def get_height_width(grid):
	height = len(grid)

	if height > 0:
		width = len(grid[0])
	else:
		width = 0

	return (height, width)

def get_adjacent(grid, x, y):
	dirs = []

	(height, width) = get_height_width(grid)

	if y > 0:
		dirs.append((grid[y - 1][x], (x, y - 1)))

	if x > 0:
		dirs.append((grid[y][x - 1], (x - 1, y)))

	if x < width - 1:
		dirs.append((grid[y][x + 1], (x + 1, y)))
	
	if y < height - 1:
		dirs.append((grid[y + 1][x], (x, y + 1)))

	return dirs

def choose_point(grid, x, y):
	def compare(a, b):
		if a[0] == b[0]:
			if a[1][1] == b[1][1]:
				return cmp(a[1][0], b[1][0])

			return cmp(a[1][1], b[1][1])

		return cmp(a[0], b[0])

	dirs = get_adjacent(grid, x, y)
	dirs.sort(compare)

	if len(dirs) == 0:
		return None

	chosen_dir = dirs[0]

	if chosen_dir[0] >= grid[y][x]:
		return None
	else:
		return chosen_dir

def path_drain(grid, x, y):
	def path_recursive(grid, x, y, path):
		path.append((x, y))

		dir = choose_point(grid, x, y)

		if dir == None:
			return path
		else:
			(dir_x, dir_y) = dir[1]

			return path_recursive(grid, dir_x, dir_y, path)

	return path_recursive(grid, x, y, [])

def set_label(grid, label_grid, x, y):
	(height, width) = get_height_width(grid)
	(prevx, prevy) = prev_point(x, y, height, width)

	if label_grid[prevy][prevx] == "":
		label = "a"
	else:
		label = chr(ord(label_grid[prevy][prevx]) + 1)

	path = path_drain(grid, x, y)
	
	(px, py) = path[-1]

	if label_grid[py][px] == "":
		for px, py in path:
			label_grid[py][px] = label
	else:
		label_grid[y][x] = label_grid[py][px]

	return label_grid

def set_grid_labels(grid):
	(height, width) = get_height_width(grid)

	label_grid = generate_grid(height, width)

	for y in range(height):
		for x in range(width):
			label_grid = set_label(grid, label_grid, x, y)

	return label_grid

def print_grid(label_grid):
	for row in label_grid:
		print ' '.join(row)

cases = int(raw_input())

for case in range(cases):
	sizes = raw_input().split(' ')
	[height, width] = [int(x) for x in sizes]

	grid = []

	for h in range(height):
		grid.append([int(x) for x in raw_input().split(' ')])

	label_grid = set_grid_labels(grid)

	print "Case #%d:" % (case + 1)
	print_grid(label_grid)

