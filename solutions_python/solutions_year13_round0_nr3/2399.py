#Fair and Square for GCJ by Kyle Parsley
from math import sqrt
a = open('C-small-attempt1.in', 'r')
b = int(a.readline()[0:3])
d , e = '', ''
result = [0 for x in range(b)]
for x in range(b):
  c = a.readline()
  d = c.split('\n')
  e = (d[0].split(' '))
  for z in range(int(e[0]), int(e[1])+1):
    w = str(z)
    q = str(sqrt(z))
    if(int(float(q))%1 == 0):
      q = q[0:(len(q)-2)]
    if((w == w[::-1]) and (q == q[::-1])):
      result[x] = result[x] + 1
counter = 1
g = open('results.out' , 'w')

for w in result:
  h = "Case #{0}: {1}\n".format(counter, w)
  print(h)
  g.write(h)
  counter = counter + 1