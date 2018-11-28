import sys

tests = input ()
for test in range (tests):
  rest = 0.0
  d, n = map(int, sys.stdin.readline().split())
  for i in range (n):
    k, s = map(int, sys.stdin.readline().split())
    rest = max (rest, (d - k) * 1.0 / s)
  resv = d / rest
  print ("Case #" + str(test + 1) + ": " + str(resv))
