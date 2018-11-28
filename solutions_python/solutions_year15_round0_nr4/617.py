import sys
import itertools

CASE_NUM, CASE_IND, INLINES = 1, 1, []

def list_from_line(line, delim):
  return line.split(delim)

def get_line():
  global CASE_IND, INLINES
  line = INLINES[CASE_IND]
  CASE_IND += 1
  return line

def get_case():
  return [int(n) for n in list_from_line(get_line(), ' ')]

def solve(case):
  x, r, c =  case
  if (r * c) % x != 0:
    return 'RICHARD'
  if (r == 1 or c == 1) and (x >= 3):
    return 'RICHARD'
  if r < x and c < x:
    return 'RICHARD'
  if r * c == 8 and x == 4:
    return 'RICHARD'

  return 'GABRIEL'

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
