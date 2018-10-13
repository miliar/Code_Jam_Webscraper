
def calculate(n, s, p, scores):
  sure = 0
  maybe = 0
  for score in scores:
    x = score / 3
    if score % 3 == 0:
      if x >= p:
        sure = sure + 1
      elif score > 0 and x + 1 >= p:
        maybe = maybe + 1
    elif score % 3 == 1:
      if x + 1 >= p:
        sure = sure + 1
      elif score > 0 and x + 1 >= p:
        maybe = maybe + 1
    else:
      if x + 1 >= p:
        sure = sure + 1
      elif score > 0 and x + 2 >= p:
        maybe = maybe + 1
  return sure + min(maybe, s)

import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
  line = sys.stdin.readline()
  values = line.split(" ")
  n = int(values[0])
  s = int(values[1])
  p = int(values[2])
  scores = [ int(k) for k in values[3:]]
  print "Case #%d: %d" % (i, calculate(n, s, p, scores))

