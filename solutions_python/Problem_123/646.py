from sys import stdin

def split(a, m):
   less = []
   more = []
   for i in m:
      if i < a:
         less += [i]
      else:
         more += [i]
   return less, more

def solve(A, M):

   #print A, M
   if len(M) == 0:
      return 0

   op = 0
   a = A
   m = M
   while len(m) > 0 and op < len(M):
      less, more = split(a, m)
      #print a, less, more
      if len(less) > 0:
         a += sum(less)
         m = more
      else:
         a1 = 2*a - 1
         m1 = m[:]
         m.remove(max(m))
         if a1 == a:
            op += 1 + solve(a, m)
         else:
            op += 1 + min(solve(a1, m1), solve(a, m))         

         #print a, less, more

         # least = min(m)
         # a += a - 1
         # if a > least:
         #    op += 1
         # else:
         #    #op += len(m)
         #    return op + len(m)
         #op += 1
   return op

T = int(stdin.readline())
for t in range(T):
   A, N = map(int, stdin.readline().split())
   M = map(int, stdin.readline().split())
   print "Case #{}: {}".format((t+1), solve(A, M))
