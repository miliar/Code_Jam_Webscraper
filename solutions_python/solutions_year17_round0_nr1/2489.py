import numpy as np

with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def flip(x):
    for i in xrange(len(x)):
        x[i] = 0 if x[i] == 1 else 1
    return x


def count_pancakes(s, k):
    s = [0 if s[i] == '-' else 1 for i in xrange(len(s))]
    if sum(s) == len(s):
        return 0
    k = int(k)
    n_flips = 0
    print s, k
    for i in xrange(len(s)):
        if s[i] == 0 and len(s[i:i + k]) == k:
            s[i:i + k] = flip(s[i:i + k])
            n_flips += 1
    if sum(s) < len(s):
        return 'IMPOSSIBLE'
    else:
        return n_flips


f = open('out.txt', 'w')
for i in xrange(1, t + 1):
    s, k = lines[i].split(' ')
    print s, k
    print('Case #%s: %s \n' % (i, count_pancakes(s, k)))
    f.write('Case #%s: %s \n' % (i, count_pancakes(s, k)))
f.close()
