import sys

cases = int(sys.stdin.readline())
for case in range(1,cases+1):
  line =  sys.stdin.readline()
  smax,k = line.split()

  maxMissing = 0
  currentMissing = 0
  currentHaving = int(k[0])
  for i in range(1, len(k)):
    ith = int(k[i])
    currentMissing = i - currentHaving
    currentHaving = currentHaving + ith
    maxMissing = max(maxMissing, currentMissing)
  print "Case #%s: %d" %(case, maxMissing)