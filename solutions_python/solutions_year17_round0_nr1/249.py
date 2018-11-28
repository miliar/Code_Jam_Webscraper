from sys import stdin
t  = int(stdin.readline())
for ca in xrange(1,t+1):
 a,kk = stdin.readline().strip().split()
 kk = int(kk)
 ans = 0
 a = list(a)
 n = len(a)
 for i in xrange(n):
  j = i + kk - 1
  if j>=n:
   break
  if a[i]=='-':
   ans += 1
   for k in xrange(i,j+1):
    if a[k]=='-':
     a[k] = '+'
    else:
     a[k] = '-'
 if a!= ['+'] * n:
  ans = 'IMPOSSIBLE'
 print "Case #{}: {}".format(ca,ans)
