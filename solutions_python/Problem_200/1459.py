import math  
def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  append_9 = 0
  while (1):
    li = [int(d) for d in str(n)]
    if is_sorted(li):
      for k in range (0,append_9):
        n *= 10
        n += 9
      print "Case #{}: {}".format(i, n)
      break;
    else:
      # print ">> {}".format(n)
      if li[len(li)-1] == 9:
        # print "n / 10 = {}".format(n / 10)
        n = n / 10
        append_9 += 1
      else :
        n -= 1
      # print "> {}".format(n)