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
    return stdin.readline().strip().split()

def parse():
    d = []
    c, i, v = read_ints()
    #for j in range(i):
    d = read_ints()
    return [c, d, v]

def solve(c, d, v):
    e = []
    sums = set()
    for dd in d:
        for i in range(c):
            e.append(dd)
    addable = set(range(1, v + 1)) - set(d)
    for counter in itertools.count():
        for addedcombo in itertools.combinations(addable, counter):
            sums = set()
            f = e[:]
            for ac in addedcombo:
                for i in range(c):
                    f.append(ac)
            for i in range(1, len(f) + 1):
                for combo in itertools.combinations(f, i):
                    sums.add(sum(combo))
            if all(z in sums for z in range(1, v + 1)):
                return counter
    

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
