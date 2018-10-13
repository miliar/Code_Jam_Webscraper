#!/usr/bin/env python
import operator

def ProcessTestCase(test_case):
  raw_input()
  numbers = [int(x) for x in raw_input().strip().split()]

  possible = reduce(operator.xor, numbers) == 0
  sean_candy = sum(numbers) - min(numbers)

  if possible:
    print "Case #%d: %d"%(test_case+1, sean_candy)
  else:
    print "Case #%d: NO"%(test_case+1)
  return


def Main():
  test_cases = int(raw_input())
  for t in range(test_cases):
    ProcessTestCase(t)

if __name__ == '__main__':
  Main()

