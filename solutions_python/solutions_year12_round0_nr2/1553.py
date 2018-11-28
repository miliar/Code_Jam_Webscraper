#!/usr/bin/env python

import sys

def get_suprisement(total,p):
    min_not_suprising_vote = p-1
    min_suprising_vote = p-2
    if min_suprising_vote < 0: min_suprising_vote = 0
    if min_not_suprising_vote < 0: min_not_suprising_vote = 0
    
    if total >= p + 2 * min_not_suprising_vote: return 0 # not suprising
    elif total >= p + 2 * min_suprising_vote: return 1 # suprising
    else: return 2

def solve(N,S,p,totals):
    totals.sort(reverse=True)
    res = 0
    for total in totals:
        suprisement = get_suprisement(total,p)
        if suprisement == 0:
            res+=1
        elif suprisement == 1 and S > 0:
            res +=1
            S -= 1
        else:
            break
    return res
        

cases_no = int(sys.stdin.readline())
for case_no in xrange(cases_no):
    case_data = map(int,sys.stdin.readline().split())
    [N,S,p] = case_data[:3]
    totals = case_data[3:]
    res = solve(N,S,p,totals)
    print "Case #%d: %d" % (case_no+1, res)
