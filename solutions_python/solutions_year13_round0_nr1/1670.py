f = open("input", 'r')
n = int(f.readline())
t = []
for i in xrange(n):
  t.append(tuple(f.readline().strip()+f.readline().strip()+f.readline().strip()+f.readline().strip()))
  f.readline()

global nn
nn = 0
#print t
f1 = open("output1", 'w')
def match(l):
  global nn
  if l in (['T', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']):
    f1.write('Case #{0}: X won\n'.format(nn))
    return 1
  elif l in (['O', 'O', 'O', 'T'], ['O', 'O', 'O', 'O']):
    f1.write('Case #{0}: O won\n'.format(nn))
    return 1
  else:
    return 0

for p in t:
  nn += 1
  if match(sorted([p[0], p[1], p[2], p[3]])) == 1: continue
  if match(sorted([p[4], p[5], p[6], p[7]])) == 1: continue
  if match(sorted([p[8], p[9], p[10], p[11]])) == 1: continue
  if match(sorted([p[12], p[13], p[14], p[15]])) == 1: continue
  if match(sorted([p[0], p[4], p[8], p[12]])) == 1: continue
  if match(sorted([p[1], p[5], p[9], p[13]])) == 1: continue
  if match(sorted([p[2], p[6], p[10], p[14]])) == 1: continue
  if match(sorted([p[3], p[7], p[11], p[15]])) == 1: continue
  if match(sorted([p[0], p[5], p[10], p[15]])) == 1: continue
  if match(sorted([p[3], p[6], p[9], p[12]])) == 1: continue
  if '.' in p: f1.write('Case #{0}: Game has not completed\n'.format(nn))
  else: f1.write('Case #{0}: Draw\n'.format(nn))

