import sys

def candy_split(t, c) :
   r1 = c[0]
   r2 = r1
   for x in c[1:] :
      r1 ^= x
      r2 += x
   if r1 == 0 :
      return r2 - min(c)
   else :
      return 'NO'

if __name__ == '__main__' :
   n = int(sys.stdin.readline())
   i = 1
   while i <= n :
      t = int(sys.stdin.readline())
      c = [int(x) for x in sys.stdin.readline().split()]
      print 'Case #%d:' % (i), candy_split(t, c)
      i += 1
