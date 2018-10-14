import fileinput
import logging
import random
import itertools
import re
import math


logging.basicConfig(level=logging.DEBUG)


def find_answer(lines):
  ''' Find the answer for this question '''
  init = lines[0].split(' ')
  total = float(init[0])
  datas = [ line.split(' ') for line in lines[1:]]
  nums = [ (total - float(data[0]))/float(data[1]) for data in datas]
  result = total/max(nums)
  return result

case_lines = 1
def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  i = 1
  while start_test < len(lines) :
    case_lines = int(lines[start_test].split(' ')[1]) + 1
    n_lines = case_lines if case_lines >0 else (int(lines[start_test]) + 1)
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    # test(tc, n)
    print 'Case #{}: {}'.format(i, n)
    i += 1
    start_test += n_lines

if __name__ == '__main__':
  main()


