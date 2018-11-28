game = {
	
	1 :[[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1]],

	2: [[0, 1, 0, 1],
		[1, 1, 1, 1],
		[0, 1, 0, 1],
		[1, 1, 1, 1]],

	3: [[0, 0, 0, 0],
		[0, 0, 1, 0],
		[0, 1, 1, 1],
		[0, 0, 1, 0]],

	4: [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 1],
		[0, 0, 1, 1]],
}

def print_result(t, s):
	print "Case #" + str(t) + ": " + s

t = int(raw_input())

for tt in range(1,t+1):
	(x,r,c) = map(int, raw_input().split(' '))

	if( game[x][r-1][c-1] == 1):
		print_result(tt, "GABRIEL")
	else:
		print_result(tt, "RICHARD")