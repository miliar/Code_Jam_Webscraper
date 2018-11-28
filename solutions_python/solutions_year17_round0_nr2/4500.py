def f(n):
  if len(n) == 1:
    return "".join(n)
  pointer = len(n) -1 
  sub1 = False
  resultArray = []

  while pointer > 0:
    lastDigit = int(n[pointer])
    compareTo = int(n[pointer - 1])
    if sub1:
      lastDigit = int(lastDigit) - 1
      sub1 = False
    if lastDigit < compareTo:
      resultArray += ['9']
      sub1 = True
    else:
      resultArray += [str(lastDigit)]
    pointer-=1

  lastDigit = n[0]

  if sub1:
    lastDigit = int(lastDigit) - 1
    resultArray = get(len(resultArray))

  if lastDigit != 0:
    resultArray +=[str(lastDigit)]
  return "".join(resultArray[::-1])
  

def get(L):
  return ['9' for i in range(L)]

tc = int(raw_input())
for t in range(1, tc+1):
  N = list(raw_input())
  print "Case #"+str(t)+": "+str(f(N))
