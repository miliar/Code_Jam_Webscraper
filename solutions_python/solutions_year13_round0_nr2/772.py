#!/usr/bin/python2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inp")
args = parser.parse_args()

def row_lower(i, j):
    #print lawn, n, m
    for y in range(0,m):
        if y != j:
            if lawn[i][y] > lawn[i][j]:
                return False
    return True

def col_lower(i, j):
    for x in range(0,n):
        if x != i:
            if lawn[x][j] > lawn[i][j]:
                return False
    return True

def possible_square(i, j):
    return row_lower(i, j) or col_lower(i, j)

def possible(lawn):
    for i in range(0,n):
        for j in range(0,m):
            if not possible_square(i,j):
                #print "not possible {0},{1}".format(i, j)
                return "NO"
    return "YES"

lines = open(args.inp).readlines()
num_cases = int(lines[0])
count = 0
for case in range(0,num_cases):
    count += 1
    nm = lines[count].split()
    n = int(nm[0])
    m = int(nm[1])
    lawn = []
    for x in range(0,n):
        count += 1
        lawn.append([int(x) for x in lines[count].split()])
    print "Case #{0}: {1}".format(case+1,possible(lawn))
