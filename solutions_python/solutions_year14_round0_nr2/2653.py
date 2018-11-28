#!usr/bin/python -tt

import sys

def solve(cookies,farm,x_target):
  freq = 2
  p_base_time = cookies/freq
  p_extra_time = (x_target-cookies)/freq
  p_end_time = p_base_time + p_extra_time
  c_end_time = 0.0
  while 1:
    freq += farm
    c_base_time = p_base_time + cookies/freq
    c_extra_time = (x_target-cookies)/freq
    c_end_time = c_base_time + c_extra_time
    if c_end_time > p_end_time:
      return ("%.8f" % p_end_time)
    p_base_time = c_base_time
    p_extra_time = c_extra_time
    p_end_time = c_end_time


def main():
  numcases = int(sys.stdin.readline())
  for casenum in range(1,numcases+1):
    line = sys.stdin.readline().split()
    cookies = float(line[0])
    farm = float(line[1])
    x_target = float(line[2])
    #print ("%.8f" % x_target)  # print precision
    print 'Case #' + repr(casenum) + ': ' + solve(cookies, farm, x_target)

if __name__=='__main__':
  main()
