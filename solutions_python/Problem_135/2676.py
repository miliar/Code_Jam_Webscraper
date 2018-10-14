from sys import stdin

def readRowOfItems():
	rowIndex = int(input())
	for uselessRow in range(rowIndex - 1):
		input()
	items = set(map(int, input().split()))
	for uselessRow in range(4 - rowIndex):
		input()
	return items

def printAnswer(caseIndex, answer):
	print("Case #", caseIndex+1, ": ", answer, sep='')

T = int(input())
for t in range(T):
	set1 = readRowOfItems()
	set2 = readRowOfItems()

	inter = set1 & set2
	if len(inter) == 1:
		printAnswer(t, inter.pop())
	elif len(inter) > 1:
		printAnswer(t, "Bad magician!")
	else:
		printAnswer(t, "Volunteer cheated!")


