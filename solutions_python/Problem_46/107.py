filename = 'A-small-attempt0'

cache = {}

def min_ways(vals, n):
  if n == 0:
    return 0 
  s = '\n'.join([x[:n] for x in vals[:n]])
  if s in cache:
    return cache[s]
  best = 1 << 30
  for i in range(n):
    all_good = True
    for j in range(n):
      if j != i and vals[j][n-1] == '1':
        all_good = False
        break

    if not all_good:
      continue

    val = vals[i]
    vals = vals[:i] + vals[i+1:]
    vals.insert(n-1, val)

    res = min_ways(vals, n - 1)
    best = min(best, n - 1 - i + res)

    val = vals[n - 1]
    vals = vals[:n-1] + vals[n:]
    vals.insert(i, val)
  
  cache[s] = best
  return best
  

f = open(filename + '.in', 'r')
lines = f.readlines()
f.close()

out = open(filename + '.out', 'w')
T = int(lines[0])
linenum = 1
for case in range(1, T + 1):
  N = int(lines[linenum])
  vals = [0]*N
  for i in range(N):
    vals[i] = lines[linenum + i + 1].strip()
  linenum += N + 1
  print vals
  cache = {}
  res = min_ways(vals, N)
  print res
  print '--------------------------------------------------'
  out.write('Case #%d: %d\n' % (case, res))

out.close()
