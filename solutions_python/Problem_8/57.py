#! /usr/bin/env python



##
#   Google Code Jam.
#   26.07.2008
#   Oleg Shelajev.
#   shelajev@gmail.com
##
import math
import array
from numarray import *;

def isint(x): 
  try: 
    x = int(x);
    return 1;
  except: 
    return 0;

def solve(a, b, p):
  ll = primes(b, p);
  #print "primes " + str(ll);
  length = b - a + 1; 
  data = list(range(a, b + 1));
  #print "data " + str(data);
  for pr in ll:
    toDelete = list();
    for i in range(len(data)):
      row = data[i];
      if isint(row): 
        lll = 1;
        if row% pr == 0:
          #print str(row) + "%" + str(pr) + "== 0";
          toDelete.append(row);
      else:
        lll = len(row); 
        for j in range(lll):
          if row[j]% pr == 0:
            #print str(row[j]) + "%" + str(pr) + "== 0";
            toDelete.append(row);
            break;
    c = list();
    #print "toDelete " + str(toDelete);
    if(len(toDelete) > 1): 
      for i in toDelete:
        data.remove(i);
        if isint(i):
          c.append(i);
        else: 
          for j in i:
            c.append(j);
      #print "c " + str(c);
      data.append(c);      
  #print data;
  return len(data);       
  


  
def primes(n, p):
  if n < 2: return [];
  if n == 2: return [2];
  s = range(3, n, 2);
  mroot = n ** 0.5;
  half = len(s);
  i = 0;
  m = 3;
  while m <= mroot:
    if s[i]:
      j = (m * m - 3)//2;
      s[j] = 0;
      while j < half:
        s[j] = 0;
        j += m;
    i = i + 1;
    m = 2 * i + 3;
  list = [2]+[x for x in s if x];
  for zz in range(len(list)):
    if list[zz] >= p:
      list = list[zz:];
      break;
  return list;
 

#change these according to where the input is and where to do output
input = '/home/oleg/prog/python/jam/inputs/B-small-attempt2.in';
output = '/home/oleg/prog/python/jam/jam-1-B-at2.result';

#print result
def printOut(result):
  out = open(output,'w');
  c = 1;
  for i in result:
    case = 'Case #' + str(c) + ': ' + str(i) +'\n';
    out.write(case);
    print case;
    c += 1;
    
  out.close();



#main
ff = open(input, 'r');

numberOfCases = int(ff.readline());
result = zeros(numberOfCases);
for i in range(numberOfCases):
  l = ff.readline().rstrip('\n ').split(' ');
  a = int(l[0]);
  b = int(l[1]);
  p = int(l[2]);
  result[i] = solve(a, b, p);
  
printOut(result);  
  
  
  

