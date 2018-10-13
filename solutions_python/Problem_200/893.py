ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  num = int(raw_input().strip())
  numstring = list(str(num))
  for j in xrange(len(numstring)-1):
    if int(numstring[-1-j])<int(numstring[-2-j]):
      for k in xrange(j+1):
        numstring[-1-k] = "9"
      numstring[-2-j] = str(int(numstring[-2-j])-1)
  print "Case #%d: %s" % (i, int("".join(numstring)))
