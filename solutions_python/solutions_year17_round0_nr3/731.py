f = open('C-large.in', 'r')
t = int (f.readline())

for c in xrange(1, t + 1):
  count = 0
  odds = 0
  values = f.readline().strip().split(" ")
  stalls = int(values[0])
  mems = int(values[1])
  if (stalls == mems):
    print "Case #{}: 0 0".format(c)
  else:
    count = 1
    prev = count
    while True:
    #while (count-1) < mems:
      prev = count
      count<<=1
      if (count-1) >= mems:
        break
      if ((stalls%2) == 1): odds+=prev
      #stalls-=1
      stalls>>=1


    if (stalls%2) == 0:
      stalls>>=1
      if ((prev + odds) >= mems):
        print "Case #{}: {} {}".format(c, stalls, stalls-1)
      else:
        print "Case #{}: {} {}".format(c, stalls-1, stalls-1)
    else:
      stalls>>=1
      if ((prev + odds) >= mems):
        print "Case #{}: {} {}".format(c, stalls, stalls)
      else:
        print "Case #{}: {} {}".format(c, stalls, stalls-1)

