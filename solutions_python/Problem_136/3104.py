import os
import sys

def min_cookie_time(farm_cost, curr_rate, rate_inc, target):
  result = 0.0
  
  while ((target*1.0)/curr_rate) > ((farm_cost*1.0)/curr_rate) + ((target*1.0)/(curr_rate+rate_inc)):
    result += (farm_cost*1.0)/curr_rate
    curr_rate += rate_inc

  return result + ((target*1.0)/curr_rate)

def main(case_no, farm_cost, rate_inc, target):
  print "Case #" + str(case_no) + ":", min_cookie_time(farm_cost, 2.0, rate_inc, target)

if __name__ == "__main__":
  fd = open("B-large.in.txt", "r")
  n_cases = int(fd.readline().strip())
  for i in xrange(1, n_cases+1):
    C, F, T = fd.readline().strip().split(" ")
    main(i, float(C), float(F), float(T))

