#!/usr/bin/python

import sys
#from fractions import gcd

#def lcm(a, b):
#  return a*b/gcd(a,b)

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    musCnt = int(inputs[0])
    low = int(inputs[1])
    high = int(inputs[2])

    notes = []
    inputs = input.readline().rstrip().split()

    answer = 'NO'

    for x in range(0, musCnt):
      notes.append(int(inputs[x]))

    for x in range(low, high+1):
      count = 0
      for y in range(0, musCnt):
        if x % notes[y] == 0 or notes[y] % x == 0:
          count += 1
          continue
        break
      if count == musCnt:
        answer = x
        break

    output.write('Case #%d: %s\n' % (val,answer))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Need file as argument"
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
