##
# CODEJAM
# prillan91
##
import sys
import re
import math

HEXADECIMAL_DIGITS = {0, 1, 4, 9}
HEXA_SQUARED_DIGITS = set(x**2 % 256 for x in range(0, 256))
DECA_DIGITS = set(x**2 % 10 for x in range(0, 10))
DECA_SQUARED_DIGITS = set(x**2 % 100 for x in range(0, 100))
DECA_SQUARED_STR = set("{:0>2}".format(x) for x in DECA_SQUARED_DIGITS)

POWERS_OF_TWO = [set(x**2 % 2**i for x in range(0, 2**i)) for i in range(2, 20)]

def palindrome_gen(length):
    odd = length % 2
    if length == 0:
        yield 0
    elif length == 1:
        for x in DECA_DIGITS:
            yield x
    elif length == 2:
        for x in DECA_DIGITS:
            if x + 10*x in DECA_SQUARED_DIGITS:
                yield x+10*x
    elif length == 3:
        for y in DECA_SQUARED_STR:
            yield int(y[::-1] + y[1:])
    elif length == 4:
        for y in DECA_SQUARED_STR:
            yield int(y[::-1] + y)
    else:
        #    yyxxxxxyy
        t = ""
        n = "" 
        free = odd + (length - 4) / 2
        print free
        for x in xrange(10**free):
            for y in DECA_SQUARED_STR:
                t = str(x)
                if len(t) < free:
                    t = "0"*(len(t)-free) + t
                    
                # print y
                # print t
                if odd == 0:
                    n = ''.join([y[::-1], t[::-1], t, y])
                else:
                    n = ''.join([y[::-1], t[::-1], t[1:], y])
                yield int(n)
def is_palindrome(p):
    s = str(p)
    for i in range(len(s) / 2 + 1):
        if s[i] != s[len(s) - (1+i)]:
            return False
    return True
def sqrt(n):
    return int(math.floor(math.sqrt(n) + 0.5))
def is_square(n):
    t = sqrt(n)
    return t*t == n

def is_fair_n_square(p):
    for i in range(len(POWERS_OF_TWO)):
        if p < 2**i:
            break
        if not (p & (2**i - 1) in POWERS_OF_TWO[i]):
            return False
    if not is_square(p):
        return False
    root = sqrt(p)
    return is_palindrome(root)

def solveSingle(f):
    A, B = tuple(int(x) for x in f.readline().strip().split(" "))
    
    minlength = int(math.floor(math.log10(A)))
    maxlength = int(math.ceil(math.log10(B)))

    count = 0
    
    for l in range(minlength, maxlength+2):
        for p in palindrome_gen(l):
            if p < A or p > B:
                continue                
            if is_fair_n_square(p):
                count += 1
    return count

def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        

if __name__ == "__main__":
    solve()
