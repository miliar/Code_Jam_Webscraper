import cProfile
import bisect
from collections import Counter
from functools import lru_cache

def parse(fn):
    results = []
    f = open(fn)
    output = open(fn + '.output', 'w')
    # skip first line
    next(f)
    case = 1
    for line in f:
        N, K = [int(n) for n in line.split(' ')]
        result = '{} {}'.format(*occupy([N], K))
        print(result)
        print('Case #{}: {}'.format(case, result), file=output)
        case += 1
    f.close()
    output.close()



@lru_cache()
def split(N):
    left = max(int((N + 1) / 2) - 1, 0)
    right = int(N / 2)
    return left, right


def pop(stalls, counter):
    longest = stalls[-1]
    counter[longest] -= 1
    if not counter[longest]:
        stalls.pop()
        del counter[longest]
    return longest

def add(stalls, counter, item):
    counter[item] += 1
    # First time appear
    if counter[item] == 1:
        bisect.insort_right(stalls, item)

def occupy(stalls, K):
    counter = Counter({stalls[0]: 1})
    while K:
        longest = pop(stalls, counter)
        left, right = split(longest)

        add(stalls, counter, left)
        add(stalls, counter, right)
        K -= 1

    return max(left, right), min(left, right)


    # return occupy(stalls, K)

# cProfile.run('occupy([1000000], 264003)')
# start = time.time()
# print(occupy([999], 127))

# print(occupy_old([999], 127))
# print(occupy([1000000], 264003))
# print(time.time() - start)
# parse('sample.in')
parse('C-small-2-attempt1.in')
# parse('sample.in')