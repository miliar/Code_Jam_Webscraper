#!/usr/bin/python

import sys


def process(input, output):
  nb = int(input.readline().rstrip())
  
  for val in range(1, nb+1):
    
    print("Case ",val)
    
    # reading data
    inputs = input.readline().rstrip().split()
    nb_of_googlers = int(inputs[0])
    nb_of_surprising = int(inputs[1])
    threshold = int(inputs[2])
    
    answer = 0
    
    for sum in map(int,inputs[3::]):
      if sum >= threshold * 3 - 2:
        answer += 1
      elif sum >= max(threshold * 3 - 4, 1) and nb_of_surprising > 0:
        answer += 1
        nb_of_surprising -= 1
    

    output.write('Case #%d: %s\n' % (val,answer))
    

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
