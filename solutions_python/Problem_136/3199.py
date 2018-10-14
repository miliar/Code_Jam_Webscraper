# cd C:/Dropbox/Joe/google_code_jam
from __future__ import division
from sys import path
if 'C:\\svn\\EnergyAnalytics' not in path: path.insert(0, 'C:\\svn\\EnergyAnalytics')
from trunk.config import * # Defines DB_name. Adds trunk package to path list.

filename = '2014_qual_B-large'
filepath = 'C:\\Dropbox\\Joe\\google_code_jam\\{}'.format(filename)
input = open(filepath + '.in').read()
input = input.split('\n')
n_cases = int(input[0])
output = ''

import trunk.lib.UDF as udf
from numpy import fromstring, array, minimum, maximum, floor, nan, add, multiply
from pandas import Panel, DataFrame, Series
from datetime import datetime, timedelta
from math import factorial
prgm_start = datetime.now()

def str_to_Series(str, dtype=float):
  return Series(fromstring(str, dtype=dtype, sep=' '))

def reverse_Series(s):
  return Series(array(s)[::-1], index=s.index)
  
for c in range(n_cases):
  rate = 2
  elapsed_time = 0
  build_cost, rate_boost, goal = tuple(str_to_Series(input[c + 1]))
  
  while True:
    time_to_build = build_cost / rate
    goal_time = goal / rate
    goal_time_w_build = time_to_build + (goal / (rate + rate_boost))
    if goal_time < goal_time_w_build:
      elapsed_time += goal_time
      break
    else:
      elapsed_time += time_to_build
      rate += rate_boost
  #
  
  result = 'Case #{}: {:.7f}'.format(c+1, elapsed_time)
  print datetime.now(), '   ', result
  output = output + result + '\n'
#
x = (datetime.now() - prgm_start).total_seconds()
print 'Code run time = {:02.0f}:{:02.0f}:{:06.3f}'.format(floor(x/3600), floor((x%3600)/60), x%60)
with open('{}.txt'.format(filename), 'w') as text_file: text_file.write(output[:-1]) # strip last blank line