# This is all you need for most Google Code Jam problems.

def tidy(num):
    return not any([num[d] > num[d+1] for d in xrange(len(num) - 1)])


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 2 in this case
  while True:
      num = str(n)
      checks = [num[d] > num[d+1] for d in xrange(len(num) - 1)]
      if any(checks):
          idx = checks.index(True)
          n-=(int(num[idx+1:])+1)
      else:
          print "Case #{}: {}".format(i, n)
          break
