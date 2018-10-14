


def magictrick():
	number = 0
	out = open("output.txt","w")
	problem = open("A-small-attempt0.in.txt")
	cases = int (problem.readline())	
	while (number < cases):
		number += 1
		for line in problem:
			if len(list(line)) == 2:
				whichrow = int(line)	
				row = 0
				while (row < whichrow):
					line = next(problem)
					row += 1
				firstrow = str.split(line)
				print(firstrow)
				break
		for line in problem:
			if len(list(line)) == 2:
				whichrow = int(line)	
				row = 0
				while (row < whichrow):
					line = next(problem)
					row += 1
				secondrow = str.split(line)
				print(secondrow)
				break
		count = 0
		for firsttime in firstrow:
			for secondtime in secondrow:
				if firsttime == secondtime:
					card = firsttime
					count += 1
		if count == 1:
			print ("Case #" + str(number) + ": " + str(card), file=out)
		elif count > 1:
			print("Case #" + str(number) + ": Bad magician!", file=out)
		elif count < 1:
			print ("Case #" + str(number) + ": Volunteer cheated!", file=out)
		

magictrick()
