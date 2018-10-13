t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, K = [int(s) for s in raw_input().split()]
  P = 1
  Max = N
  Min = N-1
  maxcount = 1
  while P * 2 <= K:
    Max /= 2
    Min = Max - 1
    N -= P
    P *= 2
    maxcount = N - Min * P
  if K - P < maxcount:
    Min = (Max - 1) / 2
    Max = Max / 2
  else:
    Max = Min / 2
    Min = (Min - 1) / 2
  print "Case #"+str(i)+": "+ str(Max) + " " + str(Min)
