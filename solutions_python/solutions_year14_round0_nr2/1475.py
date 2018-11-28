import sys

tests = int(sys.stdin.readline())

for i in range(0, tests):
  line = sys.stdin.readline()
  stuff = [float(n) for n in line.split()]
  cookies = 0
  rate = 2
  time = 0
  C = stuff[0]
  F = stuff[1]
  X = stuff[2]
  can_improve = True

  while can_improve:
    toX = (X - cookies) / rate
    toF = (C - cookies) / rate

    can_improve = toX > toF + (X - cookies) / (rate + F)

    if can_improve:
      time += toF
      rate += F
    else:
      time += toX

  print "Case #%d: %.7f" % ((i + 1), time)
