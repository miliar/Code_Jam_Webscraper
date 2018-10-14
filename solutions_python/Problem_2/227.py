#!/usr/bin/python
import sys
input = open(sys.argv[1], "r")
output = open("train.out", "w")

#Variables
acc = 0
aAns = 0
bAns = 0
N = 0
T = 0
aAcc = 0
bAcc = 0
metaAcc = 0
aGain = [1441]#1441 is so there's at least one in it. It will never be reached
aUse = [1441]
bGain = [1441]
bUse = [1441]
#functions
def hhmmToM(str):
    ret=0
    ret+= int(str.split(":")[1])
    ret+= int(str.split(":")[0])*60
    return ret

def solveIt():
    #Sort the lists, then check each of the 1440 minutes
    aAns = 0
    bAns = 0
    a = 0
    b = 0
    #print aGain, aUse
    #print bGain, bUse
    aGain.sort()
    bGain.sort()
    aUse.sort()
    bUse.sort()
    for t in range(1440):
	while aGain[0] == t:
	    aGain.pop(0)
	    a += 1
	while bGain[0] == t:
	    bGain.pop(0)
	    b += 1
	while aUse[0] == t:
	    aUse.pop(0)
	    a -= 1
	while bUse[0] == t:
	    bUse.pop(0)
	    b -= 1
	if a < aAns:
	    aAns = a
	if b < bAns:
	    bAns = b
    output.write("Case #" + str(acc) + ": " + str(aAns*-1) +" " + str(bAns*-1) +"\n" )

#processing loop
for line in input:
    if N == 0:
	N = int(line)
	continue
    if aAcc:#A train from A
	aUse += [hhmmToM(line.split(' ')[0])]
	bGain += [hhmmToM(line.split(' ')[1])+T]
	aAcc -= 1
    elif bAcc:#A train from B
	bUse += [hhmmToM(line.split(' ')[0])]
	aGain += [hhmmToM(line.split(' ')[1])+T]
	bAcc -= 1
    elif metaAcc:#NA, NB
	aAcc = int(line.split(' ')[0])
	bAcc = int(line.split(' ')[1])
	metaAcc = 0
    else: #T
	if acc:
	    solveIt()
	    #reset vars for next case
	    aAns = 0
	    bAns = 0
	    aGain = [1441]
	    aUse = [1441]
	    bGain = [1441]
	    bUse = [1441]
	acc += 1
        T = int(line)
	metaAcc = 1

solveIt()
output.close()
