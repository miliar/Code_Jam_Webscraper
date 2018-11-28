import sys
import re

def conv(num, base):
  num.reverse()
  exp = 0
  ret = 0
  for n in num:
    ret += n*pow(base, exp)
    exp += 1
  return ret

def solve_case(f):
  org_str = re.findall('[a-z0-9]', f.readline().rstrip())
  uniq = []
  for c in org_str:
    if c not in uniq:
      uniq.append(c)
  base = len(uniq)
  if base == 1:
    base = 2
  cmap = {}
  pool = [0] + range(2, base)
  print pool
  ret = []
  for c in org_str:
    if c not in cmap.keys():
      if not len(cmap):
        cmap[c] = 1
      else:
        cmap[c] = pool.pop(0)
    ret.append(cmap[c])
  # ret conv 10 alapura
  print org_str
  print cmap
  print base
  ret = conv(ret, base)
  print ret
  return ret


fin = open(sys.argv[1], 'r')
fout = open(sys.argv[1]+'.out', 'w')

for case in range(int(fin.readline().rstrip())):
  r = solve_case(fin)
  r = "Case #%s: %s" % (case+1, r)
  print r
  fout.write(r+"\n")

fin.close()
fout.close()