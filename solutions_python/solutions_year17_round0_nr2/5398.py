def isTidy(num):
  exploded_num = [int(i) for i in str(num)]
  pre_exploded = exploded_num[:]
  exploded_num.sort()
  if pre_exploded == exploded_num:
    return True
  return False

t = int(raw_input())  # Read the first input (case count)
for i in xrange(1, t + 1):
  n = int(raw_input())  # Read the case input

  while not isTidy(n):
    n -= 1

  print "Case #{}: {}".format(i, n)
  # check out .format's specification for more formatting options
