import math

#f = open('B.in', 'r')
f = open('B-large.in', 'r')
T = int(f.readline())
for testCase in range(1, T+1):
  (B, N) = map(int, f.readline().split())
  M = map(int, f.readline().split())

  low = 1
  high = N * max(M)

  while (True):
    mid = (low + high) / 2 # make sure always converges
    numCut = 0
    for i in range(B):
      numCut += math.ceil(float(mid) / float(M[i])) # auto floor
      #if (mid % M[i]):
      #  numCut += 1

    if (high - low) <= 1:
      break

    if (numCut >= N):
      high = mid
    elif (numCut < N):
      low = mid

  numCut = 0
  for i in range(B):
    numCut += math.ceil(float(low) / float(M[i])) # auto floor
  #print "low = %d, numCut = %d" % (low, numCut)
  lowNumCut = numCut

  numCut = 0
  for i in range(B):
    numCut += math.ceil(float(high) / float(M[i])) # auto floor
  
#  print "high = %d, numCut = %d" % (high, numCut)
  highNumCut = numCut

  #print "number to cut this round %d" % (N - lowNumCut)
  target = N - lowNumCut
  if (target == 0):
    target = N
  cutSoFar = 0
  for i in range(B):
    if (low % M[i] == 0):
      cutSoFar += 1

    if (cutSoFar == target):
      print "Case #%d: %d" % (testCase, i+1)
      break




  


