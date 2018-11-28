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
input = '/home/oleg/prog/python/jam/inputs/A-large.in';
output = '/home/oleg/prog/python/jam/jam-A-large.result.0';


def solve(dict, queries):
  nos = 0;
  while True:
    eng = '';
    maxIndex = 0;
    try:
      for k in dict.keys():
        #print "looking for " + str(k);
        z = queries.index(k);
        #print "found " + str(z);
        if (z > maxIndex):
          maxIndex = z;
          eng = k;
      #we need a switch
      #print "engine: " + str(eng);
      nos += 1;
      #remove processed queries
      queries = queries[maxIndex:];
      #print "switch:" + str(maxIndex);
      #print queries;
      
    except ValueError:
      return nos;     
    


def printOut(result):
  out = open(output,'a');
  c = 1;
  for i in result:
    case = 'Case #' + str(c) + ': ' + str(i) + '\n';
    out.write(case);
    #print case;
    c += 1;
    
  out.close();
  
f = open(input, 'r');

numberOfCases = n = int(f.readline());

result = zeros(n);


#for each case
for i in range(n):
  nen = int(f.readline()); 
  engines = dict();
  queries = list();
  #read engine names
  for j in range(nen):
    l = f.readline().rstrip('\n ');
    engines[l] = False;
    
  noq = int(f.readline());   
  for j in range(noq):
    l = f.readline().rstrip('\n ');
    queries.append(l);
  
  
  #print "Engines"  
  #print engines;
  #print "Queries"  
  #print queries;
  result[i] = solve(engines, queries);  
 
  
printOut(result);  
f.close();  
  
    
    
    
    
    
    
    
    
    










