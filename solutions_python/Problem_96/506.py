#!/usr/bin/env python
'''
Juan Manuel Caicedo
cavorite.com
'''

import sys


def valid_score(s, total):
    m = min(s)
    x = max(s)
    if x - m > 2:
        return False, 0, 0

    if x > 10:
        return False, 0, 0

    if m < 0:
        return False, 0, 0

    t = sum(s)
    valid = t == total

    return valid, x, x - m == 2

def max_scores(total):
    avg = total / 3
    r = total % 3

    if r == 0:
        scores = [
            (avg + 1, avg - 1, avg),
            (avg, avg, avg),
        ]
        
    elif r == 2:
        scores = [
            (avg + 2, avg , avg),
            (avg + 1, avg + 1, avg),
        ]
        
    else:
        scores = [
            (avg + 1, avg, avg),
        ]
        
    score = 0
    score_surp = None
    for s in scores:
        valid, mx, surp = valid_score(s, total)
        if not valid:
            continue

        if surp:
            score_surp = mx
        else:
            score = mx
            
    return score, score_surp



def best_results(totals, p, surprises):
    max_values = [max_scores(t) for t in totals]
    max_values.sort(reverse=True)

    n = 0
    for (s_normal, s_surp) in max_values:
        if s_normal >= p:
            n += 1
        elif surprises > 0 and s_surp >= p:
            n += 1
            surprises -= 1

    return n

def main():
    lines = sys.stdin

    cases = int(lines.next())
    for i in xrange(1, cases+1):
        l = lines.next()
        line = map(int, l.split())
        g = line[0]
        surprises = line[1]
        p = line[2]
        scores = line[3:]

        n = best_results(scores, p, surprises)
        print 'Case #%d: %s' % (i, n)


if __name__ == '__main__':
    main()
    

