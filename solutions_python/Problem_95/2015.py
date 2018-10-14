import string 
import sys

tr=string.maketrans(string.lowercase,'yhesocvxduiglbkrztnwjpfmaq')
inname = "A-small-attempt1.in"
outname = "A-small-attempt1.out"
if len(sys.argv)>1:
    inname = sys.argv[1]
    outname = inname.rstrip(".in")
    outname = outname + ".out"

fin = open(inname,"r")
fout = open(outname,"w")
testCaseNum = int(fin.readline())
lines = fin.readlines()
caseNum = 0
for line in lines:
    caseNum = caseNum + 1
    line = line.rstrip('\n')
    answer = "Case #%d: " %(caseNum)
    answer = answer + line.translate(tr)
    answer = answer + "\n"
    fout.write(answer)

fin.close()
fout.close()

