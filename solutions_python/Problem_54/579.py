#!/usr/bin/python2.4
from decimal import *
getcontext().prec = 100;
f = file('in','r');
cs = int(f.readline());
for step in range(cs):
  s = f.readline().split(' ');
  n = int(s[0]);
  a = [];
  for i in s[1:]:
    a.append(Decimal(i));
  a.sort()
  ans = Decimal('0')
  for i in a[1:]:
    b = i - a[0]
    if ans == Decimal('0'):
      ans = b;
    else:
      x = ans;
      y = b;
      while (y != Decimal('0')):
        r = x % y;
        x = y;
        y = r;
      ans = x;
  if (a[0] % ans) == Decimal('0'):
    ans = 0;
  else:
    ans = ans - (a[0]%ans);
  print "Case #" + str(step+1) + ": " + str(ans)
print
