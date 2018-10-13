## I was in a hurry ;)
attempt = "A-small-attempt0"

import time
# from collections import OrderedDict
time.clock()

def removeadjacentduplicates(string):
  thestring = list(string)
  i = 1
  while i < len(thestring):
    while i < len(thestring):
      if thestring[i-1] == thestring[i]:
        thestring.pop(i)
      else: break
    i = i + 1
  return thestring

def solve(fegla):
  answer = 0
  # if (list(OrderedDict.fromkeys(fegla[0])) == list(OrderedDict.fromkeys(fegla[1]))):
  if (removeadjacentduplicates(fegla[0]) == removeadjacentduplicates(fegla[1])):
    lenn = max(len(fegla[0]),len(fegla[1]))
    fegla[0].extend([1]*lenn)
    fegla[1].extend([1]*lenn)
    
    x = 1
    while True:
      if ((fegla[0][x] == 1) and (fegla[1][x] == 1)): break
      while fegla[0][x] != fegla[1][x]:
        if fegla[0][x] == fegla[0][x-1]:
          fegla[0].pop(x)
        else:
          fegla[1].pop(x)
        answer = answer + 1
      x = x + 1
    return str(answer)
  else:
    return 'Fegla won'
    


fin = open(attempt + ".in", 'r')
fout = open(attempt + ".out",'w')

numcases = int(fin.readline())

for casenum in range(1,numcases+1):
  N = int(fin.readline())
  fegla = []
  for i in range(1,N+1):
    line = fin.readline()
    line = line.rstrip('\n')
    fegla.append(list(line))
  print('Case #' + repr(casenum) + ': ' + solve(fegla), file=fout)

fin.close()
fout.close()
print(time.clock())