#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser('CodeJam Problem')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-i', '--infile', metavar='INFILE', 
                    help='input file to process, stdin if omitted')
args = parser.parse_args()

if args.infile:
    f_in = open(args.infile)
else:
    f_in = sys.stdin

def solve(query):
    return None # Replace...


def solve(M, rownum, colnum):
    empty_rows = []
    for i, row in enumerate(M):
        if all(c == '?' for c in row):
            empty_rows.append(i)
            continue
        else:
            row[0] = [c for c in row if c != '?'][0]
            for pos in range(1, colnum):
                if row[pos] == '?':
                    row[pos] = row[pos-1]
    #  Now take care of all-empty rows
    if 0 in empty_rows:
        first_good = [r for r in range(rownum) if r not in empty_rows][0]
        M[0] = M[first_good][:]
    for rownum in empty_rows:
        if rownum == 0:
            continue
        else:
            M[rownum] = M[rownum -1][:]
    return M
    
def print_matrix(M):
    for row in M:
        print(''.join(c for c in row))
        

lines = [line.strip() for line in f_in if line.strip()]
trial_tot = int(lines[0])
lindex = 1
trial_num = 1
while lindex < len(lines):
    # First read sizes
    rows, cols =  map(int, lines[lindex].split())    
    lindex +=1
    M = [[None for _ in range(cols)] for __ in range(rows)]
    # print("rows = {}  cols = {}".format(rows, cols))
    for row_num in range(rows):
        M[row_num] = [c for c in lines[lindex]]
        # if len(M[row_num]) != cols:
        #     print("Expected {} cols, and got {}".format(cols, len(M[row_num])))
        lindex +=1
    
    # print(M)
    solution = solve(M, rows, cols)
    print("Case #{}:".format(trial_num))
    print_matrix(M)
    trial_num +=1
    
