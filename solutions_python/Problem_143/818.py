import sys

FileName = sys.argv[1]
def main():
	with open(FileName) as FileReader:
		TestCases = int(FileReader.readline())
		for CaseIndex in range(1, TestCases + 1):
			StringInput = FileReader.readline().split()
			A = int(StringInput[0])
			B = int(StringInput[1])
			K = int(StringInput[2])
			Wins = 0
			for a in range(A):
				for b in range(B):
					if a & b < K:
						Wins += 1
			print "Case #" + str(CaseIndex) + ": " + str(Wins)
main()