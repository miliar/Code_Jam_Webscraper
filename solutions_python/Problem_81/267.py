#!/usr/bin/python -tt

import sys
import fractions

def getWP(case):
  WP = []
  counter = 0.0
  win = 0.0
  for i in case: 
    counter = 0.0
    win = 0.0
    for j in i: 
      if j == '.':
        continue
      elif j == '1':
        win += 1
      counter += 1
    WP.append((win/counter, counter))
  return WP
  
def getOWP(case, WP):
  OWP = []
  for i in case:
    total = 0.0
    sofar = 0.0
    for index, j in enumerate(i): 
      if j == '.': 
        continue
      elif j == '1':
        sofar += (WP[index][0]*(WP[index][1]))/(WP[index][1]-1)
      else: 
        sofar += (WP[index][0]*WP[index][1]-1)/(WP[index][1]-1)
      total += 1
    OWP.append(sofar/total)
  return OWP

def getOOWP(case, OWP):
  OOWP = []
  for i in case:
    total = 0.0
    sofar = 0.0
    for index, j in enumerate(i): 
      if j == '.':
        continue
      total += 1
      sofar += OWP[index]
    OOWP.append(sofar/total)
  return OOWP

def doWork(case): 
  WP = getWP(case)
  #print WP
  OWP = getOWP(case, WP)
  #print OWP
  OOWP = getOOWP(case, OWP)
  #print OOWP
  RPI = []
  for i in range(len(OWP)):
    RPI.append(0.25*WP[i][0] + 0.5*OWP[i] + 0.25*OOWP[i])
  return RPI
  

def main():
  f = open("input", 'rU')
  lines = f.readline()
  #output = open('output', 'w')
  for i in range(int(lines)):
    #line = f.readline().split(" ")
    #a, b, c = map(int, line)
    case = []
    for j in range(int(f.readline())):
      case.append(list(f.readline())[:-1])
    answer = doWork(case)
    #print input
    #answer = doWork(a, b, c)
    #answer = doWork(int(line[0]), int(line[1]), int(line[2]))
    #print ("Case #%d: %s" % (i+1, answer)
    print ("Case #%d:" % (i+1))
    for k in answer:
      print k
    #output.write("Case #%d: %s\n" % (i+1, answer))
  f.close()
  #output.close()
  
if __name__ == '__main__':
  main()
