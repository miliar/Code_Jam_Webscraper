import sys, re
import fractions

cases = sys.stdin.readline()



for case in range(0,int(cases)):
  M = [int(x) for x in sys.stdin.readline().split()]
  L = M[0]
  t = M[1]
  N = M[2]
  C = M[3]
  a = M[4:len(M)]

  timesWithout = [0]
  for i in range(1,N+1):
    timesWithout.append(a[(i-1)%C]*2+timesWithout[i-1])
#  print timesWithout

  res = 1000000000000
  if L==0:
    res = timesWithout[N]
  if L>=1:
    for i in range(0,N):
      aktT = a[i%C]
      buildT = max(t-timesWithout[i],0)
      timeToNext = buildT+(aktT-(buildT/2.0))
      shorter = max(aktT*2-timeToNext,0)
#      print timeToNext, aktT, buildT, shorter
      if L==2:
        for j in range(i+1,N):
         aktT2 = a[j%C]
         tmpT = timesWithout[j]-shorter
         buildT2 = max(t-tmpT,0)
         timeToNext =  buildT2+(aktT2-(buildT2/2.0))
         shorter2 = max(aktT2*2-timeToNext,0)
         res = min(res,timesWithout[N]-shorter-shorter2)
      else:
        res = min(res,timesWithout[N]-shorter)

  print "Case #%d:" % (case+1), int(res)
