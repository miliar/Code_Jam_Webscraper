def test_cases():
	from sys import stdin
	from collections import defaultdict
	
	num_cases = int(stdin.readline().strip())
	for case in xrange(num_cases):
		tiles = defaultdict(lambda:defaultdict(lambda:'.'))
		height, width = map(int, stdin.readline().strip().split())
		for row in xrange(height):
			r = stdin.readline().strip()
			for col in xrange(width):
				tiles[row][col] = r[col]
		
		yield ((height, width), tiles)

def print_tiles((height, width), tiles):
	from sys import stdout
	for row in xrange(height):
		for col in xrange(width):
			stdout.write(tiles[row][col])
		print

def replace_hashes((height, width), tiles):
	for row in xrange(height):
		for col in xrange(width):
			if tiles[row][col] == '#':
				if row+1<height and col+1<width and tiles[row+1][col] == '#' and tiles[row+1][col+1] == '#' and tiles[row][col+1] == '#':
					tiles[row][col] = '/'
					tiles[row][col+1] = '\\'
					tiles[row+1][col] = '\\'
					tiles[row+1][col+1] = '/'
				else:
					return False
	return True

def find_hashes((height, width), tiles):
	for row in xrange(height):
		for col in xrange(width):
			if tiles[row][col] == '#':
				return True
	return False

for (case_number, ((height, width), tiles)) in enumerate(test_cases()):
	possible = replace_hashes((height, width), tiles) and not find_hashes((height, width), tiles)

	print "Case #%d:" % (case_number+1)
	if possible:
		print_tiles((height, width), tiles)
	else:
		print "Impossible"