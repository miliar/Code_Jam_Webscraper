def solve( line ):
   plaintext = "abcdefghijklmnopqrstuvwxyz "
   cipher    = "ynficwlbkuomxsevzpdrjgthaq "

   result = ""
   for c in line:
      pos = cipher.find(c)
      if pos >= 0:
         result += plaintext[pos]
   return result

from sys import stdin

T = int( stdin.readline() )
for i in range(T):
   line = stdin.readline()
   print "Case #{}: {}".format( i+1, solve( line ) )
