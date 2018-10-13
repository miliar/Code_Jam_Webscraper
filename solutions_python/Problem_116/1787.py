#! /usr/bin/python3
# VIC Nicolas - Qualification Round: Problem A for the Google CodeJam 2013

def solve_tictac(lines):
	#vertical
	return_val = check_4(lines[0][0], lines[0][1], lines[0][2], lines[0][3])
	if return_val == 1 : return
	return_val = check_4(lines[1][0], lines[1][1], lines[1][2], lines[1][3])
	if return_val == 1 : return
	return_val = check_4(lines[2][0], lines[2][1], lines[2][2], lines[2][3])
	if return_val == 1 : return
	return_val = check_4(lines[3][0], lines[3][1], lines[3][2], lines[3][3])
	if return_val == 1 : return
	#horizontal
	return_val = check_4(lines[0][0], lines[1][0], lines[2][0], lines[3][0])
	if return_val == 1 : return
	return_val = check_4(lines[0][1], lines[1][1], lines[2][1], lines[3][1])
	if return_val == 1 : return
	return_val = check_4(lines[0][2], lines[1][2], lines[2][2], lines[3][2])
	if return_val == 1 : return
	return_val = check_4(lines[0][3], lines[1][3], lines[2][3], lines[3][3])
	if return_val == 1 : return
	#diagonals
	return_val = check_4(lines[0][0], lines[1][1], lines[2][2], lines[3][3])
	if return_val == 1 : return
	return_val = check_4(lines[0][3], lines[1][2], lines[2][1], lines[3][0])
	if return_val == 1 : return

	check_draw(lines)

def check_4(char1,char2, char3, char4):
	global counter

	if (char1 == 'X' or char1 == 'T') \
	and (char2 == 'X' or char2 == 'T') \
	and (char3 == 'X' or char3 == 'T') \
	and (char4 == 'X' or char4 == 'T') :
		print("Case #{}: X won".format(counter))
		counter = counter + 1
		return 1

	if (char1 == 'O' or char1 == 'T') \
	and (char2 == 'O' or char2 == 'T') \
	and (char3 == 'O' or char3 == 'T') \
	and (char4 == 'O' or char4 == 'T') :
		print("Case #{}: O won".format(counter))
		counter = counter + 1
		return 1

	return 0

def check_draw(lines):
	global counter
	for line in lines:
		for char in line :
			if char == '.' :
				print("Case #{}: Game has not completed".format(counter))
				counter = counter + 1
				return

	print("Case #{}: Draw".format(counter))
	counter = counter + 1
	return


total_problems = int(input())
counter = 1

for i in range(total_problems):
	solve_tictac([input(), input(), input(), input()])
	input()



