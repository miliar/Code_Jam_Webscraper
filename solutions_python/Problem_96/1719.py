import sys
sys.stdin = open("data.in", "r")
sys.stdout = open("data.out", "w")
i = 1
t = int(input())
while i <= t:
  line = [int(x) for x in input().split(" ")]
  s = line[1]
  p = line[2]
  numbers = (x for x in line[3:] if x >= p)
  total = 0
  for x in numbers:
    if 3 * p - 2 <= x:
      total += 1
    elif 3 * p - 4 <= x and s > 0:
      total += 1
      s -= 1
  print("Case #%d: %d" % (i, total))
  i += 1
