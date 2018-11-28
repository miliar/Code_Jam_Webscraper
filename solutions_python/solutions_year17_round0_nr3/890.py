import math

 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  # read a list of integers, 2 in this case
  n, k = [int(s) for s in raw_input().split(" ")]

  m = int(math.log(k, 2))
  remained = n - (2 ** m) + 1
  base_value = remained / (2 ** m)
  r = remained % (2 ** m)

  rd = k - (2 ** m) + 1
  if rd <= r:
    base_value += 1

  if base_value % 2 != 0:
    max_s = base_value / 2
    min_s = base_value / 2
  else:
    max_s = base_value / 2
    min_s = base_value / 2 - 1

  print "Case #{}: {} {}".format(i, max_s, min_s)
  # check out .format's specification for more formatting options
