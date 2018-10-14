import numpy as np
import math

def is_palindrome(number):
   number_string = str(number)
   length = len(number_string)
   first_half = number_string[0:length/2]
#   print number, ":", first_half
   if length%2 == 1:
      second_half = number_string[(length/2):length]
   else:
      second_half = number_string[(length/2)+1:length]

   second_half = number_string[((length-1)/2)+1:length]
#   print second_half
   if first_half == second_half[::-1]:
      return True
   else:
      return False

def numbers(i, j):
   i_number = "1"
   j_number = ""
   for k in range(i-1):
      i_number += "0"
   for k in range(j):
      j_number += "9"
   return (int(i_number), int(j_number))

f = open('C-small-attempt1.in', 'r')
g = open('output.txt', 'w')

test_cases = int(f.readline())
print test_cases
for i in range(1, test_cases+1):
   dimensions = map(int, f.readline().split(' '))
#  print dimensions
   lower = dimensions[0]
   upper = dimensions[1]
   sqrt_lower_digits = len(str(lower))/2
   sqrt_upper_digits = (len(str(upper))+1)/2

   sqrt_lower, sqrt_upper = numbers(sqrt_lower_digits, sqrt_upper_digits)
#  print sqrt_lower, sqrt_upper
   count = 0

   for j in range(sqrt_lower, sqrt_upper):
      if is_palindrome(j):
         sqj = j**2
         if is_palindrome(sqj):
       #     print j, sqj
            if sqj>=lower and sqj<=upper:
               count += 1
#               print j, sqj
   is_palindrome(11211)
#   print count
   g.write("Case #" + str(i) + ": " + str(count) + "\n")
