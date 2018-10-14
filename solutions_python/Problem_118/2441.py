import os
import math
import sys
import string
import itertools

#c small
LOW_BOUNDS = 1
HIGH_BOUNDS = 1000
def toNum(str_num):
    num = 0
    rev_str_num = str_num[::-1]
    for decimal in range(len(rev_str_num)):
        num += 10 ** decimal * int(rev_str_num[decimal])
    return num

def generatePalindromes(A, B):
    a_n_digits = countDigits(A)
    b_n_digits = countDigits(B)
    palindromes = []
    for digits in range(a_n_digits, b_n_digits + 1):
        palindromes.extend(generatePalindromesWithNDigits(digits))
    return palindromes

def generatePalindromesWithNDigits(n_digits):
    if (n_digits == 1):
        return list(range(1, 10))
    elif (n_digits == 2):
        return list(range(11, 100, 11))
    return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if n_digits%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in range(1,10)
            for ys in itertools.permutations(range(10), n_digits/2-1)
            for z in (range(10) if n_digits%2 else (None,))]

def isPalindrome(test_str):
    return test_str == test_str[::-1]

def isFair(palindrome):
    #c small
    sq_low = int(math.floor(math.sqrt(palindrome)))
    sq_high = int(math.ceil(math.sqrt(palindrome)))
    return sq_low == sq_high and isPalindrome(str(sq_low))

def countDigits(number):
    if number < 0:
        number *= -1
    digits = 0
    while (number != 0):
        digits += 1
        number //= 10
    return digits

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    fin = open(sys.argv[1], 'r')
    fout = open("output.txt", 'w')
    T = int(fin.readline())
    # generate palindromes before running all cases
    palindromes = generatePalindromes(LOW_BOUNDS, HIGH_BOUNDS)
    for case in range(1, T + 1):
        A, B = [int(t) for t in fin.readline().strip().split()]
        # c small, just iterate each
        subset_palindromes = [p for p in palindromes if p >= A and p <= B]
        count = 0
        for palindrome in subset_palindromes:
            if isFair(palindrome):
                count += 1
        fout.write("Case #%d: %d\n" % (case, count))
    fin.close()
    fout.close()