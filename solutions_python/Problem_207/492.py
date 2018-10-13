import sys
from itertools import *

name = "B-small-attempt1"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for test_case in range(T):
    n, r, o, y, g, b, v = (int(x) for x in input().strip().split())
    if r > y + b or y > r + b or b > y + r:
        ans = "IMPOSSIBLE"
    else:
        ans = ''
        last = ''
        sort = sorted([[r, 'r'], [y, 'y'], [b, 'b']], key=lambda x:x[0], reverse = True)
        while sort[0][0] != 0:
            ans += sort[0][1]
            if sort[1][0]:
                ans += sort[1][1]
            sort[0][0] -= 1
            sort[1][0] -= 1
            sort.sort(key=lambda x:x[0], reverse = True)
        if ans[0] == ans[-1]:
            ans_mod = list(ans)
            if ans_mod[-4] != ans_mod[-1]:
                temp = ans_mod[-3]
                ans_mod[-3] = ans_mod[-1]
                ans_mod[-1] = temp
            else:
                temp = ans_mod[-2]
                ans_mod[-2] = ans_mod[-1]
                ans_mod[-1] = temp
            ans = ''.join(ans_mod)


    print("Case #" + str(test_case + 1) + ": " + str(ans.upper()))