#!/usr/bin/python -tt

import sys

'''def doWork(n, k):
  print "n is: ", n, "\nk is: ", k
  powered = 0
  sappers = []
  # build list
  for i in range(n): 
    sappers.append(False)
  
  # update the list
  for i in range(k): 
    print i
    for j in range(n):
      #if current node is powered
      if j <= powered or j == 0: 
        sappers[j] = not sappers[j]
        print sappers
      else: 
        break;
    #update powered 
    for j in range(n): 
      powered = 0;
      if sappers[j] == False or j == n-1:
        powered = j
        break;
    print "powered: ", powered
  # end update list
  if powered == n-1 and sappers[n-1] == True: 
    print 'win'
    return 1
  else: 
    print 'lose'
    return 0
  return'''
  
def doWork(n, k): 
  # k is how many times to increment
  # n is how big the number is before it overflows.
  # return true if the number is maxPossibleNumber ie 2^n-1
  k = k % 2**n
  if k == 2**n-1: 
    return 1
  else:
    return 0
  return

def main():
  f = open("input", 'rU')
  lines = f.readline()
  #print int(lines)
  #doWork(4, 47)
  #return
  
  output = open('output', 'w')
  for i in range(int(lines)):
    line = f.readline().split(" ")
    if doWork(int(line[0]), int(line[1])) == 1:
      output.write('Case #'+str(i+1)+': '+"ON\n")
    else: 
      output.write('Case #'+str(i+1)+': '+"OFF\n")
    #break
  f.close()
  
if __name__ == '__main__':
  main()
