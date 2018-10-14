#!/usr/bin/python
entries = int(raw_input())

for c in xrange(1, entries + 1):
  entry = raw_input().split()
  r = int(entry[0])
  t = int(entry[1])
  # r = radius of initial white circle
  # t = milliltires of black paint, 1 millilitre = pi cm^2 paint

  s = 0 # rings painted
  p = 0 # paint needed

  while True:
    #p = p + ((r + s * 2 + 1) ^ 2 - (r + s * 2) ^ 2)
    p = p + 2 * r + 4 * s + 1
    if p <= t:
      s = s + 1
    else:
      break


  print("Case #" + str(c) + ": " + str(s))
