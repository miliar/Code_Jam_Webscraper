#!/usr/bin/python

import sys

def resolve(D, horses):
  t = 0
  horses.sort(key=lambda h: h[0])

  while len(horses) > 1:
    collisions = []
    i = 0
    # find the collision times
    while i+1 < len(horses):
      if horses[i][1] > horses[i+1][1]:
        t = (horses[i+1][0]-horses[i][0])/(horses[i][1]-horses[i+1][1])
        d = horses[i][0] + horses[i][1]*t
        if d < D:
          collisions.append((i,t))
        i += 1
      else:
        # no collision for these horses, remove the fastest
        del horses[i+1]

    if len(collisions):
      # the horses causing the first collision can be removed, it will follow
      # the next one
      collisions.sort(key=lambda c: c[1])
      del horses[collisions[0][0]]
    else:
      break

  return horses[0][1] * D / (D - horses[0][0])

    

dataset=open(sys.argv[1], 'r')
T=int(dataset.readline())
for t in xrange(1,T+1):
  (D,N)=map(int, dataset.readline().strip().split())
  D = float(D)
  horses = []
  for i in xrange(N):
    horses.append(map(float, dataset.readline().strip().split()))
  print "Case #%d: %f"%(t, resolve(D, horses))
