#!/usr/bin/env python3

import sys

def translate(c):
  if c == 'a':
    return 'y'
  elif c == 'b':
    return 'h'
  elif c == 'c':
    return 'e'
  elif c == 'd':
    return 's'
  elif c == 'e':
    return 'o'
  elif c == 'f':
    return 'c'
  elif c == 'g':
    return 'v'
  elif c == 'h':
    return 'x'
  elif c == 'i':
    return 'd'
  elif c == 'j':
    return 'u'
  elif c == 'k':
    return 'i'
  elif c == 'l':
    return 'g'
  elif c == 'm':
    return 'l'
  elif c == 'n':
    return 'b'
  elif c == 'o':
    return 'k'
  elif c == 'p':
    return 'r'
  elif c == 'q':
    return 'z'
  elif c == 'r':
    return 't'
  elif c == 's':
    return 'n'
  elif c == 't':
    return 'w'
  elif c == 'u':
    return 'j'
  elif c == 'v':
    return 'p'
  elif c == 'w':
    return 'f'
  elif c == 'x':
    return 'm'
  elif c == 'y':
    return 'a'
  elif c == 'z':
    return 'q'
  else:
    if (c != ' '):
      print("unknown letter!")
    return c

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip()

    answer = ""
    for c in inputs:
      answer += translate(c)

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
