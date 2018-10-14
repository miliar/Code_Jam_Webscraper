
import sys
from collections import Counter

lines = [line.strip() for line in open(sys.argv[1])]

cases = int(lines[0])
lines.remove(lines[0])
gameset = []
case_number = 1

def has_won_list(list):
	counter = Counter(list)
	if counter['X'] == 4:
		return "X won"
	elif counter['O'] == 4:
		return "O won"
	elif counter['X'] == 3 and counter['T'] == 1:
		return "X won"
	elif counter['O'] == 3 and counter['T'] == 1:
		return "O won"
	else:
		return "noresult"

def has_completed(list):
	counter = Counter(list)
	if counter['.'] != 0:
		return "notcompleted"

def append_columns(list):
	col_list = []
	temp = []
	for x in range(0, 4):
		for row in list:
			temp.append(row[x])
		col_list.append(temp)
		temp = []
	
	for col in col_list:
		list.append(col)
	return list

def append_diag(list):
	diag_1 = []
	diag_2 = []
	for x in range(0, 4):
		y1 = 0
		y2 = 3
		for row in list:
			if x == y1:
				diag_1.append(row[x])
			if x == y2:
				diag_2.append(row[x])
			y1 += 1
			y2 -= 1
	list.append(diag_1)
	list.append(diag_2)
	return list

def process_game(list):
	
	#add columns and diagnals
	
	list = append_columns(list)
	list = append_diag(list)

	for row in list:
		ret = has_won_list(row)
		if ret == "noresult":
			continue
		else :
			return ret

	for row in list:
		ret = has_completed(row)
		if ret == "notcompleted":
			return "Game has not completed"
		
	return "Draw"

for line in lines:
	if len(line) == 0:
		state = process_game(gameset)
		print "Case #" + str(case_number) + ": " + str(state)
		gameset = []
		case_number += 1
			
	else:
		gameset.append(list(line))
