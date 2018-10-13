
def magic(sIn, sOut):
	fIn = open(sIn, 'r')
	fOut = open(sOut, 'w')

	T = int(fIn.readline())
	for t in range(1, T+1):
		ans1 = int(fIn.readline())
		for i in range(1, 4+1):
			line = fIn.readline().strip()
			if ans1 == i:
				row1 = set(line.split(' '))
		ans2 = int(fIn.readline())
		for i in range(1, 4+1):
			line = fIn.readline().strip()
			if ans2 == i:
				row2 = set(line.split(' '))
		intersect = row1 & row2
		result = ''
		if len(intersect) == 1:
			result = intersect.pop()
		elif len(intersect) > 1:
			result = 'Bad magician!'
		elif len(intersect) == 0:
			result = 'Volunteer cheated!'
		fOut.write('Case #{t}: {result}\n'.format(t=t, result=result))

if __name__ == '__main__':
	import sys
	magic(sys.argv[1], sys.argv[2])
