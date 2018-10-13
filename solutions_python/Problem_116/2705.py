import sys

f = open(sys.argv[1])

N = int(f.readline())

xwin = ['XXXX', 'TXXX', 'OTXX', 'XXTX', 'XXXT']
owin = ['OOOO', 'TOOO', 'OOTO', 'OTOO', 'OOOT']

for count in range(1, N+1):
	grid = []
	for j in range(4):
		grid.append(f.readline().strip())
	f.readline()
	win_cond = grid + [''.join([grid[i][k] for i in range(4)]) for k in range(4)] + [''.join([grid[i][i] for i in range(4)])] + [''.join([grid[i][3-i] for i in range(4)])]
	xhaswin, ohaswin, draw = False, False, False
	for test in win_cond:
		if test in xwin:
			xhaswin = True
		if test in owin:
			ohaswin = True
		if '.' in test:
			draw = True
	if xhaswin:
		print "Case #" + str(count) + ": X won"
	elif ohaswin:
		print "Case #" + str(count) + ": O won"
	elif draw:
		print "Case #" + str(count) + ": Game has not completed"
	else:
		print "Case #" + str(count) + ": Draw"

