t, T = 0, int(raw_input())

while t != T:
   t += 1

   N, K = map(int, raw_input().split())
   
   if K & 2**N-1 == 2**N-1 :
      ans = 'ON'
   else:
      ans = 'OFF'

   print 'Case #%d:' % t, ans

