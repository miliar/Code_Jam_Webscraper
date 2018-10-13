#!/usr/bin/env python3
import os
import sys

problem = sys.argv[1]
path = os.path.expanduser('~/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'

with open(file_in, 'rb') as fin, open(file_out, 'w') as fout:
    lines = fin.read().splitlines()
    case = 1
    for l in lines[1:]:
        _len = len(l)
        _last_reset_index = _len
        digits = [int(s) for s in l]
        for i in range(_len, 1, -1):
            if digits[i - 1] < digits[i - 2]:
                digits[i - 2] -= 1
                for j in range(i - 1, _last_reset_index):
                    digits[j] = 9
                _last_reset_index = i - 1
        start = 0
        if digits[0] == 0:
            start = 1
        fout.write("Case #%d: %s\n" % (case, ''.join(map(str, digits[start:]))))
        case += 1
