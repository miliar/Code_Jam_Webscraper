import fileinput
import logging
import random
import itertools
import re
import math


logging.basicConfig(level=logging.DEBUG)


def find_answer(line):
  ''' Find the answer for this question '''
  data = line[0].split(' ')
  s = data[0]
  num = int(data[1])
  
  
  
  s = re.sub(r'^\++','', s)
  s = re.sub(r'\++$','', s) 
  suffix = re.findall(r'\++$', s)
  if len(suffix)>0:
    s = s + '+'*(len(suffix[0])%num)
  
  s = s.replace('+', '0').replace('-', '1')

  result = 0
  while len(s)>= num:
    logging.debug(num)
    logging.debug(s)
    logging.debug('1'*num)
    prefix = int('1'*num) - int(s[0: num])
    logging.debug(prefix)
    if prefix == 0:
      s = s[num:]
      if s:
        s = str(int(s)) 
    else:
      s = str(prefix) + s[num:]
      logging.debug('is not  0') 
      logging.debug(str(prefix)) 
      logging.debug(s)
    result += 1 
  
  if s:
    return 'IMPOSSIBLE'

  return result

case_lines = 1
def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1 

  for i in xrange(0, n_tests):
    n_lines = case_lines if case_lines >0 else (int(lines[start_test]) + 1)
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    # test(tc, n)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()


