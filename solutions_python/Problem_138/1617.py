import sys

def ReverseChained(chained):
	List = list(chained)
	List.reverse()
	return List

FileName = sys.argv[1]
def main():
	with open(FileName) as FileReader:
		TestCases = int(FileReader.readline())
		for CaseIndex in range(1, TestCases + 1):
			N = int(FileReader.readline())
			Stack = []
			DeceitfulWar = DeceitfulWarLosses = DeceitfulWarWins = WarCounter = WarWin = WarLosses = 0
			NaomiWeights = sorted([float(x) for x in FileReader.readline().split()])
			KenWeights = sorted([float(x) for x in FileReader.readline().split()])
			NaomiWeights.reverse()
			KenWeights.reverse()
			for x in range(N * 2):
				if len(KenWeights) == 0 or (len(NaomiWeights) > 0 and NaomiWeights[0] > KenWeights[0]):
					NaomiWeights.pop(0)
					Stack.append(1)
				else:
					KenWeights.pop(0)
					Stack.append(-1)
			for Value in Stack:
				if DeceitfulWarWins + DeceitfulWarLosses >= N:
					break
				if Value == 1:
					DeceitfulWar += 1
					DeceitfulWarWins += 1
				else:
					if DeceitfulWar > 0:
						DeceitfulWar -= 1
					else:
						DeceitfulWarLosses += 1
			Stack.reverse()
			for Value in Stack:
				if Value == 1:
					WarCounter += 1
				else:
					if WarCounter > 0:
						WarLosses += 1
						WarCounter -= 1
					else:
						WarWin += 1
			print "Case #" + str(CaseIndex) + ": " + str(DeceitfulWarWins) + " " + str(WarWin)

main()
