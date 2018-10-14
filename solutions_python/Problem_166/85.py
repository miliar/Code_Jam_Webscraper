from __future__ import print_function

import sys
import collections
import itertools


def solve(keys, word, S):
    unique_keys = set(keys)
    word_letters = set(word)

    if not word_letters.issubset(unique_keys):
        return 0.0

    unique_start = 1
    while unique_start < len(word):
        if word.startswith(word[unique_start:]):
           break
        unique_start += 1

    counter = collections.Counter(keys)

    prob = {}
    for c, v in counter.items():
        prob[c] = v / len(keys)

    prob_per_starting_point = 1.0
    for l in word:
        prob_per_starting_point *= prob[l]


    starting_points = S - len(word) + 1

    max_bananas = (S - (len(word) - unique_start)) // unique_start

    found = 0
    options = 0
    for option in itertools.product(keys, repeat=S):
        options += 1
        option = "".join(option)

        for i in range(starting_points):
            if option[i:].startswith(word):
                found += 1

    expected = found / options

    # expected = prob_per_starting_point * starting_points



    return max_bananas - expected



fin = sys.stdin

num_cases = int(fin.readline().strip())

for t in range(num_cases):
    _,_,S = [int(x) for x in fin.readline().split()]
    keys = fin.readline().strip()
    word = fin.readline().strip()

    print("Case #{}: {:.6f}".format(t+1, solve(keys, word, S)))