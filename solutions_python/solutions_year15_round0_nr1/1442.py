from sys import stdin, stdout

num = int(stdin.readline()[:-1])

for i in xrange(num):
  line = stdin.readline()[:-1]
  v=line.split(' ')
  persons, levels = v[0], v[1]
  levels = [int(x) for x in levels]

  shyness = 0; shy = 0
  for l in range(len(levels)):
    if shyness  < l and levels[l] > 0:
      inc = l-shyness
      shy += inc
      shyness += inc
    shyness+=levels[l]

  print "Case #%d: %d" %(i+1, shy)
