
with open('o1', 'w+') as output:
	with open('t1', 'r+') as fle:
		cases = int(fle.readline())
		curCase = 0
		for i in range(cases):
			curCase += 1
			ans = int(fle.readline()) - 1
			lines = []
			for inc in range(4):
				if inc == ans:
					lines = fle.readline().split()
				else:
					fle.readline()
			ans2 = int(fle.readline()) - 1
			lines2 = []
			for inc in range(4):
				if inc == ans2:
					lines2 = fle.readline().split()
				else:
					fle.readline()
			matches = 0
			matchNums = []
			for char in lines:
				for char2 in lines2:
					if char == char2:
						matches += 1
						matchNums.append(char)
			if matches == 0:
				output.write('Case #' + str(curCase) + ': Volunteer cheated!')
			elif matches == 1:
				output.write('Case #' + str(curCase) + ': ' + str(matchNums[0]))
			else:
				output.write('Case #' + str(curCase) + ': Bad magician!')
			output.write('\n')



