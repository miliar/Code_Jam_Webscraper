T = int(raw_input())

for i in range(T):
 n, k = map(int, raw_input().split())
 k %= 2 ** n
 print "Case #%d:" % (i+1), 
 if k == 2**n-1:
   print "ON"
 else:
   print "OFF"
