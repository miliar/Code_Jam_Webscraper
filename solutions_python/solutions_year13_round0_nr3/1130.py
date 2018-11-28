#!/usr/bin/env python2

from math import sqrt, ceil, floor

#def is_square(number):
#  sqrt_number = sqrt(number)
#  return sqrt_number == int(sqrt_number)

def range(start, stop):
   i = start
   while i < stop:
       yield i
       i += 1

palindromes = {}
def is_palindrome(number):
  number = str(number)

  if number in palindromes:
    return True

  n = len(number)
  m = n - 1
  for i in range(0, n):
    if number[i:i+1] != number[m-i]:
      return False

  palindromes[number] = 1
  return True

#def is_fair_square(number):
##  if not is_square(number):
##    return False
#  return is_palindrome(number) and is_palindrome(sqrt(number))

def test_range(start, end):
  count = 0
  x_start = int(ceil(sqrt(start)))
  x_end = int(floor(sqrt(end)))
  for number in range(x_start, x_end+1):
    if is_palindrome(number) and is_palindrome(number**2):
      count += 1
  return count

def read_entry(input_file):
  r0, r1 = [int(i) for i in input_file.readline().strip().split()]
  return (r0, r1)

def process_entry(entry):
  return test_range(*entry)

def decode_input(input_file):
  results = []

  entries = int(input_file.readline().strip())

  for i in xrange(entries):
    entry = read_entry(input_file)
    results.append(process_entry(entry))

  i = 1
  for r in results:
    print('Case #%d: %s' % (i, r))
    i += 1



if __name__ == '__main__':
  import sys
  
  if len(sys.argv) > 1:
    decode_input(open(sys.argv[1]))
