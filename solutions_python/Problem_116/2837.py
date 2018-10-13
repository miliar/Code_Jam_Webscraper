from copy import deepcopy
import sys

games = open("tictac.dat").readlines()
cases = int(games[0].replace("\n", ""))
CONS_X = "X"
CONS_O = "O"
CONS_T = "T"
CONS_DOT = "."

win = ((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15), # Horizontal
	   (0,4,8,12),(1,5,9,13),(2,6,10,14),(3,7,11,15), # Vertical
	   (0,5,10,15), (3,6,9,12)) # Diagonal
table = []

def define_table():
	line_start = 1
	for case in range(cases):
		line = []
		for i in range(4):
			l = games[line_start].replace("\n", "")
			for n_line in range(4):
				line.append(l[n_line])
			line_start += 1
		line_start += 1
		table.append(line)

def change_t(list, cons):
	return [list[i].replace(CONS_T, cons) for i in range(len(list))]

def check_equal(list):
	return not list or list == [list[0]] * len(list)

def check_dot(list):
	c = 0
	for element in list:
		if element == CONS_DOT:
			return True
	return False

def brute_force(list):
	list_tmp = change_t(deepcopy(list), CONS_O)
	if check_equal(list_tmp):
		return True
	list_tmp = change_t(deepcopy(list), CONS_X)
	if check_equal(list_tmp):
		return True
	return False

def check_win(table):
	for row in win:
		if table[row[0]] != CONS_DOT and brute_force([table[i] for i in row]):
			return table[row[0]]

def main():
	define_table()
	for tabl in range(cases):
		result = check_win(table[tabl])
		if result == CONS_X or result == CONS_T:
			sys.stdout.write("Case #")
			sys.stdout.write(str(tabl + 1))
			sys.stdout.write(": X won")
		elif result == CONS_O or result == CONS_T:
			sys.stdout.write("Case #")
			sys.stdout.write(str(tabl + 1))
			sys.stdout.write(": O won")
		elif check_dot(table[tabl]):
			sys.stdout.write("Case #")
			sys.stdout.write(str(tabl + 1))
			sys.stdout.write(": Game has not completed")
		else:
			sys.stdout.write("Case #")
			sys.stdout.write(str(tabl + 1))
			sys.stdout.write(": Draw")
		print

if __name__ == "__main__":
	main()

