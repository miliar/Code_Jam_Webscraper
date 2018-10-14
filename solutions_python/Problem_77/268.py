#!/usr/bin/python -tt
import sys


def goro():
  filename = sys.argv[1]
  input_file = open(filename, 'r')
  # get the number of cases
  num_of_cases = int(input_file.readline())
  for i in range(1, num_of_cases + 1):
    input_file.readline()
    sortval = []
    value = [int(x) for x in list(input_file.readline().strip().split())]
    sortval.extend(value)
    sortval.sort()
    
    sortc = 0
    for x in sortval:
      k = sortval.index(x)
      if value[k] == x:
        sortc = sortc + 1
       
          
    print "Case #" + str(i) + ":", len(value) - sortc
       

if __name__ == '__main__':
  goro()