def f(x, r, c):
  if r * c % x != 0:
    return False
  if x == 1:
    return True
  if x == 2:
    return True 
  if x == 3:
    return min(r, c) >= 2
  if x == 4:
    return min(r, c) >= 3
     

Z = int(raw_input())
for z in range(Z):
  x, r, c = map(int, raw_input().strip().split())
  print "Case #%d: %s" % (z + 1, "GABRIEL" if f(x, r, c) else "RICHARD")
