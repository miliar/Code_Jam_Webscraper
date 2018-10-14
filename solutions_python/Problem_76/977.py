#!/usr/bin/env python

def add(x_, y_):
    """
    Given two integer x_ and y_, add in Patrick's way
    """
    x, y = bin(x_)[2:], bin(y_)[2:]
    result = ''
    # string reversed
    x, y = x[::-1], y[::-1]
    if len(x) > len(y):
        temp = (len(x) - len(y)) * '0'
        y = y + temp
    elif len(x) < len(y):
        temp = (len(y) - len(x)) * '0'
        x = x + temp
    for i in range(len(x)):
        if x[i] == y[i]: result = result + '0'
        else: result = result + '1'
    # result reversed
    result = result[::-1]
    # return a decimal value of the reversed binary string
    return int(result, 2)

def check(left, right):
#    if len(left) == 0:
#        l = 0
#    else:
#        l = reduce(lambda x, y: add(x, y), left)
#    if len(right) == 0:
#        r = 0
#    else:
#        r = reduce(lambda x, y: add(x, y), right)
    l = reduce(lambda x, y: add(x, y), left)
    r = reduce(lambda x, y: add(x, y), right)
    if l == r: return True
    else: return False

def compute(l):
    """
    let's see whether Sean can trick Patrick
    """
    result = -1
    if len(l) == 2:
        if l[0] == l[1]: return l[0]
        else: return "NO"
    from itertools import combinations
    for length in range(1, len(l)):
        for left in combinations(l, length):
            right = []
            for i in l:
                if i not in left:
                    right.append(i)
            if check(left, right):
                temp = max(reduce(lambda x, y: x + y, left), reduce(lambda x, y: x + y, right))
                if temp > result:
                    result = temp
    if result > -1: return result
    else: return "NO"

if __name__ == "__main__":
    from sys import stdin
    from string import split, strip
    test = int(strip(stdin.readline()))
    for cnt in range(1, test+1):
        size = int(strip(stdin.readline()))
        l = split(stdin.readline())
        for i in range(size):
            l[i] = int(l[i])
        print "Case #%d: %s" %(cnt, compute(l))
