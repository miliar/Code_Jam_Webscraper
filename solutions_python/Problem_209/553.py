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
  total = int(init[0])
  num = int(init[1])
  datas = []
  for i, line in enumerate(lines[1:]):
    data = line.split(' ')
    r = int(data[0])
    h = int(data[1])
    datas.append({'i': i, 'r': r, 'h': h, 'sqr': r*(r+2*h), 'sph': 2*r*h})
  if num == 1:
    return float(max([ data['sqr'] for data in datas]))*math.pi      
  sqr_top = sorted(datas, key=lambda k: k['sqr'], reverse=True)[:]
  # logging.debug('sorted base')
  # logging.debug(sqr_top)
  sph_top = sorted(datas, key=lambda k: k['sph'], reverse=True)[:]
  # logging.debug('sorted sides')
  # logging.debug(sph_top)
  accepted = False
  result = 0
  sqr_i = 0
  sph_i = 0
  while sqr_i < total:
    count = 1
    no_another = True
    base = sqr_top[sqr_i]
    new_result = base['sqr']
    # logging.debug('base now')
    # logging.debug(base)
    for j in sph_top:
      if j['i'] != base['i']:
        if j['r']>base['r']:
          no_another = False
        else:
          # logging.debug('choose j')
          # logging.debug(j)
          count += 1
          new_result = new_result + j['sph']
          # logging.debug('new_result')
          # logging.debug(new_result)
      if count == num:    
        result = max(result, new_result)
        # logging.debug('update result')
        # logging.debug(result)
        break
    sqr_i += 1
    # accepted = no_another and (count == num)

  return float(result)*math.pi

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
    case_lines = int(lines[start_test].split(' ')[0]) + 1
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


