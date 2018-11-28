def isTidy(a):
  isTidy = True;
  for i in xrange(0, len(a)-1):
    isTidy = isTidy & (a[i] <= a[i+1])
  return isTidy

def getFirstNonTidyIndex(n):
  a = 0
  while (n[a] <= n[a+1]):
    a += 1
  return a+1

def toArray(n):
  return [int(d) for d in str(n)]

def getSmallestSame(n, i):
  while (i > 0) & (n[i] == n[i-1]):
    i = i -1
  return i

def getNextLargestTidy(n):
  i = getFirstNonTidyIndex(n)
  i2 = getSmallestSame(n, i-1)
  n[i2] = n[i2]-1
  for i in xrange(i2+1, len(n)):
    n[i] = 9

def toInteger(arrayN):
  s = ""
  for i in xrange(0,len(arrayN)):
    s += str(arrayN[i])
  return int(s)

def largestTidy(n):
  arrayN = toArray(n)
  if(isTidy(arrayN)):
    return n
  else:
    getNextLargestTidy(arrayN)
    return toInteger(arrayN)

numLines = int(raw_input())
for i in xrange(0, numLines):
  n = int(raw_input())
  answer = largestTidy(n)
  print('Case #{}: {}'.format(i+1, answer))
