import sys
import collections 

nibbles = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
	"4":"0100", "5":"0101", "6":"0110", "7":"0111",
	"8":"1000", "9":"1001", "A":"1010", "B":"1011",
	"C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def hex2bin(s):
	return "".join(map(lambda x: nibbles[x], s))

def sum(s):
	return reduce(lambda x, y: x + y, s)

def transposed(lists):
   if not lists: return []
   return map(lambda *row: list(row), *lists)

def find_boards(chessboard, marks, size):
	count = 0
	for y in range(len(chessboard)-size+1):
		for x in range(len(chessboard[y])-size+1):
			rows_to_check = collections.deque(range(size))
			quit = False
			prev_row = None
			while len(rows_to_check) and not quit:
				row = rows_to_check.popleft()
				neighbors = zip(chessboard[y+row][x:x+size], chessboard[y+row][x+1:x+size])
				alternates = map(lambda x: x[0] != x[1] and x[0] in ["0", "1"] and x[1] in ["0", "1"], neighbors)
				if not reduce(lambda x, y: x and y, alternates) or sum(marks[y+row][x:x+size]) > 0:
					quit = True 
				if prev_row != None:
					neighbors = zip(chessboard[y+row][x:x+size], prev_row)
					alternates = map(lambda x: x[0] != x[1] and x[0] in ["0", "1"] and x[1] in ["0", "1"], neighbors)
					if not reduce(lambda x, y: x and y, alternates) or sum(marks[y+row][x:x+size]) > 0:
						quit = True 
				prev_row = chessboard[y+row][x:x+size]
			if not quit:
				for row in range(size):
					marks[y+row][x:x+size] = [size]*size
				count += 1
	return count
	
def test():
	dims = map(lambda x: int(x), sys.stdin.readline().split())
	chessboard = []
	boards = []
	marks = []
	for line in range(dims[0]):
		input = sys.stdin.readline()[:-1]
		chessboard.append(hex2bin(input))
		marks.append([0] * len(chessboard[line]))
	for x in reversed(range(2,min(dims)+1)):
		boards.append(str(x) + " " + str(find_boards(chessboard, marks, x)))
	boards.append("1" + " " + str(sum(map(lambda x: x.count(0),marks))))
	boards = filter(lambda x: int(x.split()[1]) > 0, boards) 
	return str(len(boards)) + "\n" + "\n".join(boards)

TestCases = int(sys.stdin.readline())
for testCase in range(TestCases):
	print "Case #"+str(testCase+1)+": "+test()
