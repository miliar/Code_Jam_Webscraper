import sys
from collections import Counter
from copy import deepcopy

temp = sys.stdout
sys.stdout = open(r'C:\Users\Spin\Desktop\o.txt', 'w')

Q = open(r'C:\Users\Spin\Desktop\t.txt')
# Q = open(r'C:\Users\Spin\Desktop\t.txt')
T = int(Q.readline())

def sol(s, k):
    s = [c == '+' for c in s]
    cnt = 0
    while s:
        last = s[-1]
        if last:
            s.pop()
        else:
            if len(s) < k:
                return 'IMPOSSIBLE'
            else:
                s[-k:] = [not c for c in s[-k:]]
                cnt += 1

    return cnt




for line in range(T):
    s, k = Q.readline().split()
    k = int(k)
    res = sol(s, k)
    print('Case #%r:' % (line + 1), res)

sys.stdout = temp
