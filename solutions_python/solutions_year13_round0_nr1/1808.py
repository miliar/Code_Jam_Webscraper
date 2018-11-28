#bennett schaffner
#tick-tac-toe-tomek solver

f = open("A-large.in","r")

cases = int(f.readline())

lines = f.readlines()
f.close()

case = 0


options = ['X won', 'O won', 'Draw', 'Game has not completed']
matrix = []


def solve(m):
	unplaced = 0;
	for h in m:
		x = o = t = 0
		for char in range(4):
			if h[char] == 'X':
				x = x + 1
			elif h[char] == 'O':
				o = o + 1
			elif h[char] == 'T':
				t = 1
			else:
				unplaced = unplaced + 1
		if x == 4 or ( x == 3 and t == 1 ):
			return 0
		elif o == 4 or ( o == 3 and t == 1 ):
			return 1
			
	for v in range(4):
		x = o = t = 0
		for y in range(4):	
			if m[y][v] == 'X':
				x = x + 1
			elif m[y][v] == 'O':
				o = o + 1
			elif m[y][v] == 'T':
				t = 1
		if x == 4 or ( x == 3 and t == 1 ):
			return 0
		elif o == 4 or ( o == 3 and t == 1 ):
			return 1

	x = o = t = 0
	for d in range(4):
		if m[d][d] == 'X':
			x = x + 1
		elif m[d][d] == 'O':
			o = o + 1;
		elif m[d][d] == 'T':
			t = 1;
	if x == 4 or ( x == 3 and t == 1 ):
		return 0
	elif o == 4 or ( o == 3 and t == 1 ):
		return 1	

	x = o = t = 0
	for d in range(4):
		if m[d][3-d] == 'X':
			x = x + 1
		elif m[d][3-d] == 'O':
			o = o + 1;
		elif m[d][3-d] == 'T':
			t = 1;
	if x == 4 or ( x == 3 and t == 1 ):
		return 0
	elif o == 4 or ( o == 3 and t == 1 ):
		return 1

	if unplaced == 0:
		return 2
	return 3


w = open('outhuge.txt','w')

for line in lines:
	if line == "\n":
		result = solve(matrix)
		matrix = []
		case = case + 1		
		w.write("Case #" + str(case) + ": " + options[result] + '\n')
		if case >= cases:
			break
	else:
		matrix.append([line[0],line[1],line[2],line[3]])


w.close()
