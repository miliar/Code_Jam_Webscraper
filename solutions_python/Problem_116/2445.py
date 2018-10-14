#!/usr/bin/python

def deal_case(case_num, board):
	result = ''
	row = 0
	empty = 0

	for array in board:
		if '.' in array:
			empty = 1
			break
	# row
	for array in board:
		if 'T' in array:			
			delimeter = array.index('T')
			array = array[:delimeter] + array[delimeter+1:]
			if array == 'XXX':
				result = 'X won'
				break
			elif array == 'OOO':
				result = 'O won'
				break
		else:
			if array == 'XXXX':
				result = 'X won'
				break
			elif array == 'OOOO':
				result = 'O won'
				break

	if result == '':
		# diagonal
		dia1 = ''
		for i in range(0,4):
			dia1 += board[i][i]
		dia2 = ''
		for i in range(0,4):
			dia2 += board[i][3-i]
		dia = [dia1, dia2]
		for array in dia:
			if 'T' in array:			
				delimeter = array.index('T')
				array = array[:delimeter] + array[delimeter+1:]
				if array == 'XXX':
					result = 'X won'
					break
					
				elif array == 'OOO':
					result = 'O won'
					break
			
			else:
				if array == 'XXXX':
					result = 'X won'
					break

				elif array == 'OOOO':
					result = 'O won'
					break

		if result == '':
			# col
			# swap
			array = ''
			trans_board = []
			for col in range(0,4):
				for row in range(0,4):
					array = array + board[row][col]
				trans_board.append(array)
				array = ''

			for array in trans_board:
				if 'T' in array:			
					delimeter = array.index('T')
					array = array[:delimeter] + array[delimeter+1:]

					if array == 'XXX':
						result = 'X won'
						break
					elif array == 'OOO':
						result = 'O won'
						break
				else:
					if array == 'XXXX':
						result = 'X won'
						break
					elif array == 'OOOO':
						result = 'O won'
						break

	if result == '':
		if empty == 1:
			result = 'Game has not completed' 
		elif empty == 0:
			result = 'Draw'
	
	return "Case #" + str(case_num) + ": " + result + "\n"

def deal_file(fname1,fname2):
	f = open(fname1, 'r')
	f_r = open(fname2, 'w')
	line_num = 0
	case_num = 1
	board = []
	for line in f:
		if line_num == 0:
 			totalcase = int(line)
		elif line_num%5 != 0:
			line = line.split('\n')[0]
			board.append(line)
			if line_num%5 == 4:
				result = deal_case(case_num, board)
				#print line_num
				#print board
				print "Case #%d: %s\n" % (case_num, result)
				f_r.write(result)
				case_num += 1
		elif line_num%5 == 0:
			board = []
		line_num += 1

	f.close()
	f_r.close()

def main():
	#deal_file('A-small-attempt0.in.txt', 'A-small-attempt0.out.txt')
	deal_file('A-large.in.txt', 'A-large.out.txt')
	#deal_file('A-small-sample.in.txt', 'A-small-sample.out.txt')

if __name__ == '__main__':
	main()
