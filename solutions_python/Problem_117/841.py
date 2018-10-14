import sys

def validate_lawn(lawn, rows, cols):
	for row in range(0, rows):
		for col in range(0, cols):

			row_mowable = True
			for col_index in range(0, cols):
				if (lawn[row][col_index] > lawn[row][col]):
					row_mowable = False
					break

			col_mowable = True
			for row_index in range(0, rows):
				if (lawn[row_index][col] > lawn[row][col]):
					col_mowable = False
					break

			if (not row_mowable and not col_mowable):
				return False

	return True

input = open(sys.argv[1], 'r')

n = input.readline()
n = n[:-1]
n = int(n)

for i in range(0, n):
	dimensions = input.readline().split()
	rows = int(dimensions[0])
	cols = int(dimensions[1])

	lawn = []
	
	for row in range(0, rows):
		line = input.readline().split()
		line = map(int, line)
		lawn.append(line)
		
	sys.stdout.write('Case #' + str(i + 1) + ': ')
		
	if (validate_lawn(lawn, rows, cols)):
		sys.stdout.write('YES')
	else:
		sys.stdout.write('NO')	
	
	if (i + 1 < n):
		print('')

input.close()