from math import *
from itertools import *
import os

# general helper functions

def split_to_int(f):
    return [int(v) for v in f.next().split()]

def split_to_float(f):
    return [float(v) for v in f.next().split()]

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


# problem

def main():

    with open("/Users/jackie/Dropbox (Personal)/Documents/Codejam/2014/Qualification/in.in") as f:
        cases = int(f.next())
        for i in range(cases):
            print "Case #%d:" % (i+1),
            line = split_to_float(f)
            C = line[0]
            F = line[1]
            X = line[2]
            min_time = X/2
            curr_rate = 2
            curr_time = 0
            j = 0
            while True:
                curr_time += C/curr_rate
                new_rate = curr_rate + F
                time_if_stop_now = curr_time + X/new_rate
                if time_if_stop_now < min_time:
                    min_time = time_if_stop_now
                if curr_time > min_time:
                    break
                curr_rate = new_rate
                j += 1
            print min_time



main()
