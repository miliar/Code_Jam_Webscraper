import numpy as np
import sys

#dat=open("small.in").readlines()
dat=open("A-small-attempt1.in").readlines()
ntests=int(dat[0])
i=1
for j in xrange(ntests):
  ans0=int(dat[i].strip('\n'))
  i=i+1
  grid0=np.array([[int(y) for y in x.strip('\n').split(' ')] for x in dat[i:i+4]])
  i=i+4
  ans1=int(dat[i].strip('\n'))
  i=i+1
  grid1=np.array([[int(y) for y in x.strip('\n').split(' ')] for x in dat[i:i+4]])
  i=i+4
  #Possibilites after first
  first_row=grid0[ans0-1,]
  #Possibilities after second
  second_row=grid1[ans1-1,]
  #Which leaves...
  both=np.intersect1d(first_row,second_row)
  #print first_row,second_row,both
  if len(both)==1:
    print "Case #%d: %d"%(j+1,both[0])
  elif len(both)==0:
    print "Case #%d: Volunteer cheated!"%(j+1)
  else:
    print "Case #%d: Bad magician!"%(j+1)

  


 

