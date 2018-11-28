import sys
import fileinput

boards = []
tests = 0
expectedTests = None
expectTestNext = False

def eall(xs):
	return all(x == xs[0] for x in xs)
	
def eany(xs, e):
	for x in xs:
		if x == e:
			return True
	return False

for line in fileinput.input():
	if fileinput.isfirstline():
		expectedTests = int(line)
		expectTestNext = True
	else:
		if line == '\n' and tests < expectedTests:
			expectTestNext = True
		if expectTestNext:
			boards.append([])
			expectTestNext = False
			tests += 1
		for cell in line:
			if cell in 'XOT.':
				boards[-1].append(cell)
				
for test, board in enumerate(boards):
	exhausted = False
	winner = None
	
	for Tx in ['X', 'O']:
		if winner is None:
			b = [Tx if x == 'T' else x for x in board]
			# Test rows
			for y in range(0, 4):
				segment = b[y*4 : y*4 + 4]
				if eall(segment) and segment[0] in 'XO':
					winner = segment[0]
					print('Case #%s: %s won' % (test + 1, winner))

			if winner is None:
				# Test columns
				for y in range(0, 4):
					segment = b[y:: 4]
					if eall(segment) and segment[0] in 'XO':
						winner = segment[0]
						print('Case #%s: %s won' % (test + 1, winner))

			if winner is None:
				# Test diagonals
				for segment in (b[::5], b[3 : -1 : 3]):
					if eall(segment) and segment[0] in 'XO':
						winner = segment[0]
						print('Case #%s: %s won' % (test + 1, winner))
				
	# Test draw
	if winner is None:
		if not eany(board, '.'):
			print('Case #%s: Draw' % (test + 1))
		else:
			print('Case #%s: Game has not completed' % (test + 1))
