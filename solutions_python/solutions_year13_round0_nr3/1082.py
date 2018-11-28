import sys
import math

def check_palindrome(number):
  for i in range(0,len(number)/2):
    if number[i] != number[len(number)- 1 - i]:
      return False
  return True

num_problems = int(sys.stdin.readline())
for i in range(0,num_problems):
  problem = sys.stdin.readline().split()
  lowest_square = int(math.ceil(math.sqrt(int(problem[0]))))
  highest_square = int(math.floor(math.sqrt(int(problem[1]))))
  count = 0
  for j in range(lowest_square,highest_square+1):
    if check_palindrome(str(j)) and check_palindrome(str(j*j)):
      count += 1
  print "Case #" + str(i+1) + ": " + str(count)
