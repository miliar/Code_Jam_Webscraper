import numpy as np
from copy import deepcopy as cp
import sys

dat=open(sys.argv[1]).readlines()
ntests=int(dat[0])
i=1
for j in xrange(ntests):
  nblocks=int(dat[i].strip('\n'))
  i=i+1
  alice=[float(x) for x in dat[i].strip('\n').split(' ')]
  alice.sort()
  i=i+1
  bob=[float(x) for x in dat[i].strip('\n').split(' ')]
  bob.sort()
  #Sort bob the other way for convenience
  bob=bob[::-1]
  i=i+1
  #First calculate the easy one
  aa=cp(alice)
  bb=cp(bob)
  awin=0
  for x in xrange(nblocks):
    a=aa.pop()
    #Can bob win this one?
    if bb[0]<a:
      #Nope, so delete smallest
      awin=awin+1
      _=bb.pop()
    else:
      #Yep, so delete smallest winner
      tmp=0
      while tmp<nblocks-x and bb[tmp]>a:
        tmp=tmp+1
      _=bb.pop(tmp-1)
  #Now what if she cheats?
  aa=cp(alice)
  bb=cp(bob)
  acheat=0
  for x in xrange(nblocks):
    #Do I have any that will never win?  If so, use them to get rid of 
    #Bob's high ones
    if aa[0]<bb[-1]:
      #This one is destined to loose, so have it loose now and take a high
      #one with it
      _=aa.pop(0)
      _=bb.pop(0)
    else:
      #OK, so we can win with our lowest by forcing bob to play low
      #So let's do that
      _=aa.pop(0)
      _=bb.pop()
      acheat=acheat+1
  print "Case #%d: %d %d"%(j+1,acheat,awin)
