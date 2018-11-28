from __future__ import division
import os

def getInputData(filename):
  f = open(os.path.normpath(filename), "r")
  lines = f.readlines()
  f.close()

  cases = []
  for n in range(1, len(lines), 2):
    P, K, L = tuple(map(int, lines[n].replace("\n","").split(" ")))
    frik = map(int, lines[n+1].replace("\n","").split(" "))
    
    cases.append({"P":P,"K":K, "L":L, "frik":frik})
    
  return cases


def solve(case):
  result = ""
  P = case["P"]
  K = case["K"]
  L = case["L"]
  frik = case["frik"]

  keys = [0] * K
  for i in range(0, len(keys)):
    keys[i] = []

  #print keys
  
  presses = 0
  
  keyi = 0
  while max(frik) != -1:
    if keyi == K:
      keyi = 0

    mostuses = max(frik)
    mostusesletter = frik.index(mostuses)
    
    keys[keyi].append(mostusesletter)
    lettrNumonKey = keys[keyi].index(mostusesletter) + 1

    presses += frik[mostusesletter] * lettrNumonKey
    
    frik[mostusesletter] = -1
    
    keyi += 1
    
  #print keys
  #print presses

  
  return presses


cases = getInputData("C:\\Other\\GJC\\A-large.in")
#cases = getInputData("C:\\Other\\GJC\\test.in")
#print cases

i = 1
f = open ("C:\\Other\\GJC\\A-large.out","w")
#f = open ("C:\\Other\\GJC\\test.out","w")
for case in cases:
  #print "---"
  answer = str(solve(case))
  #print answer
  if i != len(cases):
    answer += "\n"
    
  f.write("Case #%d: %s" % (i, answer))
  i += 1
f.close()
