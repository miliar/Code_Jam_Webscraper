import io, os, sys

file_ = open(sys.argv[1])

T = int(file_.readline())

def calc(n):
  A = []
  a = str(n)
  for i in range(len(a)):
    A.append(int(a[i]))
  #print A
  l = len(A)
  for i in range(l-1):
    if  A[l-i-1] < A[l-i-2]:
      for j in range(l-i-1,l):
        A[j] = 9
      A[l-i-2] = A[l-i-2] - 1
  if A[0] == 0:
    del A[0]
  a = ''
  for i in range(len(A)):
    a += str(A[i])
  return long(a)


def tidy(n):
  A = []
  a = str(n)
  for i in range(len(a)):
    A.append(int(a[i]))
  for i in range(len(A)-1):
    if A[i] > A[i+1]:
      return False
  return True 


def calLastTidy(n):
  for i in range(n):
    if tidy(n-i):
      return n-i
  return 0

'''
for i in range(10000):
  a = calLastTidy(i+1)
  b = calc(i+1)
  if a != b:
    print "ERROR", (i+1)
'''

for i in range(T):
  a = long(file_.readline())
  print "Case #"+ str(i+1) + ": " + str(calc(a))


