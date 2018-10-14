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
  case = list_from_line(get_line(), ' ')
  s_max = int(case[0])
  ppl_by_shyness = [int(ppl) for ppl in case[1]]
  return [s_max, ppl_by_shyness]

def solve(case):
  """
  Keep track of how many people are needed so far, num_invites (init to 0).
  Keep track of people looked at so far, num_present (init to 0).
  Look at shyness levels from left to right
  - num_invites += index - num_present
  """
  s_max, ppl_by_shyness = case
  num_invites, num_present = 0, ppl_by_shyness[0]
  for shyness in range(1, s_max + 1):
    ppl = ppl_by_shyness[shyness]
    extra_required = shyness - num_present
    if extra_required > 0:
      num_invites += extra_required
      num_present += extra_required
    num_present += ppl

  return str(num_invites)

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
