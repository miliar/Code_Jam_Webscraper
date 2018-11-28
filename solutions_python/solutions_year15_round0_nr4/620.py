import sys
import math

lines = sys.stdin.read().split('\n')

for k in range( 0, int(lines[0]) ):
  vec1 = map( int, lines[k+1].split(' ') )

  x = vec1[0]
  r = vec1[1]
  c = vec1[2]

  if x == 1:
    result = 'GABRIEL'
  elif x == 2:
    if (r*c)%2==1:
      result = 'RICHARD'
    else:
      result = 'GABRIEL'
  elif x == 3:
    if min(r,c) == 1 or (r*c)%3 != 0:
      result = 'RICHARD'
    else:
      result = 'GABRIEL' #
  elif x == 4:
    if (r*c)%4 != 0 or min(r,c)<3 or max(r,c)<4:
      result = 'RICHARD'
    else:
      result = 'GABRIEL'
  elif x == 5:
    if (r*c)%5 != 0 or min(r,c)<3 or max(r,c)<5:
      result = 'RICHARD'
    else:
      result = 'GABRIEL'
  elif x == 6:
    if (r*c)%6 != 0 or min(r,c)<3 or max(r,c)<6:
      result = 'RICHARD'
    else:
      result = 'GABRIEL'
  elif x > 6:
    result = 'RICHARD'
 
  sys.stdout.write( 'Case #' + str(k+1) + ': ' )

  print( result )

