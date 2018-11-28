#!python2
from __future__ import division, print_function

import sys
from pprint import pprint as pp

def result(ans1, tb1, ans2, tb2):
    #pp(ans1)
    #pp(tb1)
    #pp(ans2)
    #pp(tb2)
    s = set(tb1[ans1-1]) & set(tb2[ans2-1])
    l = len(s)
    if l == 1:
        return str(s.pop())
    elif l == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def read_tb():
    return [
        [int(x.strip()) for x in sys.stdin.readline().strip().split(' ')]
        for _ in range(4)
    ]

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        ans1 = int(sys.stdin.readline().strip())
        tb1 = read_tb()
        ans2 = int(sys.stdin.readline().strip())
        tb2 = read_tb()
        print("Case #{}: {}".format(str(t+1), result(ans1, tb1, ans2, tb2)))
