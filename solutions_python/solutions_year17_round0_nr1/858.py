def flipper_brute(pstring, flipsize):
  plist = list(pstring)
  neg_run = 0
  flips = 0
  for i in xrange(len(pstring)):
    #print "position %d" % i
    if plist[i]=='-':
      #print "neg found"
      neg_run += 1
    elif neg_run > 0:
      #print "pos found"
      if i > len(pstring) - flipsize:
        return "IMPOSSIBLE"
      flips += 1
      for j in xrange(i+1, i+flipsize):
        if plist[j]=='-':
          plist[j]='+'
        else:
          plist[j] ='-'
      neg_run += 1
    if neg_run == flipsize:
      #print "flip back"
      flips += 1
      neg_run = 0
  if neg_run>0:
    return "IMPOSSIBLE"
  return str(flips)

ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  fields = raw_input().strip().split(' ')
  print "Case #%d: %s" % (i, flipper_brute(fields[0], int(fields[1])))
