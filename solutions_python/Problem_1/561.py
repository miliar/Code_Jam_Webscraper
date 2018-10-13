import sys

def stripline(): return sys.stdin.readline().rstrip()
def parseline(): return sys.stdin.readline().rstrip().split(" ")

names = {}

N = int(parseline()[0])
for i in range(N):
  S = int(parseline()[0])
  names.clear()
  for k in range(S):
    names[stripline()] = 0

  Q = int(parseline()[0])
  n = 0
  switches = 0
  for k in range(Q):
    name = stripline()
    if names[name] == 0:
      names[name] = 1
      n += 1
      if n >= S:
        for key in names.keys():
          names[key] = 0
        names[name] = 1
        n = 1
        switches += 1
  
  print "Case #"+str(i+1)+": "+str(switches)
