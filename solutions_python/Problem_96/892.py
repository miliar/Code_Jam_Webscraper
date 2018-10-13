import sys

t = int(sys.stdin.readline());

for i in range(0, t):
  line = sys.stdin.readline()
  data = line.split()
#  print data
  n = int(data[0])
  s = int(data[1])
  p = int(data[2])
  t = []
  for j in range(0, n):
    t.append(int(data[3 + j]))

#  print n, s, p, t

  def hasBest(a, b, c):
    for k in range(0, c + 1):
      if a >= b * 3 - k and a >= b:
        return True
    return False

  y = 0
  u = []
  for j in range(0, n):
    if not hasBest(t[j] , p, 2):
      u.append(t[j])
    else:
      y = y + 1

  t = u
  for j in range(0, len(t)):
    if hasBest(t[j], p,  4) and s >= 1:
      y = y + 1
      s = s - 1


  print "Case #" + str(i+1) + ": " + str(y)

