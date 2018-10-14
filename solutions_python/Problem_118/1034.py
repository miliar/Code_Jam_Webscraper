#!/usr/bin/python2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inp")
args = parser.parse_args()

def palindrome(x):
    return str(x) == str(x)[::-1]

def num_fairnsquare(a, b):
    i = 0
    num = 0
    while True:
        i += 1
        if i*i >= a:
            if i*i > b:
                return num
            if palindrome(i) and palindrome(i*i):
                num += 1

lines = open(args.inp).readlines()
t = int(lines[0])
for case in range(1,t+1):
    split = lines[case].split()
    a = int(split[0])
    b = int(split[1])
    print "Case #{0}: {1}".format(case, num_fairnsquare(a, b))
