#!/usr/bin/env python3

import sys


def process(input, output):
  nb = int(input.readline().rstrip())
  
  for val in range(1, nb+1):
    
    print("Case ",val)
    
    # reading data
    inputs = input.readline().rstrip().split()
    
    length = len(inputs[0])
    minimum = int(inputs[0])
    maximum = int(inputs[1])
    
    answer = solve(length, minimum, maximum)

    output.write('Case #%d: %s\n' % (val,answer))



def solve(length, minimum, maximum):
  """ nb of pairs between min and max """
  if length == 1:
    return 0
  
  pairs = set()
    
  result = 0
  for i in range(minimum,maximum + 1):
    #print ("i : ",i)
    j = i
    for k in range(length - 1):
      j = shift(j,length)
      if j >= minimum and j <= maximum and j != i:
        pairs.add((i,j))
        result += 1
        #break
        #print(i,j)
  
  print(pairs)
  return int(len(pairs)/2)
  
  

def shift(n,length):
  """ shift n one to the right"""
  last_digit = n % 10
  return (last_digit * 10**(length - 1)) + n // 10

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Need file as argument")
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
