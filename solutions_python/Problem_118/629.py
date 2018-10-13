#!/usr/bin/python

import sys
import math


def is_palindrome( current_integer ):
    int_as_str = str( current_integer )
    reversed_int_as_str = int_as_str[::-1]
    return int_as_str == reversed_int_as_str

def top_middle_is_small_enough( top, middle, upper_bound ):
    bottom = top[::-1]
    total = top + middle + bottom
    if int( total ) <= upper_bound:
        return True
    else:
        return False

def increment_top_middle( top, middle ):
    if middle == '':
        top_len = len( top )
        top = int( top )
        top += 1
        top = str( top )
        # We made it bigger by incrementing
        if top_len != len( top ):
            middle = '0'
            top = top[:-1]
    elif middle == '9':
        top_len = len( top )
        if top == '':
            top = '0'
        top = int( top )
        top += 1
        top = str( top )
        if top_len != len( top ):
            middle = ''
        else:
            middle = '0'
    #if middle != '9' and middle != '':
    else:
        middle = int( middle )
        middle += 1
        middle = str( middle )
    return top, middle

def get_viable_palindromes( lower_bound, upper_bound ):
    tops = []
    middles = []
    lb_as_list = list( str( lower_bound ) )
    num_digits = len( lb_as_list )
    top = lb_as_list[:num_digits/2]
    top = ''.join( top )
    middle = ''
    if num_digits % 2:
        middle = lb_as_list[num_digits/2]
    while top_middle_is_small_enough( top, middle,upper_bound ):
        tops.append( top )
        middles.append( middle )
        top, middle = increment_top_middle( top, middle )
        #print "Just got ", top, "and", middle
    palindromes = []
    for i in range( len( tops ) ):
        palindromes.append( int( tops[i] + middles[i] + tops[i][::-1] ) )
    return palindromes


with open(sys.argv[1]) as f:
    content = f.readlines()

num_cases = int(content[0].split()[0])
for case in range(num_cases):
    lower_bound_str, upper_bound_str = content[case+1].split()
    lower_bound = int( lower_bound_str )
    upper_bound = int( upper_bound_str )

    # Get the bounds we really care about
    sqrt_lower_bound = int( math.sqrt( lower_bound ) )
    sqrt_upper_bound = int( math.sqrt( upper_bound ) )

    # Some checks on our bounds
    sqrt_lower_bound -= 1
    while sqrt_lower_bound**2 < lower_bound:
        sqrt_lower_bound += 1
    while (sqrt_upper_bound+1)**2 <= upper_bound:
        sqrt_upper_bound += 1


    lower_palindromes = get_viable_palindromes( sqrt_lower_bound, sqrt_upper_bound )
    final_palindromes = []
    for value in lower_palindromes:
        square = value**2
        if is_palindrome( square ) and lower_bound <= square and square <= upper_bound:
            final_palindromes.append( square )

    # Construct each palindrome in the range
    # WE MIGHT NEED TO ADD A get_first_palindrome THAT IS MORE COMPLICATED
    #palindromes_in_lower_range = []
    #next_palindrome = get_next_palindrome( lower_bound-1 )
    #while next_palindrome <= sqrt_upper_bound:
        #palindromes_in_lower_range.append( next_palindrome )
        #next_palindrome = get_next_palindrome( next_palindrome )
        #print next_palindrome


    # For each palindrome in the lower range, square it and see if it's one in the larger range

    #print sqrt_lower_bound, sqrt_upper_bound
    #print lower_palindromes
    #print final_palindromes
    print "Case #" + str(case+1) + ":", len( final_palindromes )
