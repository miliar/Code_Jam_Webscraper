#!/usr/bin/python
import sys, os, math

def print_usage():
  print "Usage: fair_and_square.py <input file>"
 
def is_palindrome(num):
  num_str = str(num)
  for i in range(len(num_str)/2):
    if num_str[i] != num_str[len(num_str) - 1 - i]:
      return False
  return True

def num_fair_and_square_in_range(start, end):
  start_sqrt = int(math.ceil(math.sqrt(start)))
  end_sqrt   = int(math.floor(math.sqrt(end)))

  count = 0
  i = start_sqrt
  #for i in range(start_sqrt, end_sqrt+1):
  while i < end_sqrt + 1:
    if is_palindrome(i) and is_palindrome(i**2):
      count += 1
    i += 1
  return count


def num_fair_and_square_in_range_2(start, end):
  start_sqrt = int(math.ceil(math.sqrt(start)))
  end_sqrt   = int(math.floor(math.sqrt(end)))

  count = 0
  i = start_sqrt
  #for i in range(start_sqrt, end_sqrt+1):
  #while i < end_sqrt + 1:
  generator = yield_palindromes(start_sqrt,end_sqrt)
  for palindrome in generator:
    if palindrome < start_sqrt or palindrome > end_sqrt:
      continue
    if is_palindrome(palindrome**2):
      #print 'palindrome: ', palindrome**2
      count += 1
    i += 1
  return count

def yield_palindromes(a,b):
  min_digits = len(str(a))
  max_digits = len(str(b))
  #print 'max digits: ', max_digits
  for digits in range(min_digits, max_digits + 1):
    if digits == 1:
      for i in range(1, 10):
        yield i
      continue

    even = digits % 2 == 0
    start_num = int('1'*(digits/2))
    end_num   = int('9'*(digits/2) )
    
    for i in range(start_num, end_num +1):
      num_str = str(i)
      if even:
        num_str = num_str + num_str[::-1]
        num = int(num_str)
        if num < a or num > b:
          continue
        yield num
      else:
        for j in range(1, 10):
          new_num_str = num_str + str(j) + num_str[::-1]
          num = int(new_num_str)
          if num < a or num > b:
            continue

          yield num
   

def read_input_data(input_filename):
  cases = []
  with open(input_filename) as input_file:
    data = input_file.read()
  data_lines = data.split("\n")[1:]
  data_ranges = map(lambda x: map(int ,x.split()), data_lines)
  
  return data_ranges

def main():
  if len(sys.argv) != 2:
    print_usage()
    sys.exit(1)
  
  input_filename = sys.argv[1]
  data_ranges = read_input_data(input_filename)
  #generator = yield_palindromes(data_ranges[0][0], data_ranges[0][1])
  #for palindrome in generator:
  #  print palindrome
  for i, data_range in enumerate(data_ranges):
    if len(data_range) == 0:
      continue
    print "Case #" + str(i+1) + ": " + str(num_fair_and_square_in_range_2(data_range[0], data_range[1]))


if __name__ == "__main__":
  main()
