def isTidy(n):
  nr = str(n)
  for i in range(0, len(nr) - 1):
    if nr[i] > nr[i+1]:
      return False
    if nr[i] == 0:
      return False
    if nr[i+1] == 0:
      return False
  return True

cases = int(input())

for case in range(1, cases + 1):
  n = int(input())
  while(not(isTidy(n))):
    n -= 1
    
  print(n)