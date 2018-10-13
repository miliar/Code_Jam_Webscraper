# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# squares.py
# Python code to find squares that are palindromes.
__author__ = 'nealabq@gmail.com'

def is_palindrome( int_in_question) :
    """
    True if int_in_question is an integer that is a
    palindrome when written in base 10.
    """
    # Change the number into a string and then a list.
    as_list_of_chars = list( str( int_in_question))
    # Copy the list and reverse it.
    reversed_list_of_chars = list( as_list_of_chars)
    reversed_list_of_chars.reverse( )
    # True if the list of chars is palindromic.
    return as_list_of_chars == reversed_list_of_chars

def palindrome_squares_up_to( limit) :
    """
    Prints all the positive integers up to but not
    including limit, where the integer's square is a
    palindrome but the integer itself is not. Also
    prints the square.
    """
    results = []
    for i in range(1, limit + 1):
        if is_palindrome(i) and is_palindrome( i * i):
            results.append(i*i)
    return results

# <codecell>

ps = palindrome_squares_up_to(10000000)

# <codecell>

fi = open("/Users/trunghuynh/Data/GoogleCodeJam/2013/qualification/fair_and_square/in/C-small-attempt0.in")
fo = open("/Users/trunghuynh/Data/GoogleCodeJam/2013/qualification/fair_and_square/out/C-small-attempt0", "w")
N = int(fi.next())
for i in xrange(N):
    row = fi.next().split()
    A, B = int(row[0]), int(row[1])
    c = len([K for K in ps if A <= K <= B])
    print c
    fo.write("Case #%d: %d\n" % (i + 1, c))
fi.close()    
fo.close()

