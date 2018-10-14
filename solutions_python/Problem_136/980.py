for t in xrange(int(raw_input())):
  c, f, x = map(float, raw_input().split())
  rate = 2
  time = 0
  while ((x - c) / rate) > (x / (rate + f)):
    time += c / rate
    rate += f
  time += x / rate
  print "Case #" + str(t + 1) + ": " + str(time)
