#!/usr/bin/env python2

import math

def check_palin(x):
  string = str(x)
  length = len(string)
  for y in xrange(0,length/2+1):
    if string[y] != string[length-y-1]:
      return False
  return True

def check_square_palin(x):
  sqr = x*x
  return check_palin(sqr)

count = int(raw_input())

for x in xrange(1,count+1):
  num_range = [0,0]
  input_2 = raw_input().split()
  num_range[0] = int(input_2[0])
  num_range[1] = int(input_2[1])
  sqrt_range = [0,0]
  sqrt_range[0] = int(math.floor(math.sqrt(num_range[0])))
  sqrt_range[1] = int(math.ceil(math.sqrt(num_range[1])))
  calc_range = [0,0]
  calc_range[0] = len(str(sqrt_range[0]))
  calc_range[1] = len(str(sqrt_range[1]))

  result_count = 0

  for y in xrange(1,10):
    check_num = y
    if check_num**2 < num_range[0] or check_num**2 > num_range[1]:
      continue
    if check_square_palin( check_num ):
      result_count += 1
    
  for y in xrange(calc_range[0], calc_range[1] + 1):
    for z in xrange(1 * 10**(y/2 - 1), 1 * 10**(y/2)):
      if z < 0:
        continue
      if y % 2 == 1:
        for w in xrange(0, 10):
          check_num = int(''.join([str(z), str(w), str(z)[::-1]]))
          if check_num**2 < num_range[0] or check_num**2 > num_range[1]:
            continue
          if check_square_palin( check_num ):
            result_count += 1
      else:
        check_num = int(''.join([str(z), str(z)[::-1]]))
        if check_num**2 < num_range[0] or check_num**2 > num_range[1]:
          continue
        if check_square_palin( check_num ):
          result_count += 1

  print "Case #" + str(x) + ": " + str(result_count)
