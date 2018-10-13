
def get_row(f):
	rownum = int(f.readline())
	for j in range(4):
		currow = f.readline()
		if j == rownum-1:
			row = [int(u) for u in currow.split()]
	return row

def solve(testid):
	f = open(testid + '.in')
	g = open(testid + '.out', 'w')

	T = int(f.readline())

	for i in range(T):
		row1 = get_row(f)
		row2 = get_row(f)
		print(row1)
		print(row2)
		card = None
		total = 0
		for x in row1:
			if x in row2:
				total += 1
				card = x

		if total == 0:
			result = 'Volunteer cheated!'
		elif total == 1:
			result = str(card)
		else:
			result = 'Bad magician!'

		g.write('Case #{}: {}\n'.format(i+1, result))

	f.close()
	g.close()

if __name__ == '__main__':
#	solve('sample')
	solve('A-small-attempt0')


