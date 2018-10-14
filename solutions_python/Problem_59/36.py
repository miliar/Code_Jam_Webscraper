#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()
    ext_path = int(inputs[0])
    new_path = int(inputs[1])

    answer = 0

    fs = dict()

    for x in range(ext_path):
      tmp_fs = fs
      for p in input.readline().rstrip().split('/')[1:]:
        if p not in tmp_fs:
          tmp_fs[p] = dict()
        tmp_fs = tmp_fs[p]

    for x in range(new_path):
      tmp_fs = fs
      for p in input.readline().rstrip().split('/')[1:]:
        if p not in tmp_fs:
          answer += 1
          tmp_fs[p] = dict()
        tmp_fs = tmp_fs[p]

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
