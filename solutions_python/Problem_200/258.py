from sys import stdin
di = '123456789'
def solve(a):
 ans = ''
 l = len(a)
 n = int(a)
 fir = int('1'*l)
 if fir > n:
  return int('9' * (l-1) )
 pr = 0
 rem = l
 for _ in xrange(l):
  j = 8
  while j>=pr:
   cur = ans + di[j] * rem
   cur = int(cur)
   if cur <= n:
    ans += di[j]
    pr = j
    rem-=1
    break
   j-=1
 return int(ans)



t  = int(stdin.readline())
for ca in xrange(1,t+1):
 a = stdin.readline().strip()
 print "Case #%d: %d"%(ca,solve(a))
