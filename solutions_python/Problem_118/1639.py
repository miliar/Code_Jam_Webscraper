import sys
import math
import itertools

def read_int(fp=sys.stdin):
    return int(fp.readline().strip())

def read_ints(fp=sys.stdin):
    return map(int, fp.readline().strip().split())

def palindrome(word):
    word = str(word)
    return word == word[::-1]

def sqrt(number):
    return int(number ** 0.5)

def palindromes(length):
    def combine(i, skip=0):
        s = str(i)
        return int(s + s[::-1][skip:])

    if length % 2: length += 2

    i  = int(10 ** int(length / 2 - 1))
    hi = int(10 ** int(length / 2))

    while i < hi:
        yield combine(i, length % 2)
        i += 1

def count_fair_and_square_numbers_simple(lo, hi):
    count = 0
    for i in range(sqrt(lo), sqrt(hi) + 1):
        if i ** 2 >= lo and palindrome(i) and palindrome(i ** 2):
            count += 1
    return count

def count_fair_and_square_numbers(lo, hi):
    count = 0
    minlen = int(math.log(sqrt(lo), 10))
    maxlen = int(math.log(sqrt(hi), 10) + 1)
    for l in range(minlen, maxlen + 1):
        for i in palindromes(l):
            if i ** 2 >= lo and i ** 2 <= hi and palindrome(i ** 2):
                count += 1
    return count

if __name__ == "__main__":
    T = read_int()
    for t in range(1, T+1):
        lo, hi = read_ints()
        count = count_fair_and_square_numbers(lo, hi)
        # assert count == count_fair_and_square_numbers_simple(lo, hi)
        print "Case #%d: %d" % (t, count)
