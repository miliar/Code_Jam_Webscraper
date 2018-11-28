m = {}
rm = {}
m['z'] = 'q'
m['q'] = 'z'
def createMap(a,b):
  for t in zip(a,b):
    m[t[0]] = t[1]

def tr(a):
  out = []
  for x in a:
    out.append(rm.get(x,x))
  return "".join(out)

createMap('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi')
createMap('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
createMap('so it is okay if you want to just give up','de kr kd eoya kw aej tysr re ujdr lkgc jv')

for k,v in m.items():
  rm[v] = k

import sys
f = sys.stdin
num_of_lines = int(f.readline())

for i in range(num_of_lines):
  sys.stdout.write( "Case #%d: %s" % (i+1, tr(f.readline())) )