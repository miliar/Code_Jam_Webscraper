# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:50:02 2015

@author: DATHOMSON
"""


def run_solver(fnamein,fnameout):
  fin = file(fnamein)
  finlines = fin.readlines()

  fout = file(fnameout,'w')

  cnt = 1  
  
  for finline in finlines[1:]:
    [smaxstr,sistr] = finline.split()
    smax = int(smaxstr)
    si = [int(c) for c in sistr]
    
    maxfriends = 0
    cumsum = si[0]
    for ii in range(1,smax+1):
      maxfriends = max(maxfriends,ii-cumsum)
      cumsum += si[ii]
  
    print("Case #%d: %d" %(cnt,maxfriends))
    fout.write("Case #%d: %d\n" %(cnt,maxfriends))
    cnt += 1
  
  fin.close()
  fout.close()
  
  