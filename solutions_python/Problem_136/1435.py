t = int(raw_input())

for case in xrange(t):
  c = None
  f = None
  x = None
  for num in raw_input().split():
    if c == None:
      c = float(num)
    elif f == None:
      f = float(num)
    else:
      x = float(num)
  seconds = x / 2
  n = 1
  pre = c / 2
  while True:
    total = pre + x/(2 + n*f)
    pre = pre + c/(2 + n*f)
    if total < seconds:
      seconds = total
      n = n + 1
    else:
      break
  print "Case #" + str(case + 1) + ": " + str(seconds)
