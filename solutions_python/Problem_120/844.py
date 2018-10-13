import math
f = open('At2')

num_cases = int(f.next())
for T in range(1,num_cases+1):
  n = f.next().split(' ')
  r = long(n[0])
  t = long(n[1])

  ans = int(( -(2*r-1) + math.sqrt((2*r-1)**2 + 8*t) ) / 4)

  if 2*ans**2 + (2*r-1)*ans > t:
    ans -= 1

  print "Case #%s: %s" % (T, ans)
