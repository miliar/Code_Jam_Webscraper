def solve(X, R, C):
  if X == 1:
    return 'GABRIEL'
  elif X == 2:
    if (R*C) & 0x1:
      return 'RICHARD'
  elif X == 3:
    if R == 1 or C == 1 or (R*C)%X!=0 or (X>C and X>R):
      return 'RICHARD'
  else:
    if (R == 4 and C == 2) or (C == 4 and R == 2):
      return 'RICHARD'
    if R == 1 or C == 1 or (R*C)%X!=0 or (X>C and X>R):
      return 'RICHARD'

  return 'GABRIEL'

f = open('D-small-attempt4.in', 'r')
#f = open('test.in', 'r')
T = int(f.readline())
for i in range(T):
  X, R, C = map(int, f.readline().split())
  print 'Case #%d: %s' % (i+1, solve(X, R, C))
