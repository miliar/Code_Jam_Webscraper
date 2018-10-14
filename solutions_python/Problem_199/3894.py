#!/usr/bin/env python
import sys

def solve(t, k, case_info,f):
    filp_time = f

    if check(case_info) == 1 :
        #import pdb; pdb.set_trace()

        return str(filp_time)
        
    else:
        left_case = left(case_info)

        if len(left_case) >= k:
            filp_time = filp_time+1
            after_case = flipper(left_case,k)

            return solve(t,k,after_case,filp_time)
        else:
            return 'IMPOSSIBLE'
            


def flipper(case_info,k):
    after_flipper = []

    for i in case_info[:k]:
        if i is '+':
            after_flipper.append('-')
        else:
            after_flipper.append('+')
    for i in case_info[k:]:
        after_flipper.append(i)
            
    return after_flipper


def left(case_info):
    count = 0
    for i in case_info:
        if i is '-':
            return case_info[count:]
        else:
            count = count +1


def check(case_info):
    for i in case_info:
        if i is '-':
            return 0
    return 1        



def process(f):
    case_num = int(f.readline())
    for t in xrange(case_num):
        case_info, kk = f.readline().strip().split()
        k = int(kk)
        filp_time = 0
        s = solve(t, k, case_info, filp_time)


        print 'Case #%d: %s' % (t+1, s)

def main():
    with open(sys.argv[1]) as f:
        process(f)

if __name__ == '__main__':
    main()
