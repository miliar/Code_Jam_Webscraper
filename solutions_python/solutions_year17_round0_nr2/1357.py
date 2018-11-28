#!/usr/bin/env pypy

import sys,os

num_cases = int(sys.stdin.readline().strip())

def is_tidy(digits):
  cur_digit = digits[0]
  for digit in digits[1:]:
    if digit > cur_digit:
      return False
    elif digit < cur_digit:
      cur_digit = digit
  return True

for case in xrange(0,num_cases):
  ending_number = int(sys.stdin.readline().strip())
  digits = []
  while ending_number > 0:
    digits.append(ending_number % 10)
    ending_number /= 10
  for i in range(0, len(digits)-1):
    if digits[i] == -1:
      digits[i] = 9
      digits[i+1] -= 1
    if is_tidy(digits[i:]):
      break
    elif digits[i] < 9:
      digits[i] = 9
      digits[i+1] -=1
  if digits[-1] == 0:
    digits.pop()
  sys.stdout.write("Case #{}: {}\n".format(case+1, "".join((str(d) for d in digits[::-1]))))
