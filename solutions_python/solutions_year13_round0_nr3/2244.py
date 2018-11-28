#!/usr/bin/python
# coding: UTF-8

# T can be either X or O so replace it by both

def palindrome(input_num):
  str_input_num = str(input_num)
  reverse = ''
  n = len(str_input_num)
  for i in range(n/2):
    if str_input_num[i] != str_input_num[n - 1 - i]: return False
  return True

def gen_squares(limit):
  result = []
  i = 1
  while(i ** 2 <= limit): # for the small case
    if palindrome(i):
      result.append(i**2)
    i += 1
  return result

if __name__ == "__main__":
  #f = open('input-task-1.txt')
  #f_out = open('prob_1_out.txt', 'w')
  f = open('C-small-attempt0.in')
  f_out = open('output_prob_3_10', 'w')
  T = int(f.readline()[:-1]) # of input cases
  squares = gen_squares(1000)
  #print squares
  for i in range(T):
    A, B = f.readline()[:-1].split()
    int_A = int(A)
    int_B = int(B)
    result = 0
    while int_A <= int_B:
      if (int_A in squares) and palindrome(int_A):
        result += 1
        #print int_A
      int_A += 1
    f_out.write("Case #" + str(i+1)+ ": " + str(result) + "\n")

