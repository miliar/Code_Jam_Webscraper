import sys
import itertools

CASE_NUM, CASE_IND, INLINES = 1, 1, []

def list_from_line(line, delim):
  return line.split(delim)

def line_from_list(lst, delim):
  return delim.join(lst)

def get_line():
  global CASE_IND, INLINES
  line = INLINES[CASE_IND]
  CASE_IND += 1
  return line

def get_lines(num_lines):
  global CASE_IND, INLINES
  lines = INLINES[CASE_IND:CASE_IND + num_lines]
  CASE_IND += num_lines
  return lines

def group_every_n(seq, n):
  args = [iter(seq)] * n
  return itertools.zip_longest(*args, fillvalue=None)

def get_case():
  l, x = [int(i) for i in list_from_line(get_line(), ' ')]
  string = get_line()
  return [l, x, string]

def solve(case):
  """
  From left, keep multiplying next char until equals i.
  - if run out of chars, NO
  From left, keep multiplying next char until equals j.
  - if run out of chars, NO
  Multiply remainder of string til no more chars.
  - if product is j, YES
  - else, NO
  """
  mult_struct = {
    'i': {'i': -1, 'j': 'k', 'k': '-j'},
    'j': {'i': '-k', 'j': -1, 'k': 'i'},
    'k': {'i': 'j', 'j': '-i', 'k': -1},
    '-i': {'i': 1, 'j': '-k', 'k': 'j'},
    '-j': {'i': 'k', 'j': 1, 'k': '-i'},
    '-k': {'i': '-j', 'j': 'i', 'k': 1},
    1: {'i': 'i', 'j': 'j', 'k': 'k'},
    -1: {'i': '-i', 'j': '-j', 'k': '-k'}
  }

  l, x, string = case
  string *= x
  num_chars = len(string)

  first, c = 1, 0

  while first != 'i':
    first = mult_struct[first][string[c]]
    c += 1
    if c == num_chars:
      return 'NO'

  second = 1
  while second != 'j':
    second = mult_struct[second][string[c]]
    c += 1
    if c == num_chars:
      return 'NO'

  third = 1
  while c < num_chars:
    third = mult_struct[third][string[c]]
    c += 1

  if third == 'k':
    return 'YES'

  return 'NO'

def main():
  global CASE_NUM, INLINES
  f = open(sys.argv[1])
  INLINES = f.readlines()
  INLINES = [line.rstrip('\n') for line in INLINES]
  f.close()

  num_test_cases = int(INLINES[0])
  out = []

  while CASE_NUM <= num_test_cases:
    out.append('Case #%d: %s' % (CASE_NUM, solve(get_case())))
    CASE_NUM += 1

  outf = open('out.txt', 'w')
  outf.write('\n'.join(out))
  outf.close()

if __name__ == '__main__':
  main()
