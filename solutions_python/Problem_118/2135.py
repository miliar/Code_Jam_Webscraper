# https://code.google.com/codejam/contest/2270488/dashboard#s=p2
# Solution here should work on first two datasets (numbers smaller than 10**14),
# definitely not on last (10**100)

from math import sqrt

def reverse(x):
    """ return a number with the digits of x reversed """
    return int(str(int(x))[::-1])

def is_palindrome(x):
    return x == reverse(x)

def fair_and_square(a, b):
    """ return number of fair and square numbers between a and b """
    count = 0
    for x in range(a, b+1):
        if is_palindrome(x) and is_palindrome(sqrt(x)):
            count += 1
    return count

if __name__ == "__main__":
    count = input()
    for i in range(count):
        vals = map(int, raw_input().split())
        print "Case #" + str(i+1) + ": " + str(fair_and_square(vals[0], vals[1]))
