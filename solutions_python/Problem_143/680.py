#! /usr/bin/python2.7

import sys


def main():
  inFileName = sys.argv[1]
  outFileName = sys.argv[2]
   
  with open(sys.argv[1]) as fin:
    T = int(fin.readline())
    
    count = [];
    for case in xrange(1, T + 1):      
      #######################################
      # code goes here
      #line = fin.readline()
      #data = map(lambda x: len(x) * 2, line.split())
      #data = map(int, line.split())
      
      line = fin.readline()
      (A, B, K) = map(int, line.split())
      
      c = 0
      for i in xrange(A):
	for j in xrange(B):
	  if ((i & j) <  K) : c += 1
	  
      count.append(c);
      #######################################
  
  #for line in sys.stdin:
    #print line
    
  with open(sys.argv[2], "w") as fout:
    for case in xrange(1, T + 1):
      
      # add output
      fout.write("Case #" + `case` +": " + `count[case - 1]` + "\n")
  
  
if __name__ == '__main__':
  main()