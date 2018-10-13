import sys

def stripline(): return sys.stdin.readline().rstrip()
def parseline(): return stripline().split(" ")

N = int(parseline()[0])
for i in range(N):
  line = parseline()
  (P,K,L) = (int(line[0]),int(line[1]),int(line[2]))
  letters = []
  line = parseline()
  for k in range(L):
    letters.append(int(line[k]))
  letters.sort(reverse=True)
  
  keys = []
  for k in range(K):
    keys.append(0)
  
  presses = 0
  impossible = 0
  for x in letters:
    mi = 2000
    best = 0
    for k in range(K):
      num = keys[k]
      if num < mi and num < P:
        mi = num
        best = k
    
    if mi == 2000:
      impossible = 1
      break
    
    keys[best] += 1
    presses += keys[best]*x
  
  if impossible == 1:
    print "Case #"+str(i+1)+": Impossible"
  else:
    print "Case #"+str(i+1)+": "+str(presses)
