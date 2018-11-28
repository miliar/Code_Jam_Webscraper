

from sys import stdin


def f(b):
	TX = ('T','X') 
	TO = ('T','O')

	# rows
	for r in range(4):
		if b[r][0] in TX and b[r][1] in TX and b[r][2] in TX and b[r][3] in TX:
			return 'X won'
		if b[r][0] in TO and b[r][1] in TO and b[r][2] in TO and b[r][3] in TO:
			return 'O won'
	# cols
	for c in range(4):
		if b[0][c] in TX and b[1][c] in TX and b[2][c] in TX and b[3][c] in TX:
			return 'X won'
		if b[0][c] in TO and b[1][c] in TO and b[2][c] in TO and b[3][c] in TO:
			return 'O won'
	
	# diags
	if b[0][0] in TX and b[1][1] in TX and b[2][2] in TX and b[3][3] in TX:
		return 'X won'
	if b[0][0] in TO and b[1][1] in TO and b[2][2] in TO and b[3][3] in TO:
		return 'O won'
	if b[0][3] in TX and b[1][2] in TX and b[2][1] in TX and b[3][0] in TX:
		return 'X won'
	if b[0][3] in TO and b[1][2] in TO and b[2][1] in TO and b[3][0] in TO:
		return 'O won'

	for r in range(4):
		for c in range(4):
			if b[r][c] == '.': return "Game has not completed"

	return 'Draw'

if __name__ == '__main__':
	T = int(stdin.readline())
	b = ['']*4
	for t in range(1, T+1):
		for x in range(4):
			b[x] = stdin.readline().strip()
			assert len(b[x]) == 4
		stdin.readline()
		print "Case #" + str(t)+': ' + f(b)


