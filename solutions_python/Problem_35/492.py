import sys
import re


def printIntMap(map, W, H):
	for row in range(0,H):
		row_result = ""
		for col in range(0,W):
			#row_result += identifier_map[drain_map[row,col]] + " "
			row_result += str(map[row,col]) + " "
		row_result = row_result[0:-1]
		print row_result

def printWaterMap(map, W, H):
	for row in range(0,H):
		row_result = ""
		for col in range(0,W):
			#row_result += identifier_map[drain_map[row,col]] + " "
			row_result += str(map[row*W + col]) + " "
		row_result = row_result[0:-1]
		print row_result

def isSink(array, row, col, W, H):
	n_row = row
	n_col = col + 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if array[row*W + col] > array[n_row*W + n_col]:
			return False
	n_row = row
	n_col = col - 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if array[row*W + col] > array[n_row*W + n_col]:
			return False
	n_row = row + 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if array[row*W + col] > array[n_row*W + n_col]:
			return False
	n_row = row - 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if array[row*W + col] > array[n_row*W + n_col]:
			return False
	return True


def findFlow(water_map, drain_map, explored, row, col, W, H):
	if isSink(water_map, row, col, W, H):
		return
	if explored[row,col]==1:
		return
	l_neighbor = -1
	
	n_row = row - 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		l_neighbor = water_map[n_row*W + n_col]
		l_row = n_row
		l_col = n_col
	
	n_row = row
	n_col = col - 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[n_row*W + n_col] < l_neighbor:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
		elif l_neighbor == -1:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
	
	n_row = row
	n_col = col + 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[n_row*W + n_col] < l_neighbor:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
		elif l_neighbor == -1:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
	
	n_row = row + 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[n_row*W + n_col] < l_neighbor:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
		elif l_neighbor == -1:
			l_neighbor = water_map[n_row*W + n_col]
			l_row = n_row
			l_col = n_col
	
	if l_neighbor == -1:
		return
	
	if drain_map[l_row,l_col] == -1:
		return
	
	drain_map[row,col] = drain_map[l_row,l_col]
	explored[row,col] = 1
	
	n_row = row
	n_col = col + 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[row*W + col] <= water_map[n_row*W + n_col]:
			findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row
	n_col = col - 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[row*W + col] <= water_map[n_row*W + n_col]:
			findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row + 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[row*W + col] <= water_map[n_row*W + n_col]:
			findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row - 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		if water_map[row*W + col] <= water_map[n_row*W + n_col]:
			findFlow(water_map, drain_map, explored, n_row, n_col, W, H)


def flowFromSink(water_map, drain_map, explored, row, col, W, H):
	n_row = row
	n_col = col + 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row
	n_col = col - 1
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row + 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		findFlow(water_map, drain_map, explored, n_row, n_col, W, H)
	n_row = row - 1
	n_col = col
	if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
		findFlow(water_map, drain_map, explored, n_row, n_col, W, H)


def init_explored(W, H):
	explored = {}
	for row in range(0,H):
		for col in range(0,W):
			explored[row,col] = 0
	return explored


if __name__ == "__main__":
	lines = sys.stdin.read().split("\n")
	
	params = lines[0].split(" ")
	T = int(lines[0])
	identifier_names = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	currentLine = 1
	for i in range(0,T):
		params = lines[currentLine].split(" ")
		H = int(params[0])
		W = int(params[1])
		currentLine += 1
		
		water_map = []
		drain_map = {}
		
		for row in range(0,H):
			line_values = lines[currentLine].split(" ")
			for col in range(0,W):
				water_map += [line_values[col],]
				drain_map[row,col] = -1
			currentLine += 1
		
		identifier = 0
		sinks = []
		for row in range(0,H):
			for col in range(0,W):		
				if isSink(water_map, row, col, W, H):
					"""
					n_row = row
					n_col = col - 1
					if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
						if water_map[row*W + col] > water_map[n_row*W + n_col]:
							drain_map[row,col] = drain_map[n_row,n_col]
					n_row = row - 1
					n_col = col
					if n_row>=0 and n_row<H and n_col>=0 and n_col<W:
						if water_map[row*W + col] > water_map[n_row*W + n_col]:
							drain_map[row,col] = drain_map[n_row,n_col]
					"""
					if drain_map[row,col] == -1:
						drain_map[row,col] = identifier
						sinks += [(row,col),]
						identifier += 1

		#print sinks
		for row,col in sinks:
			explored = init_explored(W,H)
			flowFromSink(water_map, drain_map, explored, row, col, W, H)

		sink_counter = 0
		identifier_map = {}
		for row in range(0,H):
			for col in range(0,W):
				identifier = drain_map[row,col]
				if identifier not in identifier_map:
					identifier_map[identifier] = identifier_names[sink_counter]
					sink_counter += 1
				
		
		case_string = "Case #" + str(i+1) + ":"
		print case_string
		for row in range(0,H):
			row_result = ""
			for col in range(0,W):
				row_result += identifier_map[drain_map[row,col]] + " "
				#row_result += str(drain_map[row,col]) + " "
			row_result = row_result[0:-1]
			print row_result
