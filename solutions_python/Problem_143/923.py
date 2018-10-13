#codeing=utf8

import sys
import os
import copy


def main(infile, outfile):
    if os.path.exists(outfile):
        os.remove(outfile)
    lines = open(infile, 'r').readlines()
    case_num = int(lines[0].strip())
    for i in range(case_num):
        case = lines[i + 1]
        res = get_result(case)
        print 'case %d' % (i+1)
        open(outfile, 'a').write('Case #%d: %d\n' % (i+1, res))


def get_result(case):
    s = case.strip().split()
    A = int(s[0])
    B = int(s[1])
    K = int(s[2])
    cnt = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                cnt += 1
    return cnt


main(sys.argv[1], sys.argv[2])