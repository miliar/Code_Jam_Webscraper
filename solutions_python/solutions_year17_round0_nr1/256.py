#from functools import lru_cache
from itertools import count

flipper = {
    '+': '-',
    '-': '+'
}

def flip(k, s):
    if len(s) < k:
        return False
    return [ flipper[c] for c in s[:k] ] + s[k:]

def case(k, s, flips=0):
    # find the first unflipped pancake
    def do(k, s):
        i = s.index('-')
        return flip(k, s[i:])

    flips = 0
    try:
        while s:
            s = do(k, s)
            flips += 1
        return "IMPOSSIBLE"
    except ValueError:
        return flips

def cases(data):
    lines = int(data[0])
    for case_number, line in zip(count(1), data[1:]):
        s, k = line.split(' ')
        k = int(k)
        s = list(s)
        result = case(k, s)
        print("Case #{}: {}".format(case_number, result))

with open('input', 'r') as f:
    cases(f.readlines())

