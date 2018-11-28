#!/usr/bin/python3

def read_input(filename):
	lines = open(filename, 'r').read().splitlines()
	number_of_inputs = int(lines[0])
	boardlist = []
	offset = 1
	while(offset < len(lines)):
		dimensions = lines[offset].split()
		[rows, columns] = map(int, dimensions)
		board = [list(map(int, r.split())) for r in lines[offset+1:offset+rows+1]]
		boardlist.append((rows, columns, board))
		assert len(board) == rows
		offset += rows+1
	assert len(boardlist) == number_of_inputs
	return boardlist

def parse_input(boardlist):
	lawns = []
	for (rows, cols, board) in boardlist:
		rotboard = [[board[x][y] for x in range(rows)] for y in range(cols)]
		lawns.append((rows, cols, board, rotboard))
	return lawns

def check_lawn(lawn):
	(rows, cols, normal, rot) = lawn
	for rowidx in range(rows):
		for colidx in range(cols):
			patch = normal[rowidx][colidx]
			possible = check_line(patch, normal[rowidx]) or check_line(patch, rot[colidx])
			if not possible:
				return False

	return True

def check_line(val, line):
	return val == max(line)

def main():
	input = read_input("input.txt")
	lawns = parse_input(input)
	cnt = 0
	for lawn in lawns:
		cnt += 1
		print("Case #", cnt, ":", sep="", end=" ")
		if check_lawn(lawn):
			print("YES")
		else:
			print("NO")

if __name__ == "__main__":
	main()
