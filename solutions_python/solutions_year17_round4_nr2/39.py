import os
import math



def solve(N, C, M, tickets):
  min_rides = 0
  tickets_per_buyer = {}
  position_counts = [0] * N
  for (P, B) in tickets:
    if B not in tickets_per_buyer:
      tickets_per_buyer[B] = 0
    tickets_per_buyer[B] += 1
    position_counts[P] += 1
  for B in tickets_per_buyer:
    min_rides = max(min_rides, tickets_per_buyer[B])
  current_tickets = 0
  for i in range(N):
    current_tickets += position_counts[i]
    min_rides = max(min_rides, (current_tickets+i) / (i+1))

  min_switch = 0
  for i in range(N):
    if position_counts[i] > min_rides:
      min_switch += position_counts[i] - min_rides

  return '%s %s' % (min_rides, min_switch)


fin = open('B-large (2).in', 'r')
fout = open('B.out', 'w')
nown = 0
nowt = 0
t = int(fin.readline())
for nowt in range(t):
  nowt += 1
  line = fin.readline()
  N, C, M = line.split()
  N = int(N)
  C = int(C)
  M = int(M)
  tickets = []
  for i in range(M):
    line = fin.readline()
    P, B = line.split()
    tickets.append((int(P)-1, int(B)-1))

  result = solve(N, C, M, tickets)

  out_str = 'Case #%d: %s\n' % (nowt, result)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()
