from __future__ import division

def solve(input):
  D = int(input.split(' ')[0])
  N = int(input.split(' ')[1])
  horses = []
  for i in range(N):
    l = raw_input()
    horses.append((int(l.split(' ')[0]), int(l.split(' ')[1])))

  maxtime = 0
  for horse in horses:
    dist = D - horse[0]
    time = dist/horse[1]
    if time > maxtime:
      maxtime = time

  return str(D/maxtime)

T = int(raw_input())
for i in range(T):
  print 'Case #' + str(i+1) + ': ' + solve(raw_input())