#!/usr/bin/env python2.7

from __future__ import print_function

import sys

TEMPLATE = 'Case #{0}: {1}'

def friends_to_invite(case_data):
  data = case_data.split()
  max_shyness = int(data[0])
  audience = [int(x) for x in data[1]]
  assert max_shyness == len(audience)-1
  standing = 0
  friends = 0
  for s, n in enumerate(audience):
    if s > standing + friends:
      friends += 1
    standing += n
  return friends

def tests():
  cases = {1: 'Case #1: 0',
           2: 'Case #2: 1',
           3: 'Case #3: 2',
           4: 'Case #4: 0'}
  data = ('4\n'
          '4 11111\n'
          '1 09\n'
          '5 110011\n'
          '0 1\n')
  as_gen = (l for l in data.splitlines())
  number_of_cases = int(as_gen.next())
  assert number_of_cases == 4
  for case_n, case_data in enumerate(as_gen, 1):
    rv = TEMPLATE.format(case_n, friends_to_invite(case_data))
    assert cases[case_n] == rv
  assert number_of_cases == case_n


def main(path_to_file):
  try:
    with open(path_to_file) as fd:
      data = (line for line in fd.readlines())
  except IOError as io_error:
    print(io_error, file=sys.stderr)
    sys.exit(1)

  _number_of_cases = int(data.next())
  for case_n, case_data in enumerate(data, 1):
    print(TEMPLATE.format(case_n, friends_to_invite(case_data)))


if __name__ == '__main__':
  tests()
  main(' '.join(sys.argv[1:]))
