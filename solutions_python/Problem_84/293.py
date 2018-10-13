def add(x, y): return x+y

def rpi(inp, r, c):
	for i in range(r):
		for j in range(c):
			if inp[i][j] == '#':
				if i+1 < r and j+1 < c and inp[i+1][j] == '#' and inp[i+1][j+1] == '#' and inp[i][j+1] == '#':
					inp[i][j] = inp[i+1][j+1] = '/'
					inp[i+1][j] =  inp[i][j+1] = '\\'
				else:
					return "Impossible"
					
	return '\n'.join([''.join(x) for x in inp])
	
	
def solve():
	fin = open("input.txt")
	lines = fin.readlines()
	line_num = 0

	tot_case = int(lines[line_num])
	line_num = line_num + 1	
	fout = open("out.txt", 'w')
	for case in range(tot_case):
		row, col =  [int(i) for i in lines[line_num].split(' ')]
		line_num = line_num + 1	
		inp = []
		for i in range(row):
			line = lines[line_num]
			line_num = line_num + 1	
			inp.append(list(line)[:col])
		
		fout.write("Case #"+str(case+1)+":\n")
		fout.write(rpi(inp, row, col) + "\n")
			
solve();