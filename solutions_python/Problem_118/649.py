from decimal import _sqrt_nearest
import sys
import cmath
import math

__author__ = 'sladiwal'

fname = "test.txt"

UBER_DICT = []


def ispalindrome(word):
    word = str(word)
    return word == word[::-1]


def precompute(upper):
    x = int(math.floor(math.sqrt(upper)))
    global UBER_DICT
    for y in range(x):
        number = y + 1
        if ispalindrome(number):
            square = number * number
            if ispalindrome(square):
                UBER_DICT.append(square)


def search(a, b):
    count = 0
    for i in UBER_DICT:
        if i > b:
            break
        if a <= i <= b:
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    f = open(fname, "r")
    precompute(int(math.pow(10, 14)))
    # print UBER_DICT
    T = int(f.readline())
    for x in range(T):
        A, B = f.readline().rstrip().split(' ')
        sys.stdout.write('Case #%d: ' % (x + 1))
        print search(int(A), int(B))



