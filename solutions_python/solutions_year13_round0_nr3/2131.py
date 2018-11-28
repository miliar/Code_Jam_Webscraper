#!/usr/bin/python

import math

def int_palindrome(a):
  s = str(a)
  return s == s[::-1]

def is_square(a):
  int_sqrt_a = int(math.sqrt(a))
  return a == int_sqrt_a * int_sqrt_a

cache = { 0:0 }
infile = open('C-small-attempt0.in')
outfile = open('fs_out', 'w')
num_case = int(infile.readline())
floor_cache = 0
for case in range(1, num_case + 1):
  a, b = map(int, infile.readline().split())
  int_sqrt_a = int(math.sqrt(a))
  int_sqrt_b = int(math.sqrt(b))
  if int_sqrt_a not in cache:
    for i in range(len(cache.keys())):
      if cache.keys()[i] > int_sqrt_a:
        floor_cache = cache.keys()[i - 1]
        break
    #cache[int_sqrt_a] = cache[floor_cache]
    for i in range(floor_cache + 1, int_sqrt_a + 1):
      cache[i] = cache[i - 1]
      if int_palindrome(i) and int_palindrome(i * i):
        cache[i] = cache[i] + 1
        #cache[int_sqrt_a] = cache[int_sqrt_a] + 1
  if int_sqrt_b not in cache:
    for i in range(len(cache.keys())):
      if cache.keys()[i] > int_sqrt_b:
        floor_cache = cache.keys()[i - 1]
        break
    #cache[int_sqrt_b] = cache[floor_cache]
    for i in range(floor_cache + 1, int_sqrt_b + 1):
      cache[i] = cache[i - 1]
      if int_palindrome(i) and int_palindrome(i * i):
        cache[i] = cache[i] + 1
        #cache[int_sqrt_b] = cache[int_sqrt_b] + 1
  if int_palindrome(a) and is_square(a) and int_palindrome(int_sqrt_a):
    result = cache[int_sqrt_b] - cache[int_sqrt_a] + 1
  else:
    result = cache[int_sqrt_b] - cache[int_sqrt_a]
  outfile.write('Case #' + str(case) + ': ' + str(result) + '\n')
