#!/usr/bin/python

import pickle
import sys
import os

def p(s):
  print s
  
def solve(C,F,X):
  cookies_per_second=2.0
  cps=cookies_per_second
  # with no factories
  t0=X/cps
  cps0=cps
  # with one factory    
  t1=C/cps0
  cps1=cps+F
  while (t1+X/cps1)<t0:
    #p("cps: %s(+%s). with: %s, without: %s"%(cps0,F,t1,t0))
    t0=t1+X/cps1
    cps0=cps1
    # one more factory    
    t1=t1+C/cps0
    cps1=cps0+F
  return t0
  
if len(sys.argv) < 2:
  quit()

f = open(sys.argv[1],'r')
fout = open("b-out.txt","w")
T = int(f.readline()) #number of test cases
for t in range(T):
    #p("case %s" % (t+1,))
    cfx = map(float,f.readline().split())
    #p(str(cfx))
    best_time=solve(cfx[0],cfx[1],cfx[2])
    fout.write("Case #%s: %s" % (t+1,best_time))
    fout.write("\n")
  
fout.close()