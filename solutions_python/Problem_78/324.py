

"""
FIRST: 
   MAX NUMBER OF GAMES WON = (G * N) number of games won
   TODAY's MAX NUMBER OF GAMES WON = (D * N)

   80*9 < (100-10) 
   (100-D) >G


   1 100 0

   (100-D) > G

   D*N

   LOWEST POSSIBLE: min(100-D)
   

for i in (1,n):
  (i * d) + ((i-n)


IF D = 0: G != 100
IF G = 100: D != < 100
IF G = 0: D != > 0
IF D > 0 < 100: G != 0 || 100

N = 100. D = 100, G = 1.  T = 10000

"""

import sys
sys.stdin.readline()
count = 0
while True:
  line= sys.stdin.readline()
  if line == "":
      break
  count = count + 1
  p = [int(x) for x in line.split(None)]
  N = p[0]
  G = p[2]
  D = p[1]
  r = "Broken"
  for n2 in range( 0, N+1):
    for n in range( n2, N+1):
      if n > 0 and (n2+.0)/n == (D+.0)/100:
        r = "Possible"
  if G == 0 and D > 0: r = "Broken"
  if G == 100 and D < 100: r = "Broken"
  print "Case #%d: %s" % ( count, r)
