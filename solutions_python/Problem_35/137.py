import re
import copy
import collections

letters = 'abcdefghijklmnopqrstuvwxyz12345'

def parse(file):
	def flow_to(x, y):
		is_flow = False
		cell = map[x][y]
		
		result = is_flow, x, y
		lowest = cell
		
		#north
		if x>0:
			if map[x-1][y] < lowest:
				result = True, x-1, y
				lowest = map[x-1][y]
		#west
		if y>0:
			if map[x][y-1] < lowest:
				result = True, x, y-1
				lowest = map[x][y-1]
		#east
		if y<(w-1):
			if map[x][y+1] < lowest:
				result = True, x, y+1
				lowest = map[x][y+1]
		#south
		if x<(h-1):
			if map[x+1][y] < lowest:
				result = True, x+1, y
				lowest = map[x+1][y]
		return result
	
	def print_map(map):
		for l in map:
			print(' '.join([str(x) for x in l]))

	lines = open(file).readlines()
	lines = [line.strip() for line in lines]
	
	maps_count = int(lines[0])
	
	maps = []
	cur_line = 1
	for i in range(maps_count):
		x, y = [int(x) for x in lines[cur_line].split(' ')]
		map = [[int(a) for a in line.split(' ')] for line in lines[cur_line+1:cur_line+1+x]]
		cur_line += 1 + x
		maps.append((x, y, map)) 
	
	#maps = [maps[1]]
	result_maps = []
	for h, w, map in maps:
		max_letter = 0
		l = letters[max_letter]
		result_map = [[l for i in range(w)] for j in range(h)]
		
		tocell_fromcell = collections.defaultdict(list)
		
		for x, row in enumerate(map):
			for y, cell in enumerate(row):
				is_flow, fx, fy = flow_to(x, y)
				tocell_fromcell[(fx, fy)] += [(x, y)]
		
		changed = True
		while changed:
			changed = False
			for f, t in copy.deepcopy(tocell_fromcell).items():
				for c in t:
					if c!=f and c in tocell_fromcell:
						tocell_fromcell[f] += tocell_fromcell[c]
						del tocell_fromcell[c]
						changed = True

		d = collections.defaultdict(list)
		for f, t in copy.deepcopy(tocell_fromcell).items():
			d[min(t)] = t
		
		if 0:
			for f, t in d.items():
				print(f, t)
		
		max_letter = 0
		l = letters[max_letter]
		keys = sorted(d.keys())
		for k in keys:
			t = d[k]
			for c in t:
				result_map[c[0]][c[1]] = l
			max_letter += 1
			l = letters[max_letter]
		
		if show_info:
			print('result')
			print_map(result_map)
			print()
		
		result_maps.append(result_map)
		pass
	
	if not show_info:
		for i, map in enumerate(result_maps):
			print('Case #%s:' % (i+1))
			#print_map(maps[i][2])
			print_map(map)

show_info = 0
parse('B-large.in')
