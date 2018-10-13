#!/usr/bin/python -u

import sys,re,bisect

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 0

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

def cost(o,e,p):
  l = o-e
  if(l<0):
    l = -l
  cost1 = -(l)*(l-1)/2
  return p*cost1

def find_first_val_greater_or_equal(arr, val):
  i = bisect.bisect(arr,val)
  if(arr[i-1]==val): return val
  if(i >= len(arr)):
    debug(arr)
    debug(val)
    debug(i)
  return arr[i]

def cheapest(os,es):
  t_cost = 0
  while(True):
    if(not es): break
    os_keys = os.keys()
    os_keys.sort()
    es_keys = es.keys()
    es_keys.sort()
    o = os_keys[-1]
    e = find_first_val_greater_or_equal(es_keys, o)
    p = min(os[o],es[e])
    os[o] = os[o] - p
    es[e] = es[e] - p
    if(not os[o]): del os[o]
    if(not es[e]): del es[e]
    c = cost(o,e,p)
    if(c): debug(str(o)+','+str(e)+','+str(p)+','+str(c))
    t_cost = t_cost + c
  return t_cost

def handleonecase(line1):
  N = long(line1[0])
  M = long(line1[1])
  expected_cost = 0
  cheapest_cost = 0
  os = {}
  es = {}
  for i in range(M):
    oepair = infile.readline().strip().split()
    o = long(oepair[0])
    e = long(oepair[1])
    p = long(oepair[2])
    expected_cost = expected_cost + cost(o,e,p)
    if(o in os): os[o]=os[o]+p
    else: os[o]=p
    if(e in es): es[e]=es[e]+p
    else: es[e]=p
  cheapest_cost = cheapest(os,es)
  debug(expected_cost)
  debug(cheapest_cost)
  return (expected_cost-cheapest_cost)%1000002013

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip().split()
#  line2 = infile.readline().strip().split()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




