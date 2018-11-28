#
# IMPORTS
#
import fileinput
import sys

data = fileinput.input()
n = int(data[0])

def flip (signals, k, i):
    for j in range (i - k + 1, i + 1):
        if signals[j] is '+':
            signals[j] = '-'
        else:
            signals[j] = '+'
    return signals
# flip()

def check (signals, k, i, flips):
    if i == k - 1:
        flag = 0
        for j in range(0, k):
            if signals[j] is '+':
                flag = flag + 1
        if flag == 0:
            return flips + 1
        elif flag == k:
            return flips
        else:
            return None
    elif signals[i] is '+':
        return check(signals, k, i - 1, flips)
    elif signals[i] is '-':
        signals = flip(signals, k, i)
        flips = check(signals, k, i - 1, flips)
        if flips is not None:
            return flips + 1
        else:
            return
# check()

for i in range(1, n + 1):
    line = data[i].split()
    signals = list(line[0])
    k = int(line[1])
    result = check(signals, k, len(signals) - 1, 0)
    if result is None:
        result = 'IMPOSSIBLE'

    print('Case #{0}: {1}'.format(i, result))
