t = int(input())
def isTinyNumber(num):
  num = str(num)
  for i in range(len(num)-1):
    if int(num[i]) > int(num[i+1]):
      return False
  return True
for i in range(t):
  n = int(input())
  while not isTinyNumber(n):
    n -= 1
  print('Case #{0}: {1}'.format(i+1, n))
