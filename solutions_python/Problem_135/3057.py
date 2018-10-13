__author__ = 'Nova'

import sys
sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for t in range(1, T+1):
    ans1 = int(input())
    a1 = [0] * 4
    for i in range(4):
        a1[i] = list(map(int, input().split()))
    ans2 = int(input())
    a2 = [0] * 4
    for i in range(4):
        a2[i] = list(map(int, input().split()))

    s1 = set(a1[ans1-1])
    s2 = set(a2[ans2-1])
    ss = s1 & s2
    p = len(ss)
    if p == 1:
        res = str(list(ss)[0])
    elif p == 0:
        res = 'Volunteer cheated!'
    else:
        res = 'Bad magician!'
    print("Case #{0}: {1}".format(t, res))
