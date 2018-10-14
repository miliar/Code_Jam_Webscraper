#coding: utf-8
import sys
INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large.out'
sys.stdin = file(INPUT_FILE, 'r')
sys.stdout = file(OUTPUT_FILE, 'w')


def process(N):
    find = False
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            find = True
            N[i] -= 1
            for j in range(i+1, len(N)):
                N[j] = 9
    return find

T = int(raw_input())
for case in xrange(1, T+1):
    N = map(int, list(raw_input()))
    while process(N): pass
    print 'Case #%d: %s' % (case, (''.join(map(str, N))).lstrip('0'))
