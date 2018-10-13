#!/usr/bin/env python

import sys

vowels = 'aeiou'


def ngram_val(sub, n):
    if all(map(lambda l: l not in vowels, sub[:n])):
        return len(sub) - n + 1
    else:
        return 0

def process(_):
    name, n = sys.stdin.readline().split(' ')
    n = int(n)

    total = 0

    ngram_vals = (ngram_val(name[i:], n) for i in xrange(len(name)-n+1))

    last_val = 0
    tot = 0
    for v in reversed(list(ngram_vals)):
        if v:
            last_val = v
            tot += v
        else:
            tot += last_val
    return tot

if __name__ == '__main__':
    results = []

    N_cases = int(sys.stdin.readline())
    for i in xrange(N_cases):
        results.append('Case #{}: {}'.format(i+1, process(i)))

    sys.stdout.write('\n'.join(results))
