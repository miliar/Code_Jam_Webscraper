#!/usr/bin/env python
import bisect
import sys
from collections import defaultdict

def main(args):
    finname = '%s.in' % args[1]
    foutname = '%s.out' % args[1]
    with open(finname, 'r') as fin, open(foutname, 'w') as fout:
        T = int(fin.readline().strip())
        for i in xrange(1, T+1):
            num_vines = int(fin.readline().strip())
            vinestats = []
            for j in xrange(num_vines):
                d, l = [int(_) for _ in fin.readline().strip().split()]
                vinestats.append((d, l))

            D = int(fin.readline().strip())

            memo = dict()
            def ok(start_vine, swing_length):
                if (start_vine, swing_length) in memo:
                    return memo[(start_vine, swing_length)]

                vine_d, vine_l = vinestats[start_vine]
                if vine_l < swing_length:
                    swing_length = vine_l
                if vine_d + swing_length >= D:
                    memo[(start_vine, swing_length)] = True
                    return True
                last_vine = bisect.bisect(vinestats, (vine_d+swing_length+1, 0), start_vine)
                
                i = start_vine+1
                result = False
                while i < last_vine:
                    if ok(i, vinestats[i][0]-vine_d):
                        memo[(start_vine, swing_length)] = True
                        return True
                    i+=1
                memo[(start_vine, swing_length)] = False
                return False
            result = 'YES' if ok(0, vinestats[0][0]) else 'NO'
            result_str = 'Case #%s: %s\n' % (i, result)
            # print result_str,
            fout.write(result_str)

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
