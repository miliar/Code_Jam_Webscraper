from __future__ import with_statement
from math import pow
import sys


with open(sys.argv[1],'r') as f:
  with open('test.out','w') as g:
    f.readline() # number cases
    for case,line in enumerate(f):
      testcase = [int(x) for x in line[:-1].split(" ")]
      ison = (testcase[1]+1)%pow(2,testcase[0])==0
      if ison:
        g.write("Case #%d: ON\n"%(case+1))
      else:
        g.write("Case #%d: OFF\n"%(case+1))



