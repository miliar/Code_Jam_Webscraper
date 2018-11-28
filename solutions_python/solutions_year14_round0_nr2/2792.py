#! /usr/bin/python2.7

import sys


def main():
  inFileName = sys.argv[1]
  outFileName = sys.argv[2]
   
  with open(sys.argv[1]) as fin:
    T = int(fin.readline())
    
    answer = []
    for case in xrange(1, T + 1):      
      ########################
      # code goes here
      speed = 2
      
      (C, F, X) = map(float, fin.readline().split())
      
      buildFarmTime = 0
      
      while (True):	
	finishTime = buildFarmTime + X / speed
	buildFarmTime += C / speed
	speed += F
	
	newFinishTime = buildFarmTime + X / speed
	
	
	if ( finishTime <= newFinishTime ):
	  timeSpent = finishTime
	  break
      
      answer.append(finishTime)
      
      ########################
    
  with open(sys.argv[2], "w") as fout:
    for case in xrange(1, T + 1):
      
      # add output {:.%}'.format(points/total)
      
      fout.write("Case #" + `case` +": "+ str(answer[case - 1]) + "\n")
  
  
if __name__ == '__main__':
  main()
  