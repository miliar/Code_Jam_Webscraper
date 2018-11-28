#!/usr/bin/python

import sys

def combi(x):
  r = set()
  v = str(x)

  for i in range(len(v) - 1):
    v = v[-1] + v[:-1]
    if (v[0] == '0'):
      continue

    r.add(int(v))

  return r

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    min = int(inputs[0])
    max = int(inputs[1])

    answer = 0

    for x in range(min, max+1):
      c = combi(x)
      for v in c:
        if v >= min and v <= max and v != x:
          answer += 1

    output.write('Case #%d: %s\n' % (val,answer/2))

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
