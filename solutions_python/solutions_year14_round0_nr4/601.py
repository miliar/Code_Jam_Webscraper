#!/usr/bin/python
import sys
sys.setrecursionlimit(1500)

def checkList(nList, kList, total):
	print("checkList", nList, kList, total)
	if len(nList) == 0:
		return total
	
	if nList[0] < kList[0]:
		nList.pop(0)
		kList.pop()
		return checkList(nList,kList,total)
	else:
		nList.pop(0)
		kList.pop(0)
		total += 1
		return checkList(nList,kList,total)

file_arg = sys.argv[1]
f = open(file_arg, 'r')
string = ""
count = 0
for i in range(int(f.readline())):
	print("------")
	line = f.readline().split()
	nLista = sorted([float(k) for k in f.readline().split()])
	kLista = sorted([float(k) for k in f.readline().split()])
	wWins = 0
	dWins = 0
	#normal Wins
	tempList = list(kLista)
	for index, item in enumerate(nLista):
		found = False
		for indexK, itemK in enumerate(tempList):
			if item < itemK:
				found = True
				tempList.remove(itemK)
				break
		if not found:
			wWins += 1
	#decit Wins
	tempKList = list(kLista)
	tempNList = list(nLista)
	dWins = checkList(tempNList,tempKList, 0)
	string += "Case #" + str(i + 1) + ": " + str(dWins) + " " + str(wWins) + "\n"
print(string)
text_file = open("output.out", "w")
text_file.write(string)
text_file.close()