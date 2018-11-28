import sys
sys.setrecursionlimit(15000)

def cookie(C,F,X,r):
  if (C/r)+ X/(r+F) > (X/r):
    return X/r
  else:
    return C/r + cookie(C,F,X,r+F)

f=open("input2")
casenum=0
for line in f:
  if casenum==0:
    casenum+=1
    continue

  values=line.split(" ")
  (C,F,X) = (float(values[0]), float(values[1]), float(values[2]))
  print "Case #" +str(casenum) + ": " +  "%.7f" % cookie(C,F,X,2)
  casenum+=1
