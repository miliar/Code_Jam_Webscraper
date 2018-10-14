#!/usr/bin/env python2.3
#
#  welcometocodejam.py
#  
#
#  Created by Steven Holte on 9/3/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

str = "welcome to code jam"

D = {}
for i,c in enumerate(str):
  if c not in D:
    D[c]=[]
  D[c].append(i)

import sys

N = int(sys.stdin.readline())

for case in range(N):
  line = sys.stdin.readline()
  count = [0 for c in str]
  for c in line:
    for i in D.get(c,[]):
      if i==0:
        count[i]+=1
      else:
        count[i]+=count[i-1]
  print "Case #%d: %#04d"%(case+1,count[-1]%10000)

