import numpy as np


def flip_counter_slow(is_happy, k):
    n = len(is_happy)
    flips = 0
    for i in range(n-k+1):
        if is_happy[i] != 1:
            is_happy[i:i+k] = ~is_happy[i:i+k]
            flips += 1

    if np.all(is_happy):
        return flips
    else:
        return 'Impossible'

def flip_counter_fast(is_happy, k):
    n = len(is_happy)
    flipped = 0
    flips = 0
    last_flip = -2*k
    for i in range(n-k+1):
        x = is_happy[i]

        if x != flipped:
            # happy side up
            continue
        else:
            # plain side up
            flipped = (flipped + 1) % 2
            # TODO

    if np.all(is_happy):
        return flips
    else:
        return 'Impossible'

if __name__=='__main__':
    # PATH_IN = 'sample.in'
    PATH_IN = 'A-large.in'
    PATH_OUT = 'A-large.out'
    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = next(f_in)
    for i, line in enumerate(f_in):
        pancakes, k = line.split()
        k = int(k)
        n = len(pancakes)
        is_happy = np.array([1 if c == '+' else 0 for c in pancakes]).astype(bool)
        res = flip_counter_slow(is_happy, k)
        print('Case #%i: %s' % (i+1, res))
        f_out.write('Case #%i: %s\n' % (i+1, res))
