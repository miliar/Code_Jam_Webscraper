#!/usr/bin/python

fname = 'B-small'

base = 'QWERASDF'

def solve(s):
  print '==='
  s = s.split(' ')
  combines = {}
  for e in base: combines[e] = {}
  opposed = {}
  for e in base: opposed[e] = []
  def newUsed():
    used = {}
    for e in base: used[e] = 0
    return used
  C = int(s[0])
  for i in xrange(1, 1+C):
    comb = s[i]
    combines[comb[0]][comb[1]] = comb[2]
    combines[comb[1]][comb[0]] = comb[2]
  D = int(s[1+C])
  for i in xrange(1+C+1, 1+C+1+D):
    op = s[i]
    opposed[op[0]] = op[1]
    opposed[op[1]] = op[0]
  L = int(s[1+C+1+D])
  s = s[1+C+1+D+1][:L]
  used = newUsed()
  res = []
  for e in s:
    print used, res, e
    if len(res) > 0:
      prev = res[-1]
      if prev in base and e in combines[prev]:
        res[-1] = combines[prev][e]
        used[prev] -= 1
        continue
    res.append(e)
    for op in opposed[e]:
      if used[op]:
        res = []
        used = newUsed()
        break
    else: used[e] += 1
  return '['+', '.join(res)+']'

fin = file(fname+'.in')
T = int(fin.readline().strip())
fout = file(fname+'.out', 'w')
for i in xrange(T):
  fout.write('Case #%s: %s\n' %(i+1, solve(fin.readline())))

