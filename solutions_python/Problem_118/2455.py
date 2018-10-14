import sys
import math as m

###

global all_n_digit_palindromes
all_n_digit_palindromes = [set() for index in xrange(101)]


###
def is_palindrome (number):
    number_str = str(number)
    digits = len(number_str)
    
    if number == 0:
        return False
    
    if digits == 1 and number > 0:
        return True
    elif digits == 2:
        return number % 11 == 0
    else:
        return number_str[0] == number_str[digits-1] and is_palindrome (int(number_str[1:digits-1]))

def generate_for_edge_digits (edge_digit, total_digits):
    s = set([])
    for number in generate_palindromes_for_digits (total_digits - 2):
        s.add (int (str(edge_digit) + str(number) + str(edge_digit)))
        
    return s

def generate_palindromes_for_digits (total_digits):
    if (len (all_n_digit_palindromes[total_digits]) > 0):
        return all_n_digit_palindromes[total_digits]

    if (total_digits == 1):
        all_n_digit_palindromes[1] = range(1, 10)
        
    elif (total_digits == 2):
        all_n_digit_palindromes[2] = [x*11 for x in range(1, 10)]
        
    else:
        for x in range (1, 10):
            all_n_digit_palindromes[total_digits] = generate_for_edge_digits (x, total_digits)
        
    return all_n_digit_palindromes[total_digits]
 
def generate_palindromes (num1, num2): 
    s = set([])
    for x in xrange (num1, num2 + 1):
        if is_palindrome(x):
            s.add(x);
    return s
'''
def generate_palindromes (num1, num2): 
    s = set([])
    num1 = int(num1)
    num2 = int(num2)

    if (num1 < 10):
        if (num2 < 10): 
            s.update (range(num1, num2 + 1))
            return s
    else:
        s.update(range (num1, 10))

    if (num1 < 100):
        if (num2 < 100):
            for x in xrange(int(m.ceil(num1/11)), int(m.floor(num2/11))+1):
                s.add(int (str(x) + str(x)))
            return s

        for x in xrange(int(m.ceil(num1/11)), 10):
            s.add(int (str(x) + str(x)))

   # by now num2 should be > 100 else it'd have returned

    if (num1 > 100):
        first_num = num1
    else:
        first_num = 100

    first_str = str(first_num)
    second_str = str(num2)
   
    first_digits = len(first_str)
    second_digits = len(second_str)
   
    if (first_digits == second_digits):
      for edge_digit in xrange (int(first_str[0]), int(second_str[0])+1):
         s.update(generate_for_edge_digits (edge_digit, first_digits))
    else: 
      s.update (generate_palindromes (first_num, pow(10,m.ceil(m.log10(first_num)))))
       
      if (first_digits+1 <= second_digits-1):
         for num_digits in xrange(first_digits+1, second_digits-1+1):
            for edge_digit in xrange(1,10):
               s.update(generate_for_edge_digits (edge_digit, num_digits))

      s.update (generate_palindromes (pow(10,m.floor(m.log10(num2))), num2))

    return s
'''
###
f = open ('palin_input.txt', 'r')
out = open("palin_output.txt", "w")

test_cases = int(f.readline())
for test_case in xrange (0, test_cases):
    line = f.readline()
    inputs = map(int, line.split())
    A = inputs[0]
    B = inputs[1]
    A_sqrt = int(m.floor(m.sqrt(A)))
    B_sqrt = int(m.ceil(m.sqrt(B)))
    
    s = generate_palindromes (A_sqrt, B_sqrt)
    ss = [x**2 for x in s]
    final = []
    for number in ss:
        if is_palindrome (number) and number >= A and number <= B:
            final.append(number)
            
    line_out = "Case #" + str(test_case + 1) + ": " + str(len(final)) + "\r\n"
    out.write(line_out)
    print line_out

out.close()