import math
import sys
import re
ipf = open (sys.argv[1], 'r')
opf = open (sys.argv[2], 'w')
T = int (ipf.readline())
for t in range (1,T+1):
  r,c = map (int,ipf.readline().split())
  tiles = []
  nbtiles = 0
  for i in range(0,r):
    tiles.append(ipf.readline().strip())
    nbtiles += tiles[i].count('#')
  if nbtiles%2 == 1:
    opf.write("Case #%d:\nImpossible\n" %t)
    print "Impossible"
    continue
  broken = 0
  for i in range(0,r-1):
    nbtiles = []
    for j in range(0,r):
      nbtiles.append(tiles[i].count('#'))
      if nbtiles[j]%2 == 1:
        opf.write("Case #%d:\nImpossible\n" %t)
        print "Impossible"
        broken = 1
        break
    if broken == 1:
      break
    n = nbtiles[i]/2
    n1 = nbtiles[i+1]/2
    for j in range(0,c-1):
      print (i,j)
      if tiles[i][j] == '#':
        if tiles[i][j] == tiles[i+1][j] and tiles[i][j+1] == tiles[i+1][j+1]:
          t1 =""
          t2 =""
          print r
          for k1 in range(0,c):
            if k1==j:
              t1 = t1 + "/"
              t2 = t2 + "\\"
            elif k1 == j+1:
              t1 = t1 + "\\"
              t2 = t2 + "/"
            else:
              t1 =t1+ tiles[i][k1]
              t2 = t2+ tiles[i+1][k1]
          tiles[i] = t1
          tiles[i+1] = t2
          print t1
          print t2
          print tiles
          print map(lambda i:len(tiles[i]),range(0,r))
        else:
          opf.write("Case #%d:\nImpossible\n" %t)
          broken=1
          break
    if broken == 1:
      break
  if broken == 1:
    continue
  opf.write ("Case #%d:\n" % t)
  for i in range(0,r):
    opf.write(str(tiles[i]) + "\n")
ipf.close()
opf.close()
