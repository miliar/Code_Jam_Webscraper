#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    rows = int(inputs[0])
    cols = int(inputs[1])

    figure = []
    impossible = False

    for x in range(0, rows):
      inputs = input.readline().rstrip()
      line = []
      for y in range(0, cols):
        line.append(inputs[y])
      figure.append(line)

    for x in range(0, rows):
      for y in range(0, cols):
        if figure[x][y] != '#':
          continue

        if x == rows -1 or y == cols -1:
          impossible = True
          break

        if figure[x+1][y] == '.' or figure[x][y+1] == '.' or figure[x+1][y+1] == '.':
          impossible = True
          break

        figure[x][y] = '/'
        figure[x+1][y] = '\\'
        figure[x][y+1] = '\\'
        figure[x+1][y+1] = '/'

    output.write('Case #%d:\n' % val)
    if impossible:
      output.write("Impossible\n")
      continue

    for x in range(0, rows):
      for y in range(0, cols):
        output.write('%s' % figure[x][y])
      output.write('\n')

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
