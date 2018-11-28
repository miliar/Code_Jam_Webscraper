#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    chickens = int(inputs[0])
    must_arrived = int(inputs[1])
    distance = int(inputs[2])
    time = int(inputs[3])

    positions = input.readline().rstrip().split()
    speeds = input.readline().rstrip().split()

    i = 0
    while (i < chickens):
      positions[i] = int(positions[i])
      speeds[i] = int(speeds[i])
      i += 1

    nb_arrived = 0
    answer = 0

    i = chickens - 1
    while (i >= 0 and nb_arrived < must_arrived):
      if (positions[i] + time*speeds[i] >= distance):
        nb_arrived += 1
      else:
        answer += must_arrived-nb_arrived
      i -= 1

    if nb_arrived != must_arrived:
      answer = "IMPOSSIBLE"

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
