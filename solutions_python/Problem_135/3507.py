#!/usr/bin/env python
infile = "A-small-attempt0.in"

ROWS_PER_TEST = 4

def make_guess(before, after):
  before_row = before['rows'][before['answer']-1]
  after_row = after['rows'][after['answer']-1]
  intersect = list(set(before_row) & set(after_row))

  if len(intersect) == 0:
    return 'Volunteer cheated!'
  elif len(intersect) > 1:
    return 'Bad magician!'
  else:
    return '%s' % (intersect[0])


def read_block(file):
  result = {
    'answer': int(file.readline()),
    'rows': [ ]
  }

  for r in xrange(ROWS_PER_TEST):
    row = f.readline().split()
    result['rows'].append([int(v) for v in row])

  return result


if __name__ == "__main__":
  f = open(infile, "r")
  num_cases = int(f.readline())

  for n in xrange(1, num_cases+1):
    before = read_block(f)
    after = read_block(f)
    print "Case #%s: %s" % (n, make_guess(before, after))
