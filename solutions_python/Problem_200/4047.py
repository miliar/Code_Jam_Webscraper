t = int(raw_input())  # read a line with a single integer
# print t
for i in xrange(1, t + 1):
  num = int(raw_input())
  while num > 0:
      b=False
      digits = [int(x) for x in str(num)]
      for yyy in range(len(digits)-1):
          summe = 0
          a = digits[yyy]
          u = digits[yyy+1]
          if u < a:
              counter = 1
              b = True
              for cc in range(len(digits)-yyy-1):
                  summe = digits[-cc-1] * counter + summe
                  counter = counter * 10
              break
      if b is True:
        num = num - summe - 1
      if b is False:
        break
  print "Case #{}: {}".format(i, num)
