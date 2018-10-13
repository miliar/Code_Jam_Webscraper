#! /usr/bin/env python



##
#   Google Code Jam.
#   17.07.2008
#   Oleg Shelajev.
#   shelajev@gmail.com
##
import math
import array
from numarray import *;


#change these according to where the input is and where to do output
input = '/home/oleg/prog/python/jam/inputs/B-large.in';
output = '/home/oleg/prog/python/jam/jam-B-large.result';


def solve(tt, a, b):
  #print "tt = " + str(tt);
  #print "A: ";
  #print a; 
  #print "B: ";
  #print b; 
  astart = 0;
  bstart = 0;
  #current
  atA = 0;
  atB = 0;
  #trains in travel
  c = list();
  for m in range(24*60):
    #check if somebody is ready again:
    for tr in c:
      if(m == tr[0]):
        if(tr[1] == 'a'):
          #print "train ready @ A " + str(m) + "(" + str(atA) + ")";
          atA += 1; 
        else:
          #print "train ready @ B " + str(m)+ "(" + str(atB) + ")";
          atB += 1;
    #check A:
    for ta in a:
      if(m == ta[0]):
        if (atA > 0):
          atA -= 1; 
          c.append([ta[1]+tt,'b']);
          #print str(m) + ": train left A -> ready @ B at " + str(ta[1]+tt); 
        else:
          astart += 1;
          c.append([ta[1]+tt,'b']);
          #print str(m) + ": train left A -> ready @ B at " + str(ta[1]+tt); 
    #check B:
    for tb in b:
      if(m == tb[0]):
        if (atB > 0):
          atB -= 1; 
          c.append([tb[1]+tt,'a']);
          #print str(m) + ": train left B -> ready @ A at " + str(tb[1]+tt); 
        else:
          bstart += 1;
          c.append([tb[1]+tt,'a']);
          #print str(m) + ": train left B -> ready @ A at " + str(tb[1]+tt); 
  return [astart, bstart];


#convert time to int representation
def convertTime(time):
  s = time.split(":");
  t = int(s[1]) + 60*int(s[0]);
  return t;

#print result
def printOut(result):
  out = open(output,'a');
  c = 1;
  for i in result:
    case = 'Case #' + str(c) + ': ' + str(i[0]) + " " + str(i[1]) + '\n';
    out.write(case);
    c += 1;
    
  out.close();


#main
f = open(input, 'r');

numberOfCases = int(f.readline());

result = zeros([numberOfCases, 2]);
for i in range(numberOfCases):
  tt = int(f.readline());
  l = f.readline().rstrip('\n ').split(' ');
  aTob = int(l[0]);
  bToa = int(l[1]);
  a = list();
  b = list();
  for j in range(aTob):
    line = f.readline().rstrip('\n ').split(' ');
    a.append([convertTime(line[0]), convertTime(line[1])]);
  for j in range(bToa):
    line = f.readline().rstrip('\n ').split(' ');
    b.append([convertTime(line[0]), convertTime(line[1])]);  

  result[i] = solve(tt, a, b);
printOut(result);
  
  
  















