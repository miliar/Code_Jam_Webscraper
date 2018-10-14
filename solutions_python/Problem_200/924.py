from itertools import *

filename = 'B-large'

def last_tidy_num(line) :
  largest_digit = 0
  largest_pos = 0
  pos = 1
  for c in line :
    digit = int(c)
    if digit > largest_digit :
      largest_digit = digit
      largest_pos = pos
    elif digit < largest_digit :
      front = str(int(line[:largest_pos]) - 1)
      back = repeat('9', len(line) - largest_pos)
      digits = dropwhile(lambda c: c == '0', chain(front, back))
      return ''.join(digits)
    pos += 1
  return line


def find_answer(line) :
  return last_tidy_num(str(int(line)))

with open(filename + '.out.txt', 'w') as output_file :
  with open(filename + '.in.txt', 'r') as input_file :
    n = int(input_file.readline())
    for case_number in range(1,n+1) :
      answer = find_answer(input_file.readline())
      output_file.write('Case #' + str(case_number) + ': ' + answer + '\n')
