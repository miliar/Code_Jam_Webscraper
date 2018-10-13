#!/usr/bin/env python

import sys

def compute(f, params):
  [max_shyness, audience] = params

  count = 0
  num_clapping = 0
  cur_needed = 0
  saw_nonzero = False
  for char in audience:
    if num_clapping < cur_needed:
      count += 1
      num_clapping += int(char) + 1
    else:
      saw_nonzero = True
      num_clapping += int(char)
    cur_needed += 1

  return count

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print >>sys.stderr, "*.py infile [outfile]"
    sys.exit(1)

  f = open(sys.argv[1], 'r')
  outname = sys.argv[1].split(".")[0] + ".out" if len(sys.argv) < 3 else sys.argv[2]
  out = open(outname, 'w')
  num_cases = int(f.readline())

  for case_num in range(1, num_cases + 1):
    line = f.readline()
    params = [x for x in line.split()]

    output = "Case #" + str(case_num) + ": " + str(compute(f, params))
    print output
    out.write(output + "\n")

  out.close()
