#!/usr/bin/python

from math import sqrt
from sys import argv, exit

def square_palindromes_in(low, high):
    count = 0
    for i in range(low, high + 1):
        if is_square_palindrome(i):
            count += 1
    
    return count

def is_square_palindrome(number):
    smaller = sqrt(number)
    if smaller % 1 != 0:
        return False
    else:
        number = str(number)
        smaller = str(int(smaller))
    
    if number == number[::-1] and smaller == smaller[::-1]:
        return True
    return False

if __name__ == "__main__":
    try:
        infile = open(argv[1],'r').read().splitlines()
    except:
        print("Malformed file or no filename given")
        exit()
    
    cycles = int(infile[0])
    del(infile[0])
    
    for cycle in range(cycles):
        [low, high] = [int(x) for x in infile[cycle].split()]
        print("Case #%d: %d" % (cycle + 1, square_palindromes_in(low, high)))
        