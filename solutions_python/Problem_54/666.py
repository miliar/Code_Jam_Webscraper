#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Dmytro Molkov on 2010-05-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import math

def gen_new_primes(primes):
  """docstring for gen_new_primes"""
  found = False
  number = primes[len(primes) - 1]
  run = 0
  inc = 100000
  old_len = len(primes)
  while len(primes) - old_len < 10000:
    print len(primes) - old_len, " ", old_len
    newvals = range(number + 2 + run * inc, number + (run + 1) * inc, 2)
    for prime in primes:
      num = prime * 2
      index = 0
      while num < newvals[len(newvals) - 1]:
        while index < len(newvals) and newvals[index] < num:
          index += 1
        if newvals[index] == num:
          del newvals[index]
        num += prime
    index = 0
    print "first"
    while index  < len(newvals):
      num = newvals[index] * 2
      second_index = index + 1
      if index % 10000 < 10:
        print index
      while num < newvals[len(newvals) - 1]:
        while second_index < len(newvals) and newvals[second_index] < num:
          second_index += 1
        if newvals[second_index] == num:
          del newvals[second_index]
        num += newvals[index]
      index += 1

  
    primes.extend(newvals)
    run += 1
  # while not found:
  #   number += 2
  #   found = True
  #   for prime in primes:
  #     if number % prime == 0:
  #       found = False
  #       break
  #     if prime * prime > number:
  #       break
  #     if tests > 10000:
  #       print "break"
  #       break
  #     tests += 1
  #   if found:
  #     primes.append(number)


def main():
  data = open("/tmp/data")
  out = open("/tmp/out.data", "w")
  tests = int(data.readline())
  result = 0
  primes = [2,3,5]
  for i in range(1, tests + 1):
    splits = data.readline().split(" ")
    numbers_count = int(splits[0])
    numbers = []
    for j in range(1, numbers_count + 1):
      number = int(splits[j])
      if not number in numbers:
        numbers.append(int(splits[j]))
    numbers.sort()
    divisor = 1
    result = 0
    j = 1
    prime_index = -1
    while j < numbers[len(numbers) - 1]:
      # prime_index += 1
      # if (len(primes) == prime_index):
      #   gen_new_primes(primes)
      j += 1
      for prime in primes:
        if j % prime == 0 and j <> prime:
          continue
      in_solution = True
      while in_solution:
        rest = numbers[0] % (j)
        for number in numbers:
          if rest <> number % (j):
            in_solution = False
            break
        # print i, " ", result, " ", divisor, " ", j, numbers[len(numbers) - 1]
        if in_solution:
          if (numbers[0] % j <> 0):
            result += divisor * (j - (numbers[0] % j))
          for k in range(0, len(numbers)):
            numbers[k] = int(math.ceil( float(numbers[k]) / j))
          divisor = divisor * j


    if ((result + int(splits[1])) % divisor <> 0):
      result = divisor - result
    out.write("Case #" + str(i) + ": " +str(result) + "\n")
    print "Case #" + str(i) + ": " +str(result) + "\n"
    


if __name__ == '__main__':
  main()

