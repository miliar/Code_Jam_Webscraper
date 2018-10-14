#!/usr/bin/python

ri = raw_input
for t in xrange(int(ri())):
  test = ri().split()
  n = int(test[0])
  time = [0,0]
  locs = [1,1]
  for r,p in zip(test[1::2],test[2::2]):
    r = 'OB'.index(r)
    p = int(p)
    time[r] = max(time[r]+abs(locs[r]-p),time[1-r]) + 1
    locs[r] = p
  print "Case #%d: %d" % (t+1,max(time))
    
    


