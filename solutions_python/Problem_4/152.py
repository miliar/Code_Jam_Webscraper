#!/usr/bin/python
import sys
input = open(sys.argv[1], "r")
output = open("scalar.out", "w")
#Theorem: If we sort one ascending and one descending, that is the optimal order
#... It would take too long to prove mathematically during the contest though.
caseN = 0
vA = []
vB = []
acc = 0
n = 0
caseVal = 0

for line in input:
    if caseN == 0:
	caseN = int(line)
	continue
    if n == 0:
	n = int(line)
	continue
    if acc == 0:
	acc+=1
	vA = map(int, line.split(' '))
    else:
	acc = 0
	n = 0
	vB = map(int, line.split(' '))
	ans = 0
	vA.sort()
	vB.sort()
	vB.reverse()
	#print vA, vB
	for i in range(len(vA)):
	    ans += vA[i] * vB[i]
	caseVal += 1
	output.write("Case #"+str(caseVal)+": "+str(ans) +"\n")

input.close()
output.close()
