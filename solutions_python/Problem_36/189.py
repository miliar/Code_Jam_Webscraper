#!python

TARGET = "welcome to code jam"

from collections import defaultdict

solved_pairs = defaultdict(int)

def num_matches(input, tar):
    t_len = len(tar) - 1
    i_len = len(input) - 1

    if tar[t_len] == input[i_len]:
        solved_pairs[(0, 0)] = 1

    for i in xrange(1, i_len+1):
        for t in xrange(0, t_len+1):
            if t > i:
                solved_pairs[(i, t)] = 0
            if input[i_len - i] == tar[t_len - t]:
                if t == 0:
                    solved_pairs[(i, t)] = 1 + solved_pairs[(i-1, t)]
                else:
                    solved_pairs[(i, t)] = solved_pairs[(i-1, t)] + solved_pairs[(i-1, t-1)]
            else:
                solved_pairs[(i, t)] = solved_pairs[(i-1, t)]

#    print solved_pairs

    return solved_pairs[(i_len, t_len)]

import sys

if len(sys.argv) != 2:
    print "Must supply a filename as the only arugment."
    exit(-1)

filename = sys.argv[1]

fh = open(filename, 'r')

fn = fh.read().split('\n')

n = int(fn[0])
fn = fn[1:]

for i in xrange(0, n):
    case = fn[i]
    solved_pairs = defaultdict(int)
    print "Case #%d: %s" % (i+1, str(num_matches(case, TARGET) % 10000).zfill(4))
