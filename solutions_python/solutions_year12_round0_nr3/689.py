# -*- coding:utf-8 -*-
import os
basepath = '/Users/voidus/Documents/workspace/xp/jam/files/recycling'

srcfilename = os.path.join(basepath, 'C-small-attempt0.in')
dstfilename = os.path.join(basepath, 'C-small-attempt0.out.txt')

def solve(A, B):
    result = 0
    len_b = len(str(B))
    mask = '%%%dd' % len_b
    for i in xrange(A, B):
        for j in xrange(i+1, B+1):
            i_s = mask % i
            j_s = mask % j
            for sp in xrange(1, len_b):
                if i_s[sp:] + i_s[:sp] == j_s:
                    result += 1
                    break
    return result

if __name__ == '__main__':
    with open(srcfilename, 'rb') as inp:
        with open(dstfilename, 'wb') as outp:
            lines = inp.readlines()
            count = int(lines.pop(0))
            outlines = []
            for i in xrange(count):
                A, B = [int(digit) for digit in lines[i].split()]
                result = solve(A, B)
                outlines.append('Case #%d: %d\n' % (i+1, result))
            outp.writelines(outlines)
