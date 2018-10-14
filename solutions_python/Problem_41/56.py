#!/usr/bin/env python
def sortString(N):
  chars = []
  for i in range(len(N)):
    chars += [N[i]]
  chars.sort()
  result = ""
  for char in chars:
    result += char
  return result
  
def checkIfLast(N):
  i = 0
  while i<len(N)-1:
    if N[i] < N[i+1]:
      return False
    i += 1
  return True

def solve(N):
  if checkIfLast(N):
    minc = N[0]
    minj = 0
    j = 1
    while j < len(N):
      if N[j] < minc and N[j] != '0':
        minc = N[j]
        minj = j
      j += 1
    result = N[minj]
    result += sortString("0" + N[0:minj] + N[minj+1:])
    print result
    return
  i=0
  while i < len(N):
    if(checkIfLast(N[i:])):
       break
    i += 1
  result = N[0:i-1]
  j = i
  minj = i
  minc = N[minj]
  while j < len(N):
    if(N[j] > N[i-1] and N[j] < minc):
      minj = j
      minc = N[minj]
    j += 1
  result += N[minj]
  result += sortString(N[i-1] + N[i:minj] + N[minj+1:])
  print result
T = int(raw_input())
for i in range(T):
  print "Case #%d:" % (i+1),
  N = raw_input()
  solve(N)
