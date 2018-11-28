import math
import sys
import os


def int_to_list(x):
    lst = []

    while x > 0:
        lst.append(x % 10)
        x /= 10

    return lst[-1::-1]

def list_to_int(lst):
    x = 0

    for i in lst:
        x *= 10
        x += i

    return x


def is_tidy(x):
    c = 10
    
    while x > 0:
        nc = x % 10
        if nc > c:
            return False
        c = nc
        x = x / 10

    return True

def convert(x, i, parent):

    if i >= len(x):
        return True
    elif x[i] < parent:
        return False
    else:
        child = convert(x, i + 1, x[i])
        if child:
            return True
        elif x[i] == parent:
            return False
        else:
            x[i] -= 1
            x[i+1:] = [9 for _ in xrange(i+1, len(x))]
            return True

def func(i):
    n = int(sys.stdin.readline())

    # while n > 0:
    #     if is_tidy(n):
    #         return n
    #     n -= 1

    x = int_to_list(n)
    done = convert(x, 0, 0)

    if not done:
        raise "Wtf?"
    
    ans = list_to_int(x)

    if not is_tidy(ans):
        raise "Wtf tidy?"

    return ans


def inp(t):

    for i in xrange(1, t + 1):
        ans = func(i)
        print "Case #{0}: {1}".format(i, ans)

    return


def main(argv):

    t = int(sys.stdin.readline())

    inp(t)

    return


if __name__ == "__main__":
    main(sys.argv)
