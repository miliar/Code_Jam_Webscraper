import io, os, sys

file_ = open(sys.argv[1])
T = int(file_.readline())

def reduce(A):
  while A[0] == 0:
    del A[0]
    if len(A) == 0:
      return []
  return A

def calc(A,n):
  count = 0
  while True:
    A = reduce(A)
    if len(A) == 0:
      return count
    if len(A) < n:
      return -1
    for i in range(n):
      A[i] = (A[i]+1) % 2
    count += 1


for i in range(T):
  s = file_.readline()
  A = s.split(" ")
  n = int(A[1])
  B = []
  for j in range(len(A[0])):
    a = 1 if A[0][j] == '-' else 0
    B.append(a)
  ret = calc(B,n)
  print 'Case #'+ str(i+1)+  ': ' + str('IMPOSSIBLE' if ret == -1 else ret) 


