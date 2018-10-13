
def run():
	testCaseCount = eval(input())

	for i in range(testCaseCount):
		answer1 = eval(input())

		for x in range(answer1-1):
			input()
		answer1Row = input()
		for x in range(answer1, 4):
			input()

		answer2 = eval(input())
		for x in range(answer2-1):
			input()
		answer2Row = input()
		for x in range(answer2, 4):
			input()

		answer1Values = [eval(s) for s in answer1Row.split(' ')]
		answer2Values = [eval(s) for s in answer2Row.split(' ')]
		matchCount = 0
		lastMatch = ""

		for v in answer1Values:
			if v in answer2Values:
				matchCount += 1
				lastMatch = v

		if matchCount == 1:
			print("Case #"+str(i+1)+": "+str(lastMatch))

		elif matchCount == 0:
			print("Case #"+str(i+1)+": Volunteer cheated!")

		else:
			print("Case #"+str(i+1)+": Bad magician!")


if __name__ == '__main__':
	run()