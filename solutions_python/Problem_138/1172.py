#!/usr/bin/python

import pickle
import sys
import os

def p(s):
  print s
  pass
  
def war(naomi,ken):
  N = len(naomi)
  pt_ken=0
  for n in range(N):
    if naomi[n]>ken[len(ken)-1]:
      return N-pt_ken
      p("naomi plays %s, ken plays %s. 1pt naomi" %(naomi[n],ken[0]))
      ken.pop(0)      
    else:
      for k in range(len(ken)):
        if ken[k]>naomi[n]:
          p("naomi plays %s, ken plays %s" %(naomi[n],ken[k]))
          ken.pop(k)        
          pt_ken=pt_ken+1
          break
  return N-pt_ken

def dwar(naomi,ken):
  """ deceitful war"""
  p(str(naomi))
  p(str(ken))
  N = len(naomi)
  pt=0
  for n in range(N):
    if naomi[n]>ken[0]:
      p("naomi plays %s(%s), ken plays %s. 1pt naomi" %(naomi[n],ken[len(ken)-1]+0.001,ken[0]))
      ken.pop(0)
      pt=pt+1
  return pt

  
if len(sys.argv) < 2:
  quit()

f = open(sys.argv[1],'r')
fout = open("b-out.txt","w")
T = int(f.readline()) #number of test cases
for t in range(T):
    p("case %s" % (t+1,))
    N = int(f.readline()) # N blocks
    naomi = map(float,f.readline().split())
    ken  = map(float,f.readline().split())
    naomi.sort()
    ken.sort()
    p(str(len(ken)))
    war_pts=war(list(naomi),list(ken))
    p(str(len(ken)))
    dw_pts=dwar(naomi,ken)
    fout.write("Case #%s: %s %s" % (t+1,dw_pts,war_pts))
    fout.write("\n")
  
