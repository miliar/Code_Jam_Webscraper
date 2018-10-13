from math import *
T = int(raw_input())
for test in range(1, T+1):
   (r, t) = map(int, raw_input().split(' ') )
   x = int( ( sqrt( (2*r-1)**2  +8*t) - (2*r-1) ) / 4.0  )
   print ('Case #{0:d}: {1:d}'.format(test, x))
