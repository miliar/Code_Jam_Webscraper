#!/usr/bin/python -tt
import sys


def candy():
  filename = sys.argv[1]
  input_file = open(filename, 'r')
  # get the number of cases
  num_of_cases = int(input_file.readline())
  for i in range(1, num_of_cases + 1):
    input_file.readline()
    value = [int(x) for x in list(input_file.readline().strip().split())]
    
    xr = 0
    min = 10000000
    samval = 0
    for x in value:
      xr = xr ^ x
      samval = samval + x
      if min > x: min  = x
      
    if xr != 0:
      print "Case #" + str(i) + ": NO"
    else:
      print "Case #" + str(i) + ":", samval - min
       

if __name__ == '__main__':
  candy()