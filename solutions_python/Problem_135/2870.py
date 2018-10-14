#! /usr/bin/python2.7

import sys


def main():
  inFileName = sys.argv[1]
  outFileName = sys.argv[2]
   
  with open(sys.argv[1]) as fin:
    T = int(fin.readline())
    
    ans = []
    for case in xrange(1, T + 1):      
      ########################
      # code goes here
      
      
         
      
      guess1 = int(fin.readline())
      for i in xrange(1, 5):
	line = fin.readline()

	if (guess1 == i):
	  line = map(int, line.split())
	  first = set(line)


      guess2 = int(fin.readline())
      for i in xrange(1, 5):
	line = fin.readline()

	if (guess2 == i):
	  line = map(int, line.split())
	  second = set(line)
      
      intersect = first & second
         
      if (len(intersect) == 0):
	ans.append("Volunteer cheated!")
      elif (len(intersect) == 1):
	ans.append(str(intersect.pop()))
      else:
	ans.append("Bad magician!")
      
      ########################
  
  with open(sys.argv[2], "w") as fout:
    for case in xrange(1, T + 1):
      
      # add output
      fout.write("Case #" + `case` +": " + ans[case - 1] + "\n")
  
  
if __name__ == '__main__':
  main()