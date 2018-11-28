#!/usr/bin/python -O

import sys

def getRow(f):
    i = 1
    row_guess = int(f.readline())
    while i < row_guess:
      f.readline()
      i += 1
    row = set(f.readline().split())
    j = 4 - i
    while j > 0:
      f.readline()
      j -= 1
    return row

def main(argv=None):
  if argv is None:
    argv = sys.argv
  f = open(sys.argv[1], 'r')
  n = int(f.readline())
  n_case = 1
  while n_case <= n:
    first_row = getRow(f)
    second_row = getRow(f)
    guess = first_row & second_row
    print "Case #" + str(n_case) + ':',
    if len(guess) == 0:
      print 'Volunteer cheated!'
    elif len(guess) == 1:
      print str(guess.pop())
    else:
      print "Bad magician!"
    n_case += 1
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
