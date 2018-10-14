#!/usr/bin/env python
# Bootstrap from https://github.com/arthurdarcet/gcj-bootstrap
# Usage: main.py [input]

import os
import sys


def solve(S, K):
    r = 0
    while len(S) >= K:
        if S[0] == '-':
            r += 1
            for i in range(K):
                S[i] = '+' if S[i] == '-' else '-'

        if '-' not in S: return r
        S = S[S.index('-'):]
    return None if '-' in S else r

def main():
    S, K = read().split(' ')
    y = solve(list(S), int(K))
    return 'IMPOSSIBLE' if y is None else y


# Parameters:
PROBLEM = 'A'
INPUT = 'large'
INPUT_FILE = '{problem}-{input}.in' # None for stdin
OUTPUT_FILE = '{problem}-{input}.out' # None for stdout
DOWNLOAD_DIR = os.path.expanduser('~/Downloads')

# Bootstrap:
def read(f=None):
    return f(in_stream.readline().strip()) if f is not None else in_stream.readline().strip()

def read_array(f=str, split=None):
    return map(f, read().split(split))

def write(s):
    out_stream.write(s)

if len(sys.argv) >= 2:
    assert len(sys.argv) == 2
    INPUT = sys.argv[1]

if INPUT_FILE is None:
    in_stream = sys.stdin
else:
    in_file = INPUT_FILE.format(problem=PROBLEM, input=INPUT)
    down_path = os.path.join(DOWNLOAD_DIR, in_file)
    if not os.path.exists(in_file) and os.path.exists(down_path):
        os.system('mv "{}" "{}"'.format(down_path, in_file))
    in_stream = open(in_file, 'r')

if OUTPUT_FILE is None:
    out_stream = sys.stdout
else:
    out_file = OUTPUT_FILE.format(problem=PROBLEM, input=INPUT)
    out_stream = open(out_file, 'w')

T = read(int)
for t in range(1,T+1):
    write('Case #{0}: {1}\n'.format(t, main()))

