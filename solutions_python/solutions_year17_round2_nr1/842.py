#!/usr/bin/env python

cases = raw_input()
for ca in range(int(cases)):
    (d,n) = raw_input().strip().split()
    d=int(d)
    hs=[]
    m = None
    for i in range(int(n)):
      (l,s) = raw_input().strip().split()
      t=(d-int(l))/float(s)
      mi = d/t
      if m==None:
        m = mi
      elif mi < m:
        m = mi

    #print d,n
    #print hs
    print "Case #%i: %f" % ( (ca+1), m)
