T = int(raw_input())

for i in xrange(T):
  c, f, x = map(float, raw_input().split(" "))
  rate = 2
  time = 0

  if c >= x:
    time = x / 2

  else:
    time = c / rate
    while ((x - c) / rate > x / (rate + f)):
      rate += f
      time += c / rate

    time += (x - c) / rate

  print "Case #" + str(i + 1) + ":",
  print time