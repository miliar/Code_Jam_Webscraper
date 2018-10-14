#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class StuckError(Exception):
    pass


def greedy_choice(cur_score, requirements):
    solved = True
    easy_choice = None
    easy_hard_req = None
    for i,(a,b) in enumerate(requirements):
        if b is not None and b <= cur_score:
            return i, 2

        if a is not None and a <= cur_score:
            if easy_hard_req is None or b > easy_hard_req:
                easy_choice = i
                easy_hard_req = b

        if a is not None or b is not None:
            solved = False
    if solved:
        return None
    elif easy_choice is not None:
        return easy_choice, 1
    else:
        raise StuckError

def shortest_path(requirements):
    try:
        cur_score = 0
        steps = 0
        while True:
            choice = greedy_choice(cur_score, requirements)
            if choice is None:
                return steps
            else:
                idx, level = choice
                if level == 1:
                    assert requirements[idx][0] <= cur_score
                    requirements[idx][0] = None
                    cur_score += 1
                elif requirements[idx][0] is not None:
                    requirements[idx] = (None, None)
                    cur_score += 2
                else:
                    requirements[idx][1] = None
                    cur_score += 1
                steps += 1
    except StuckError:
        return None

def main():
    numcases = int(sys.stdin.readline())
    for i in xrange(numcases):
        numlevels = int(sys.stdin.readline())
        reqs = []
        for _ in xrange(numlevels):
            a,b = sys.stdin.readline().strip().split()
            a,b = int(a), int(b)
            reqs.append([a,b])
        answer = shortest_path(reqs)
        if answer is None:
            answer = 'Too Bad'
        print 'Case #{case}: {answer}'.format(case=i+1, answer=answer)

if __name__ == '__main__':
    main()
