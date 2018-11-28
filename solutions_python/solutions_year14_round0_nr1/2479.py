from codejam import *

from collections import defaultdict

def ff():
  a0 = read_int()
  b0 = []
  for i in range(4):
    b0.append(read_int_list())

  a1 = read_int()
  b1 = []
  for i in range(4):
    b1.append(read_int_list())

  r0 = b0[a0-1]
  r1 = b1[a1-1]

  c = defaultdict(int)

  for i in r0 + r1:
    c[i] += 1

  ans = []
  for k,v in c.iteritems():
    if v == 2:
      ans.append(k)

  #print r0, r1, ans
  if len(ans) == 1:
    return ans[0]
  elif len(ans) == 0:
    return 'Volunteer cheated!'
  else:
    return 'Bad magician!'

  
T=read_int()
for t in xrange(1, T+1):
  print 'Case #%d: %s' % (t, str(ff()))
