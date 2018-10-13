from sys import stdin

def printAnswer(caseIndex, answer):
	print("Case #", caseIndex+1, ": ", answer, sep='')

T = int(input())
for t in range(T):
	(farmCost, farmExtraProd, winCost) = map(float, input().split())
	currProd = 2

	timeForWin = winCost / currProd
	prevTimeForWin = timeForWin

	accTime = 0
	while timeForWin <= prevTimeForWin:
		accTime += farmCost / currProd
		currProd += farmExtraProd

		prevTimeForWin = timeForWin
		timeForWin = winCost / currProd + accTime

	printAnswer(t, prevTimeForWin)