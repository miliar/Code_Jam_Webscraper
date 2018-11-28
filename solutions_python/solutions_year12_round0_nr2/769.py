def solve( N, S, p, t ):
   count = 0
   for i in t:
      x, y = divmod( i, 3 )

      # Edge cases
      if i == 0:
         if p <= 0: count += 1
         continue
      elif i == 1:
         if p <= 1: count += 1
         continue
      elif i == 29:
         if p <= 9: count += 1
         continue
      elif i == 30:
         if p <= 10: count += 1
         continue

      if y == 0:
         if x >= p:
            count += 1
         elif S > 0 and x+1 >= p:
            S -= 1
            count += 1
      elif y == 1:
         if x+1 >= p:
            count += 1
      else: #y == 2
         if x+1 >= p:
            count += 1
         elif S > 0 and x+2 >= p:
            S -= 1
            count += 1
   return count

from sys import stdin
T = int( stdin.readline() )
for i in range(T):
   tokens = [ int(j) for j in stdin.readline().split() ]
   N = tokens[0]
   S = tokens[1]
   p = tokens[2]
   t = tokens[3:]
   #print "N={}, S={}, p={}, t={}".format( N, S, p, t )
   print "Case #{}: {}".format( i+1, solve( N, S, p, t ) )
