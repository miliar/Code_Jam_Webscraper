#!/usr/bin/python

positions = [(0, 1, 2, 3),
             (4, 5, 6, 7),
             (8, 9, 10, 11),
             (12, 13, 14, 15),
             (0, 4, 8, 12),
             (1, 5, 9, 13),
             (2, 6, 10, 14),
             (3, 7, 11, 15),
             (0, 5, 10, 15),
             (3, 6, 9, 12)]

# let's jam!
in_file = open('0-a.in', 'r')
tests = int(in_file.readline())
out_file = open('0-a.out', 'w')

for test in range(1, tests + 1):
	board = ''.join([in_file.readline().strip() for i in range(4)])
	in_file.readline()

	for position in positions:
		outcome = set([board[i] for i in position])

		if outcome <= set(['X', 'T']):
			out_file.write('Case #%d: X won\n' % test)
			break

		elif outcome <= set(['O', 'T']):
			out_file.write('Case #%d: O won\n' % test)
			break

	else:
		if board.find('.') == -1:
			out_file.write('Case #%d: Draw\n' % test)

		else:
			out_file.write('Case #%d: Game has not completed\n' % test)

out_file.close()
in_file.close()
