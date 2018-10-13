#!/usr/bin/python
import sys
input = open(sys.argv[1], "r")
output = open("universe.out", "w")
acc = 0
queryAcc = 0
searchAcc = 0
newSet = True
searchNames = []
tally = []
ans = 0
firstLine = True
for line in input:
    if firstLine:
	firstLine = False
	continue 
    if queryAcc:
	queryAcc -= 1
	i = searchNames.index(line)
	if tally.count(0) == 1 and tally[i] == 0:
	    ans += 1
	    for j in range(len(tally)):
		tally[j] = 0
	tally[i] += 1
    elif searchAcc:
	searchAcc -= 1
	searchNames.append(line)
    elif newSet:#read S
	if acc != 0:
	    output.write("Case #" + str(acc) + ": " + str(ans) + "\n" )
	acc += 1
	searchAcc = int(line)
	searchNames=[]
	tally = []
	for i in range(searchAcc):
	    tally += [0]
	ans = 0
	newSet = False
    else:#read Q
	queryAcc = int(line)
	newSet = True

output.write("Case #" + str(acc) + ": " + str(ans) + "\n" )
output.close()
