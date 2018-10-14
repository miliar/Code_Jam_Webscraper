#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def getto_time(seq, color):
    last_pos = 1
    for c, pos in seq:
        if c == color:
            yield abs(pos - last_pos)
            last_pos = pos

def solve(seq):
    times = {}
    times["O"] = iter(getto_time(seq, 'O'))
    times["B"] = iter(getto_time(seq, 'B'))
    last_push = {}
    last_push["O"] = 0
    last_push["B"] = 0
    cur_time = 0
    for color, pos in seq:
        next_time = max(times[color].next() + last_push[color], cur_time)
        cur_time = next_time + 1
        last_push[color] = cur_time
    return cur_time
        

def main():
    sys.stdin.readline()
    for case,line in enumerate(sys.stdin):
        fields = line.strip().split()
        seq = []
        for i in xrange(1, len(fields), 2):
            seq.append((fields[i], int(fields[i+1])))
        print "Case #%d: %d" % (case+1, solve(seq))

if __name__ == '__main__':
    main()
