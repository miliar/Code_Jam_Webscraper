import numpy as np
import sys

dat=open("B-large.in").readlines()
ntests=int(dat[0])
i=1
for j in xrange(ntests):
  c,f,x=(float(x) for x in dat[i].strip('\n').split(' '))
  n=1
  tf_n=x/2
  tp_nmm=1./2.
  tf_npp=(x/(2+f))+c*tp_nmm
  while tf_npp<tf_n:
    tf_n=tf_npp
    tp_nmm=tp_nmm + 1.0/(2+f*n)
    n=n+1
    tf_npp=(x/(2+f*n))+c*tp_nmm
  i=i+1
  print "Case #%d: %.7f"%(j+1,tf_n)
