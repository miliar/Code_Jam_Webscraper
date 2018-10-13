from itertools import product
import numpy as np
from math import factorial
import sys
import time

def get_num_substrings(S, L):
    return S-L+1

def count_substrings(prod, target):
    count = 0
    start = None
    while (start > 0) or (start == None):
        start = prod.find(target, start if None != start else 0) + 1
        if start > 0:
            count+=1
    return count

def get_max_and_mean_occurence(target, vocab, S):
    target_counter = 0.0
    total_counter = 0.0

    st = [vocab]*S
    it = product(*st)
    max_occurence = 0

    for i in it:
        sub_count = count_substrings(''.join(i), target)
        if sub_count > max_occurence:
            max_occurence = sub_count
        target_counter += sub_count
        total_counter += 1

    return max_occurence, target_counter/float(total_counter)


def get_remaining_bananas(target, vocab, S, L):
    if set(target).difference(vocab):
        return 0.0

    mx, mn = get_max_and_mean_occurence(target, vocab, S)
    return mx - mn


if __name__=='__main__':
    #start = time.time()
    count = 0
    for i in sys.stdin:
        if count == 0:
            count += 1
            acc = 3
            continue
        if acc == 3:
            K, L, S = map(int, i.split())
            acc -= 1
            continue
        if acc == 2:
            vocab = i.strip()
            acc -= 1
            continue
        if acc == 1:
            target = i.strip()

        print 'Case #%d:' % (count), get_remaining_bananas(target, vocab, S, L)
        count += 1
        acc = 3
    #print time.time() - start
