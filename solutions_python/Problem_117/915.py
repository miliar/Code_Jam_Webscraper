from pprint import pprint
import pdb

def main():
	with open('B-large.in') as f:
		ntests = int(f.readline())
		for n in range(ntests):
			pattern = []
			xy = f.readline()[:-1].split(' ')
			x, y = (int(xy[0]), int(xy[1]))
			for i in range(x):
				pattern.append(f.readline()[:-1].split(' '))
			if ispossible(pattern, x, y):
				result = "YES"
			else:
				result = "NO"
			print "Case #%d: %s" % (n+1, result)

def ispossible(pattern, x, y):
	for i in range(x):
		for j in range(y):
			if not isaccessible(pattern, i, j, x, y):
				return False
	return True

def isaccessible(pattern, i, j, x, y):
	"""A square is accessible if all square on the same line OR column are of equal or lower value"""
	height = int(pattern[i][j])
	column = row = False
	#check column
	for a in range(x):
		if int(pattern[a][j]) > height:
			break
	else:
		column = True

	#check row
	for a in range(y):
		if int(pattern[i][a]) > height:
			break
	else:
		row = True
	return (column or row)
main()



333
323
323