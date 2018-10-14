import sys
import os

case_num = int(sys.stdin.readline()[:-1])
arr = [ [0 for col in range(60)] for row in range(60) ]

def load_arr(row,column,arr):
	for i in range(row):
		row_content = sys.stdin.readline()[:-1]
		for j in range(column):
			arr[i][j] = row_content[j]	

def check_able(row_id, col_id, arr):
	if arr[row_id+1][col_id] == "#" and arr[row_id+1][col_id+1] == "#" and arr[row_id][col_id+1] == "#":
		arr[row_id][col_id] = "/"
		arr[row_id+1][col_id] = "\\"
		arr[row_id][col_id+1] = "\\"
		arr[row_id+1][col_id+1] = "/"
		return True
	else:
		return False

for case_id in range(1, case_num+1):
	is_able = True
	arr_size = sys.stdin.readline()[:-1].split(" ")
	row = int(arr_size[0])
	column = int(arr_size[1])
	load_arr(row,column,arr)
	for row_id in range(row):
		for col_id in range(column):
			if arr[row_id][col_id] != "#":
				continue
			else:
				if check_able(row_id, col_id,arr) == False:
					is_able = False
					break
		if is_able == False:
			break
	if is_able == False:
		print "Case #%d:" % (case_id)
		print "Impossible"
	else:
		print "Case #%d:" % (case_id)
		for r in range(row):
			for c in range(column):
				sys.stdout.write(arr[r][c])
			print
			
					
