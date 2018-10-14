import sys

def main(argv):
	with open(argv) as inputFile:
		testcases = inputFile.readline()

		for t in range (0, int(testcases)):
			# print "Test case: "+str(t+1)

			answer1 = inputFile.readline()
			for offset in range(1, int(answer1)):
				inputFile.readline()

			set1 = inputFile.readline().split()

			for offset in range(0, 4-int(answer1)):
				inputFile.readline()

			answer2 = inputFile.readline()
			for offset in range(1, int(answer2)):
				inputFile.readline()

			set2 = inputFile.readline().split()

			for offset in range(0, 4-int(answer2)):
				inputFile.readline()

			result = list(set(set1).intersection(set(set2)))

			with open('output.txt', 'a') as output:
				if len(result) == 1:
					output.write("Case #"+str(t+1)+": "+str(result[0])+"\n")
				elif len(result) == 0:
					output.write("Case #"+str(t+1)+": Volunteer cheated!\n")
				else:
					output.write("Case #"+str(t+1)+": Bad magician!\n")
			# print "Case #"+str(t+1)+": "+str(time_total)
			

if __name__ == "__main__":
	# main(sys.argv[1:])
	main("A-small-attempt0.in")