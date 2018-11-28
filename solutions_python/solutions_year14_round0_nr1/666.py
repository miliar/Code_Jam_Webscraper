def main():
	scanner = open('A-small-attempt1.in','r')
	writer = open('A-small-attempt1.out','w')
	T = int(scanner.readline())
	x = 1
	while x <= T and x <= 100:
		ans1 = 0
		ans2 = 0
		card1 = []
		card2 = []
		line = ''
		
		ans1 = int(scanner.readline())
		row = 0
		while row < 4:
			line = scanner.readline().split()
			colNums = []
			col = 0
			while col < 4:
				colNums.append(int(line[col]))
				col += 1
			card1.append(colNums)
			row += 1
		
		ans2 = int(scanner.readline())
		row = 0
		while row < 4:
			line = scanner.readline().split()
			colNums = []
			col = 0
			while col < 4:
				colNums.append(int(line[col]))
				col += 1
			card2.append(colNums)
			row += 1
		
		i = 0
		pos = -1
		while i < 4:
			j = 0
			while j < 4:
				if card1[ans1 - 1][i] == card2[ans2 - 1][j]:
					if pos == -1:
						pos = i
					else:
						pos = -2
						break
				j += 1
			if pos == -2:
				break
			i += 1
		
		if pos == -1:
			writer.write('Case #%d: Volunteer cheated!' % x)
		elif pos == -2:
			writer.write('Case #%d: Bad magician!' % x)
		else:
			writer.write('Case #%d: %d' % (x, card1[ans1-1][pos]))
		if x < T and x < 100:
			writer.write('\n')
		x += 1

if __name__ == '__main__':
	main()