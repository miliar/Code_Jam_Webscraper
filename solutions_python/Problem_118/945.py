#!/usr/bin/python
import sys,os
from math import sqrt, ceil, floor


def solve(min, max):
    """Returns a number[int] of fair and square palindromes between min and max"""
    num_fair_n_square = 0
    sqrt_min = int(ceil(sqrt(min)))
    sqrt_max = int(floor(sqrt(max)))
    # for each palindrome between min and sqrt_min and sqrt_max
    for e_palindrome in get_palindromes(sqrt_min, sqrt_max):
        # calculate palindrome square
        palindrome_squared = e_palindrome * e_palindrome
        # if palindrome square is palindrome again increase num_fair_n_square by 1
        if is_palindrome(str(palindrome_squared)):
            num_fair_n_square += 1
        # return num_fair_n_square
    return num_fair_n_square

def get_palindromes(min=0,max=0):
    palindrome = get_next_palindrome(min-1)
    while min <= palindrome <= max:
        yield palindrome
        palindrome = get_next_palindrome(palindrome)

def get_next_palindrome(num):
    str_num = str(num)
    str_num_len = len(str_num)
    odd_len = (str_num_len % 2 != 0)
    head, center = get_head_and_center(str_num)
    if odd_len:
        increment = pow(10, str_num_len / 2)
        new_num = int(head + center + head[::-1])
    else:
        increment = int(1.1 * pow(10, str_num_len / 2))
        new_num = int(head + head[::-1])
    if new_num > num:
        return new_num
    if center != '9':
        return new_num + increment
    else:
        return get_next_palindrome(round_up(num))


def get_head_and_center(str_num):
    len_str_num = len(str_num)
    return str_num[:len_str_num / 2], str_num[(len_str_num - 1) / 2]

def round_up(num):
    length = len(str(num))
    increment = pow(10, ((length / 2) + 1))
    return ((num / increment) + 1) * increment

def is_palindrome(str_num):
    return str_num == str_num[::-1]

#Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        
        cases = int(f_in.readline().strip())
        for case in range(1,cases+1):
            #Get input data
            a, b = [int(x) for x in f_in.readline().strip().split()]
            #Solve and output
            print("Case #{}: {}".format(case, solve(a, b)))
    
if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '"+str(sys.argv[1])+"' does not exist!"
    else:
        print "No file supplied! Run program this way: '"+str(sys.argv[0])+" something.in'"
        
