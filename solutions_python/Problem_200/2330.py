from sys import stdin
import collections
import functools

DEBUG = False


def debug_print(*args):
    if DEBUG:
        print args

def to_digits(n):
    digits = []
    while n:
        digit = n % 10

        digits += [digit]

        # remove last digit from number (as integer)
        n //= 10

    return digits

def tidy(n):
    if n < 10:
        return True

    digits = str(n)
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    return True

def nearest_tidy(n):
    if tidy(n):
        return n
    while True:
        n -= 1
        if tidy(n):
            return n


def solve(n):
    if tidy(n):
        return n
    digits = str(n)
    while True:
        #print 'digits', digits
        if tidy(int(digits)):
            return digits
        for i in range(len(digits) - 1):
            partial = int(digits[i] + digits[i+1])
            #print 'first', i, partial
            if tidy(partial):
                #print 'tidy'
                continue
            new = str(nearest_tidy(partial))
            if i > 0:
                if len(new) == 1:
                    new = '0' + new
            #print 'new', new, digits
            digits = digits[:i] + new + '9' * len(digits[i+2:])
            #print digits
            break

tidy_to_least_most = {}

def main():
    # last_nt = 0
    # out = ''
    # for n in range(4000):
    #     nt = nearest_tidy(n)
    #     if nt != last_nt:
    #         if out != '':
    #             out += str(n-1)
    #             print out
    #             out = ''
    #         last_nt = nt
    #         out += str(nt) + ' ' + str(n) + ','
    num_cases = int(stdin.readline())
    for case in range(1, num_cases + 1):

        n = int(stdin.readline().strip())

        out = solve(n)

        print "Case #{}: {}".format(case, out)

if __name__ == "__main__":
    main()
