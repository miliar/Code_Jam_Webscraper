import sys

sys.setrecursionlimit(12000)

#f = open('test', 'r')
f = open('B-large.in', 'r')

T = int(f.readline())

def answery(n, p):
  if p == 2**n:
    return 2**n - 1
  if p <= 2**(n-1):
    return 0
  if n == 0:
    return 0
  return 2*answery(n-1, p - 2**(n-1)) + 2

def answerz(n, p):
  if p == 2**n:
    return 2**n - 1
  return (2**n - 1) - answery(n, 2**n - p) - 1

for test in range(1, T+1):
  line = f.readline()
#  print line.split()
  n, p = [int(num) for num in line.split()]
  
  print 'Case #' + str(test) + ': ' + str(answery(n,p)) + ' ' + str(answerz(n,p))
