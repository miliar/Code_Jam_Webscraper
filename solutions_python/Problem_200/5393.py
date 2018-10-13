import sys

counter = 10000
sys.setrecursionlimit(10000000)

def f(N):
  global counter
  sN = str(N)
  #print counter, ' s ', sN
  
  isValid = 1
  for position, item in enumerate(sN):
    if position<len(sN)-1 and isValid == 1:
      if position < len(sN)-1 and sN[position] <= sN[position+1]:
        isValid = 1
      else:
        isValid = 0
      
  if isValid == 1:
    return N
  elif counter > 0 and isValid==0:
    counter-=1
    return f(N-1)
  

t = int(raw_input())

for i in xrange(1, t + 1):
  number = int(raw_input())
  val = f(number)
  #print 'Case #' + i +':' + val
  print 'Case #{}: {}'.format(i,val)