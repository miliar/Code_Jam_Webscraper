# http://www.numpy.org/
import numpy as np

import multiprocessing

def choose_stall(stalls):
    used = np.where(stalls)[0]

    mins = []
    maxes = []
    for i, s in enumerate(stalls):
        if s:
            mins.append(-1)
            maxes.append(-1)
            continue

        ls = i - used[used < i][-1] - 1 if len(used[used < i]) > 0 else i
        rs = used[used >= i][0] - i - 1 if len(used[used >= i]) > 0 else len(stalls) - i - 1
        mins.append(min(ls, rs))
        maxes.append(max(ls, rs))

    mins = np.array(mins)
    maxes = np.array(maxes)

    if len(np.where(mins == mins.max())[0]) == 1:
        pos = mins.argmax()
    else:
        maxes[mins != mins.max()] = -1
        pos = maxes.argmax()
    return pos, mins[pos], maxes[pos]

def calculate(n, k):
    stalls = [False] * n
    for _ in range(k):
        index, min_rl, max_rl = choose_stall(stalls)
        stalls[index] = True
    return min_rl, max_rl


if __name__ == '__main__':
    f = open('C-small-1-attempt1.in', 'r')
    lines = f.read().split('\n')[1:-1]

    out = open('output', 'w')

    p = multiprocessing.Pool(8)

    results = []
    for lnum, line in enumerate(lines):
        n, k = [int(s) for s in line.split(" ")]

        results.append(p.apply_async(calculate, (n, k)))

    for lnum, res in enumerate(results):
        min_rl, max_rl = res.get()
        out.write("Case #{}: {} {}\n".format(lnum + 1, max_rl, min_rl))

    out.close()