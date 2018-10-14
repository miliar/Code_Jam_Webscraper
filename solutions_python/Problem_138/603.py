import math
from bisect import bisect

fin = open( 'D.in', 'rb' )
fout = open ( 'D.out', 'wb' )

t = int( fin.readline() )

for x in range(t):
  # reading
  n = int( fin.readline() )
  
  line = fin.readline()
  NAOMI = eval( '[%s]' % line.replace(' ', ',' ) )
  NAOMI.sort()

  line = fin.readline()
  KEN = eval( '[%s]' % line.replace(' ', ',' ) )
  KEN.sort()

  # processing
  y = 0
  z = 0

  # War playing
  naomi = list(NAOMI)
  ken = list(KEN)

  for i in range(n):
    pos = bisect(ken, naomi[i])
    if pos >= ( n-i ):
      del ken[0]
      z += 1
    else:
      del ken[pos]

  # Dec War playing
  naomi = list(NAOMI)
  ken = list(KEN)

  while True:
    if naomi == []:
      break

    if naomi[-1] < ken[-1]:
      # can't win, just consume Ken's heaviest block
      del naomi[0]
      del ken[-1]
    else:
      # can win, score 1 point
      del naomi[-1]
      del ken[-1]
      y += 1

  line = 'Case #%d: %d %d\n' % (x+1, y, z)
  fout.write(line)

fin.close()
fout.close()

