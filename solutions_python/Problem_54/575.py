def gcd(a,b):
   while b:
      a, b = b, a%b
   return a

c, C = 0, int(raw_input())

while c != C:
   c += 1

   line = map(int, raw_input().split())
   N, line = line[0], line[1:]

   m = min(line)
   g = reduce(gcd, (x-m for x in line if x!=m))
   if line[0]%g == 0:
      isuck = 0
   else:
      isuck = g-(line[0]%g)

   print 'Case #%d:' % c, isuck
