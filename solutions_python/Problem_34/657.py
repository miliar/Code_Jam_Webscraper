import sys, re
    
#read in the file, parse the input to get the data.
file = sys.argv[1]
f = open(file,'r')

LDN = f.readline();
match = re.match("(\d+) (\d+) (\d+)",LDN)
L = match.group(1)
D = match.group(2)
N = match.group(3)

words = []
for i in xrange(int(D)):
  words.append(f.readline().replace("\n",""))

patterns = []
for i in xrange(int(N)):
  patterns.append(f.readline().replace("\n",""))

patterns = map(lambda x: x.replace("(","[").replace(")","]"),patterns)

caseNum = 1;
for pat in patterns:
  print "Case #"+str(caseNum)+": "+str(len(filter(lambda x: re.match(pat,x),words)))
  caseNum = caseNum + 1

