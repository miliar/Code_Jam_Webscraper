# 00:09

def doit(tab):
	vazio = False
	for row in tab:
		if all(map(lambda x: x in 'XT', row)):
			return 'X won'
		if all(map(lambda x: x in 'OT', row)):
			return 'O won'

		vazio = vazio or '.' in row

	for x in xrange(4):
		col = tab[0][x] + tab[1][x] + tab[2][x] + tab[3][x]

		if all(map(lambda x: x in 'XT', col)):
			return 'X won'
		if all(map(lambda x: x in 'OT', col)):
			return 'O won'

	diag1 = tab[0][0] + tab[1][1] + tab[2][2] + tab[3][3]
	diag2 = tab[0][3] + tab[1][2] + tab[2][1] + tab[3][0]

	if all(map(lambda x: x in 'XT', diag1)):
		return 'X won'
	if all(map(lambda x: x in 'OT', diag1)):
		return 'O won'

	if all(map(lambda x: x in 'XT', diag2)):
		return 'X won'
	if all(map(lambda x: x in 'OT', diag2)):
		return 'O won'

	if vazio:
		return 'Game has not completed'
	return 'Draw'

def main():
	# fp = open('a.in')
	fp = open('A-large.in')

	for case in xrange(int(fp.readline())):
		tab = []
		for x in xrange(4):
			tab.append(fp.readline().strip())
		fp.readline()

		result = doit(tab)

		print 'Case #{0}: {1}'.format(case+1, result)

if __name__ == "__main__":
	main()
