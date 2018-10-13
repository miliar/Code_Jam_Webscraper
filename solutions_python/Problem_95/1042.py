#!/usr/bin/python
#Filename:Tongues.py

import sys

inname = "input.txt"
inref = "inputref.txt"
inres = "inputres.txt"
outname = "output.txt"
if len(sys.argv)>1:
	inname = sys.argv[1]
	outname = inname.rstrip(".in")
	outname = outname + ".out"
fin = open(inname,"r")
finref = open(inref,"r")
finres = open(inres,"r")
fout = open(outname,"w")

refNum = int(finref.readline().rstrip("\n"))

ori = []
res = []
ton = dict()
for i in xrange(refNum):
	line = finref.readline().rstrip("\n")
	lineres = finres.readline().rstrip("\n")
	for j in xrange(len(line)):
		ton[line[j]]=lineres[j]


ton["z"]="q"
ton["q"]="z"
#print len(ton)
#print ton.keys()
#print ton.values()


testCaseNum = int(fin.readline().rstrip("\n"))
for i in xrange(testCaseNum):
	line = fin.readline().rstrip("\n")
	answer = "Case #%d: " %(i+1)
	an = ""
	for j in line:
		an += ton[j]
	answer += an + "\n"
	fout.write(answer)

fin.close()
finres.close()
fout.close()

	
