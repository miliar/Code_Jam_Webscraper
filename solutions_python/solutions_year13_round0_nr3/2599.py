from math import sqrt

input = open("/home/doohyunl/C-small-attempt0.in", 'rb').readlines()

cases = int(input[0])

def is_palindrome(n):
    num_as_str = str(n)
    return num_as_str == num_as_str[::-1] 

def is_fair_and_square(n):
    v = int(sqrt(n))
    return (float(v) == sqrt(n)) and (is_palindrome(v))

for i in xrange(cases):
    case = input[i+1].split()
    case = [int(n) for n in case]
    palindromes = [n for n in xrange(case[0], case[1]+1) if is_palindrome(n)]
    fair_and_square = [n for n in palindromes if is_fair_and_square(n)]
    print "Case #{0}: {1}".format(i+1, len(fair_and_square))

