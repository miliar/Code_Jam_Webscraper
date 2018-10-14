#!/usr/bin/env python

import sys

if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())
  for i in xrange(N):
    T = int(sys.stdin.readline().strip())
    trains = sys.stdin.readline().strip().split(' ')
    len_from_A = int(trains[0])
    len_from_B = int(trains[1])
    from_A = []
    for j in xrange(len_from_A):
      timing = sys.stdin.readline().strip()
      start = timing.split(' ')[0].split(':')
      start = int(start[0], 10)*60 +  int(start[1], 10)
      end = timing.split(' ')[1].split(':')
      end = int(end[0], 10)*60 +  int(end[1], 10)
      from_A.append((start, end + T))
    from_B = []
    for j in xrange(len_from_B):
      timing = sys.stdin.readline().strip()
      start = timing.split(' ')[0].split(':')
      start = int(start[0], 10)*60 +  int(start[1], 10)
      end = timing.split(' ')[1].split(':')
      end = int(end[0], 10)*60 +  int(end[1], 10)
      from_B.append((start, end + T))
    from_A.sort()
    from_B.sort()
    if False:
      print 'A:',
      for route in from_A:
        print "%d-%d" % (route[0], route[1]),
      print
      print 'B:',
      for route in from_B:
        print "%d-%d" % (route[0], route[1]),
      print

    trains_A = []
    trains_B = []
#     print trains_A, trains_B
    while len(from_A) + len(from_B) > 0:
      trains_A.sort()
      trains_B.sort()
      next = None
      if len(from_A) > 0 and len(from_B) > 0:
        if from_A[0][0] < from_B[0][0]:
          next = (from_A.pop(0), 'A', trains_A)
        else:
          next = (from_B.pop(0), 'B', trains_B)
      elif len(from_A) > 0:
        next = (from_A.pop(0), 'A', trains_A)
      elif len(from_B) > 0:
        next = (from_B.pop(0), 'B', trains_B)
      if len(next[2]) == 0 or next[0][0] < next[2][0][0]:
        # no trains here! Add one leaving here at this time
        # or no train here yet - add one leaving here at this time
        if next[1] == 'A':
          trains_B.append((next[0][1], next[1]))
        elif next[1] == 'B':
          trains_A.append((next[0][1], next[1]))
      else:
        # get the first train to take this trip back
        if next[1] == 'A':
          popped = trains_A.pop(0)
          trains_B.append((next[0][1], popped[1]))
        elif next[1] == 'B':
          popped = trains_B.pop(0)
          trains_A.append((next[0][1], popped[1]))
#       print trains_A, trains_B

    total_A = 0
    total_B = 0
    for train in trains_A + trains_B:
      if train[1] == 'A':
        total_A += 1
      elif train[1] == 'B':
        total_B += 1

    print 'Case #%d: %d %d' % (i + 1, total_A, total_B)
