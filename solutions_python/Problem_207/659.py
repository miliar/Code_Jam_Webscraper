#!/usr/bin/env python3

import sys
import argparse
import operator

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

lines = [line.strip() for line in f_in if line.strip()]
trial_tot = int(lines[0])
# print("{} total trials\n".format(trial_tot), file=sys.stderr)
lindex = 1
trial_num = 1
while lindex < len(lines):
    N, R, O, Y, G, B, V = map(int, lines[lindex].split())
    amts = {'R':R, 'O':O, 'Y':Y, 'G':G, 'B':B, 'V':V}
    lindex +=1
    if O == 0 and G == 0 and V == 0:
        # Small dataset goes here...
        if R > N/2 or Y > N/2 or B > N/2:
            print("Case #{:d}: {}".format(trial_num, 'IMPOSSIBLE'))
            trial_num +=1
            continue
        spots = N * ['']
        for i, (color, num) in enumerate(sorted(amts.items(), 
                                        key = operator.itemgetter(1),
                                        reverse=True)):
            if i == 0:
                for pos in range(num):
                    topcolor = 2 * pos
                    spots[topcolor] = color
                # print(spots)
            elif i == 1:
                for pos in range(num):
                    current = (topcolor + 1 + (2 * pos) + (N % 2)) % N
                    spots[current] = color
                # print(spots)
            else:
                for pos in range(N):
                    if spots[pos] == '':
                        spots[pos] = color
                # print(spots)
        print("Case #{:d}: {}".format(trial_num, ''.join(spots)))
        trial_num +=1
    else:
        # Large dataset goes here...
        print("Case #{:d}: {}".format(trial_num, "Can't do this yet..."))
    
f_in.close()
