# coding: utf-8

import sys

def solve_cookie():
  f = open(sys.argv[1], 'r')
  f_out = open(sys.argv[1] + '_out', 'w')
  T = int(f.readline())

  for i in xrange(T):
    variables = map(float, f.readline()[:-1].split(' '))
    C = variables[0] # cost to buy a cookie farm
    F = variables[1] # extra cookies produced by the cookie farm
    X = variables[2] # target num. of cookies
    INIT = 2
    prev_time = X / 2
    #print prev_time
    n = 2
    prev_calc = C / 2
    current_time = prev_calc + X / (2 + F)
    while prev_time > current_time:
      prev_time = current_time
      #for i in xrange(n):
      #  current_time += C / (2 + i*F)
      prev_calc += C / (2 + (n-1)*F)
      current_time = prev_calc + X / (2 + n*F)
      n += 1
    min_result = str(min(prev_time, current_time))
    
    print min(prev_time, current_time)
    f_out.write('Case #' + str(i + 1) + ": " + min_result + '\n')

if __name__ == "__main__":
  solve_cookie()
