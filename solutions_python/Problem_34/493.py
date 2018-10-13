
filename = 'A-large.in'
text = open(filename)

L,D,N = [int(x) for x in text.readline().strip().split(' ')]

D = [text.readline().strip() for x in range(D)]

N = [text.readline().strip() for x in range(N)]
N = [n.replace('(','[').replace(')',']') for n in N]

output = open('A-large.out','w')

import re

for i,n in enumerate(N):
  validCount = 0
  r = re.compile('^'+n+'$')
  for d in D:
    if r.match(d):
      validCount += 1
  output.write('Case #%s: %s'%(i+1,validCount)+'\n')
