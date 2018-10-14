import argparse
import collections
import fractions
import functools
import itertools
import math
import operator

from sys import exit, stdin
from multiprocessing import Pool

def solve_star(args):
    return solve(*args)

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return [int(n) for n in stdin.readline().strip().split()]

def read_floats():
    return [float(n) for n in stdin.readline().strip().split()]

def read_words():
    return stdin.readline().strip()

def parse():
    x = read_ints()[1]
    l = read_words()
    return [x, l]

dict = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
        'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}
        }

def multiply(x, y):
    s0 = -1 if len(x) == 2 else 1
    v = dict[x[-1]][y]
    s1 = -1 if len(v) == 2 else 1
    sign = '' if s0 * s1 == 1 else '-'
    #print(x, "times", y, "is", sign + v[-1])
    return sign + v[-1]

def solve_k(s):
    v = '1'
    for i in range(len(s)):
        c = s[i]
        v = multiply(v, c)
    return v == 'k'

def solve_j(s, j):
    v = '1'
    for i in range(j, len(s)):
        if (v, i) in jcache:
            break
        jcache.add((v, i))
        c = s[i]
        v = multiply(v, c)
        if v == 'j':
            if solve_k(s[(i + 1):]):
                return True
    return False

jcache = set()
#kcache = set()

def solve(x, l):
    jcache.clear()
    #kcache.clear()
    s = l * x
    v = '1'
    for i in range(len(s)):
        c = s[i]
        v = multiply(v, c)
        if v == 'i':
            if solve_j(s, i + 1):
                return "YES"
    return "NO"
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--multi", help="turn on multiprocessing", action="store_true")
    args = parser.parse_args()
    
    with open("out.txt", "w") as f:
        if args.multi:
            pool = Pool()
            iter = pool.imap(solve_star, (parse() for i in range(read_int())))
            for i, result in enumerate(iter):
                s = "Case #{}: {}".format(i + 1, result)
                print(s)
                f.write(s + "\n")
        
        else:
            for i in range(read_int()):
                s = "Case #{}: {}".format(i + 1, solve(*parse()))
                print(s)
                f.write(s + "\n")
