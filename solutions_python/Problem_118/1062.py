'''
Created on 2013/04/13

@author: hanaue51
'''

import os
os.chdir("../../../data/2013/qualification/")
filename = "C-small-attempt0"
postfix_in = ".in"
postfix_out = ".out"

def multiply(number0, number1):
    result = [0]
    
    for place0 in xrange(len(number0)):
        for place1 in xrange(len(number1)):
            if len(result) <= place0 + place1:
                result.append(0)
            digit = result[place0 + place1] + number0[place0] * number1[place1]
            carry = digit / 10
            if carry > 0:
                if len(result) <= place0 + place1 + 1:
                    result.append(0)
                result[place0 + place1 + 1] += carry
            result[place0 + place1] = digit % 10
    
    return result

def is_fair(number):
    result = True
    
    if len(number) > 1:
        half_len = len(number) / 2
        for i in xrange(half_len):
            if number[i] != number[- (i + 1)]:
                result = False
                break
    
    return result

def compare(number0, number1):
    result = 0
    
    if len(number0) > len(number1):
        result = 1
    elif len(number0) < len(number1):
        result = -1
    else:
        for i in xrange(len(number0) - 1, -1, -1):
            if number0[i] > number1[i]:
                result = 1
                break
            elif number0[i] < number1[i]:
                result = -1
                break
    
    return result

def next_number(number):
    result = number[:]
    
    if len(result) < 1:
        result = [1]
    else:
        result[0] += 1
        place = 0
        while result[place] >= 10:
            carry = result[place] / 10
            result[place] %= 10
            if len(result) <= place + 1:
                result.append(0)
            result[place + 1] += carry
            place += 1
    
    return result

def next_fair_number(number):
    if len(number) == 0:
        result = [1]
    elif len(number) == 1:
        if number[0] >= 9:
            result = [1, 1]
        else:
            result = [number[0] + 1]
    else:
        odd_digits = (len(number) % 2 != 0)
        half_len = len(number) / 2
        upper_digits = number[-half_len:]
        lower_digits = number[:half_len]
        
        upper_digits_reversed = upper_digits[:]
        upper_digits_reversed.reverse()
        sgn = compare(upper_digits_reversed, lower_digits)
        if sgn > 0:
            result = upper_digits_reversed[:]
            if odd_digits:
                result.append(number[half_len])
            result.extend(upper_digits)
        elif sgn < 0:
            upper_digits_next = next_number(upper_digits)
            result = upper_digits_next[:]
            result.reverse()
            if odd_digits:
                result.append(number[half_len])
            result.extend(upper_digits_next)
        else:
            if odd_digits:
                if number[half_len] >= 9:
                    upper_digits_next = next_number(upper_digits)
                    if len(upper_digits_next) > len(upper_digits):
                        result = upper_digits_next[:]
                        result.reverse()
                        result.extend(upper_digits_next)
                    else:
                        result = upper_digits_next[:]
                        result.reverse()
                        result.append(0)
                        result.extend(upper_digits_next)
                else:
                    result = number[:]
                    result[half_len] += 1
            else:
                upper_digits_next = next_number(upper_digits)
                if len(upper_digits_next) > len(upper_digits):
                    result = upper_digits_next[1:]
                    result.reverse()
                    result.extend(upper_digits_next)
                else:
                    result = upper_digits_next[:]
                    result.reverse()
                    result.extend(upper_digits_next)
    return result

def count_fair_square_numbers(lower, upper):
    result = 0
    
    number = [1]
    while True:
        square = multiply(number, number)
        if compare(square, upper) > 0:
            break
        elif compare(square, lower) >= 0 and is_fair(square):
            result += 1
        number = next_fair_number(number)
    
    return result

results = []
format = "Case #%d: %s\n"

# read inputs
infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

cases_count = int(lines[0].strip())
for i in xrange(cases_count):
    elements = lines[i + 1].strip().split()
    lower = [int(digit) for digit in elements[0]]
    lower.reverse()
    upper = [int(digit) for digit in elements[1]]
    upper.reverse()
    results.append(format % (i + 1, count_fair_square_numbers(lower, upper)))

# write results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
