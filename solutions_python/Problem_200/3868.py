#contest 170201
import math
import collections
import heapq
import string

def problem_A():
    pass

def problem_B(n):
    size = len(str(n))
    if int('1'*size) > n:
        size -= 1

    top = 1
    str_int = {v:i for i,v in enumerate('0123456789')}
    int_str = {i:v for i,v in enumerate('0123456789')}
    # tidy_stack = []
    tidy_str = ''
    for i in xrange(size,0,-1):
        while top<9 and int(tidy_str+int_str[top+1]*i) <= n:
            top += 1
        tidy_str += int_str[top]
    return tidy_str

def main_B():
    T = int(raw_input())
    for i in xrange(1,T+1):
        n = int(raw_input())
        sol = problem_B(n)
        print "Case #{}: {}".format(i, sol)

def main_A():
    pass

if __name__=='__main__':
    main_B()