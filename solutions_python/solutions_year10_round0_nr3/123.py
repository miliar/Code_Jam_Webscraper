import sys

def cumsum(l, n):
  cumsums = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    cumsums[i][0] = l[i]
    for j in range(1, n):
      cumsums[i][j] += cumsums[i][j - 1] + l[(i + j) % n]
  return cumsums

def c(j, r, k, n, g):
  cumsums = cumsum(g, n)
  ns = []
  for i in range(n):
    c = 0
    while c < n and c < k and cumsums[i][c] <= k:
      c += 1
    if c > 0:
      ns.append((c, cumsums[i][c - 1], (i + c) % n))

  idx = 0
  seen_idxs = []
  start_idx = 0
  for i in range(r):
    seen_idxs.append(idx)
    idx = ns[idx][2]
    if idx in seen_idxs:
      start_idx = idx
      break
      
  e_tot = 0
  
  #prerepetition
  idx = 0
  num_rides = 0
  if start_idx != 0:
    for i in range(r):
      if idx == start_idx:
        break
      e_tot += ns[idx][1]
      idx = ns[idx][2]
    num_rides = i
  
  #repetition
  rep_len = len(seen_idxs) - seen_idxs.index(start_idx)
  e = 0
  for i in range(rep_len):
    e += ns[idx][1]
    idx = ns[idx][2]
  reps, rest = divmod(r - num_rides, rep_len)
  e_tot += e * reps

  #postrepetition
  for i in range(r - rep_len * reps - num_rides):
    e_tot += ns[idx][1]
    idx = ns[idx][2]
    
  print 'Case #%d: %d' % (j, e_tot)

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for j in range(1, t + 1):
      r, k, n = (int(x) for x in f.readline().split())
      g = [int(x) for x in f.readline().split()]
      c(j, r, k, n, g)
