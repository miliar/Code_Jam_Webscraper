#!/usr/bin/python
import sys
import string

# Open in- and output files
f = "" if len(sys.argv) < 2 else sys.argv[1]
i = open(f, 'r')
o = open("%s.out" % f, 'w')

# Parse input file
cases = int(i.readline())

for case in range(1, cases + 1):  
  # chunks = i.readline().strip().split(" ")
  # OR
  # value = int(i.readline())

  X, S, R, t, N = i.readline().strip().split(" ")
  
  min_time = float(X) / float(S)
  print min_time
  
  walkways = []
  w_dist = 0
  for n in range(0,int(N)):
    Bi, Ei, wi = i.readline().strip().split(" ")
    di = int(Ei) - int(Bi)
    w_dist += di
    walkways.append((int(Bi), int(Ei), int(wi), di))

  print walkways

  # sort afgter velocity
  walkways.sort(None, lambda elem : elem[2])

  X = float(X)
  R = float(R)
  S = float(S)
  t = float(t)

  n_dist = X - w_dist
  
  dist_done = 0
  time_done = 0
  
  t_n = n_dist / R
  
  if t >= t_n:
    time_done += t_n
    t -= t_n
    dist_done = n_dist
  else:
    d_rest = n_dist - (t * R)
    dist_done = n_dist
    time_done += t + float(d_rest) / S
    t = 0
  
  for cur in walkways:
    t_needed = float(cur[3]) / (R + float(cur[2]))
    if t >= t_needed:
        dist_done += float(cur[3])
        t -= t_needed
        time_done += t_needed
    else:
        d_rest = float(cur[3]) - (R + float(cur[2])) * t

        dist_done += float(cur[3])
        time_done += t + d_rest / (S + float(cur[2]))
        t = 0        
  
  print walkways
  result = "Case #%i: %s" % (case, time_done)
  print result
  o.write("%s\n" % result)

# Close in- and output
i.close()
o.close()
