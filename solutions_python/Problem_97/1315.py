import sys

def solveProblem():
  line = sys.stdin.readline().split()
  a = int(line[0])
  b = int(line[1])
  
  out = []

  for i in range(a,b+1):
    stri = str(i)
    for j in range(1,len(stri)):
      strj = stri[-j:]+stri[:-j]
      if int(strj) <= b and int(strj) >= a and int(strj) > i:
        out.append((i, stri[-j:]+stri[:-j]))
  out = set(out)
  return len(out)

pcount = int(sys.stdin.readline())

for i in range(1, 1+pcount):
  print "Case #"+str(i)+":", solveProblem()
