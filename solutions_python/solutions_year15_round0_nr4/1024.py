import math
     
IN = open("in", 'r')
OUT = open("out", 'w')

n = IN.readline()
for x in xrange(1, int(n)+1):
  D = map(int, IN.readline().strip().split(' ')) 
  X = D[0]
  R = D[1]
  C = D[2]
  p1 = "GABRIEL"
  p2 = "RICHARD"
  winner = p1
  area = R * C
  maxL = R + C
  hX = X/2.0
  if (X > 6) or (area < X) or (area % X != 0) or (hX > R) or (hX > C) or (X > R and X > C) or (X == 4 and (R==2 or C==2)):
    winner = p2
  
  
  outline = "Case #" + str(x) + ": " + winner + "\n"
  print outline

  OUT.write(outline)


OUT.close()
IN.close()
