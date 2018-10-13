#!/usr/bin/python

from sys import stdin

def rollercoaster_case(g, k, R):
  N = len(g)
  earned = []
  next   = []

  # Index the groups by range and successor.
  for idx in range(0, N):
    count = 0
    i     = idx

    # Count the max. possible occupants from this index.
    while True:
      if count + g[i] <= k:
        count += g[i]
      else:
        break      # We can't pack the next group in.
        
      i += 1
      
      if i == N:   # Wrap around the queue is necessary.
        i = 0
      if i == idx: # Make sure we don't load the same group again.
        break
    
    # Log the successor index and amount earned.
    earned.append(count)
    next.append(i)

  # Iterate the test case.
  idx = 0
  earnings = 0
 
  # Run 'R' groups through the ride.  
  for _ in range(0, R):
    earnings += earned[idx]
    idx = next[idx]

  return earnings

# Read in all of the test cases.
num_cases = int(stdin.readline())

for n in range(0, num_cases):
  R, k, N = map(int, stdin.readline().split())
  g = map(int, stdin.readline().split())
  print 'Case #' + str(n + 1) + ': ' + str(rollercoaster_case(g, k, R))
