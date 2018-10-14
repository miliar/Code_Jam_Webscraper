import sys

temp = sys.stdout
sys.stdout = open(r'C:\Users\Spin\Desktop\o.txt', 'w')

Q = open(r'C:\Users\Spin\Desktop\t.txt')
T = int(Q.readline())

from collections import deque


def sol(n, k):
    if k == n:
        return 0, 0

    counter = {n: 1}
    keys = deque([n])

    while True:
        top = keys.popleft()
        cnt = counter[top]
        left = (top - 1) // 2
        right = top - left - 1

        if k <= cnt:
            return right, left

        counter.pop(top)
        if right in counter:
            counter[right] += cnt
        else:
            keys.append(right)
            counter[right] = cnt

        if left in counter:
            counter[left] += cnt
        else:
            counter[left] = cnt
            keys.append(left)

        k -= cnt


for line in range(T):
    t = map(int, Q.readline().split())
    res = sol(*t)
    print('Case #%r:' % (line + 1), res[0], res[1])

sys.stdout = temp
