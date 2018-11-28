import math
import re
import sys

def main():

  lines = sys.stdin.readlines()

  num_cases = int(lines[0])

  for i in range (1,num_cases+1):
    num_fair_and_square = 0
    case_line = re.split("\D", lines[i])
    #print case_line
    start = int(case_line[0])
    end = int(case_line[1])
    squares_in_range = calculate_squares(start,end)
    #print squares_in_range
    for n in squares_in_range:
      if is_fair_and_square(n):
        num_fair_and_square += 1
        #print n, "is fair and square"
    print "Case #"+str(i)+": "+str(num_fair_and_square)

def is_square(n):
  result = False
  sqrt = int(math.sqrt(n))
  if n == (sqrt * sqrt):
    result = True
  return result

def calculate_squares(start, end):
  squares_in_range = []
  first_square_root = None
  for i in range (start, end+1):
    if is_square(i):
      first_square_root = int(math.sqrt(i))
      break
  
  if first_square_root is None:
    return []
  
  cur_addition = first_square_root + (first_square_root + 1)
  cur_square = i
  
  while (cur_square <= end):
    squares_in_range.append(cur_square)
    cur_square += cur_addition
    cur_addition += 2

  return squares_in_range

# if is square
def is_fair_and_square(n):
  result = False
  n = int(n)
  sqrt = int(math.sqrt(n))
  if is_palindrome(sqrt): #sqrt is smaller, check it first
    if is_palindrome(n):
      result = True

  return result
    
def is_palindrome(n):
  result = True
  n = str(n)
  length = len(n)
  last = length - 1
  for i in range(0, length):
    if n[i] is not n[last-i]:
      result = False
      break
      
  return result
  
if __name__ == "__main__":
  main()