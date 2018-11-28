import time
import math

# Found a mistake after my little submission.  The length being used in the inner loop
# should be the length of n and not of bigA.

debug = False

xlate = "yhesocvxduiglbkrztnwjpfmaq"

tStart = time.time()

fname = "A-small-attempt0"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):
    line = flines[icase]
    outstr = ""
    for i in range(len(line)):
        if line[i] == ' ':
            outstr += ' '
        elif line[i] == "\n":
            outstr += "\n"
        else:
            outstr += xlate[ord(line[i])-ord('a')]
    outstr = "Case #%d: %s" % (icase,outstr)
    print outstr
    fout.write("%s" % (outstr))

fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))
