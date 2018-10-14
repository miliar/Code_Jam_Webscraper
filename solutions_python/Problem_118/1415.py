from util import *
from cmath import sqrt
from time import time

THRESH = 10 ** 29

def is_palindrome(i):
    i_str = str(int(i.real))
    length = len(i_str) / 2
    valid = True

    j = 0
    while j < length:
        if i_str[j] != i_str[-j - 1]:
            valid = False
            break
        j += 1

    return valid

def fair_and_sqr(num, input):
    lower, upper = [ int(a) for a in readline(input).split()] 

    ret = 0
    for i in xrange(lower, upper + 1):
        # for i < 10 ** 29
        if i <= THRESH:
            i_sqrt = sqrt(i)
            if i_sqrt % 1 != 0.0: continue
        else:
            assert False

        if is_palindrome(i_sqrt) and is_palindrome(i):
            ret += 1

    print "Case #%d: %d" % (num, ret)


if __name__ == "__main__":
    process(fair_and_sqr)



