# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

def tidy_nums(chars):
  digit = [int(x) for x in chars]
  first_bad_index = None
  for i in range(1, len(digit)):
    if digit[i] < digit[i-1]:
      first_bad_index =  i
      break
  if first_bad_index is None:
    return chars
  else:
    leading = str(int(''.join(chars[:first_bad_index])) - 1)
    following = ''.join(['9' for x in chars[first_bad_index:]])
    
    return tidy_nums(leading) + following
  

num_cases = int(raw_input())
for case in range(num_cases):
  label = 'case #{}:'.format(case + 1)
  print(label, int(tidy_nums(raw_input())))
