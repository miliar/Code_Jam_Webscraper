from __future__ import print_function

def flip_consecutive(pattern, start, count):
    for i in range(start, start + count):
        if pattern[i] == '+':
            pattern[i] = '-'
        else:
            pattern[i] = '+'

def calc_flips(pattern, width):
    flips = 0
    #print('pattern is', ''.join(pattern))
    for i in range(len(pattern) - width + 1):
        #print('checking position', i)
        if pattern[i] == '-':
            #print('flipping {} at position {}'.format(width, i))
            flip_consecutive(pattern, i, width)
            #print('pattern is', ''.join(pattern))
            flips += 1
    if '-' in pattern:
        return 'IMPOSSIBLE'
    return flips

line_count = int(raw_input())
for case in range(line_count):
    p, w = raw_input().split()
    p = list(p)
    w = int(w)
    print('Case #{}: {}'.format(case + 1, calc_flips(p, w)))
