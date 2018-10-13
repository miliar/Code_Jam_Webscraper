import sys
from collections import Counter
from copy import deepcopy

temp = sys.stdout
sys.stdout = open(r'C:\Users\palzle\Desktop\o.txt', 'w')

Q = open(r'C:\Users\palzle\Desktop\t.txt')
T = int(Q.readline())


from collections import Counter

from collections import Counter

def sol(c, n, k=2):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    res = []
    rank = c.most_common()
    rank = [(cnt, char) for char, cnt in rank]
    rank.sort()
    rank = {rank[i][1]: i for i in range(len(rank))}

    for _ in range(n // k):
        c += Counter()
        fill = c.items()
        if len(fill) < k:
            # print('@@@')
            return 'IMPOSSIBLE'
        fill = [(cnt, rank[char], char) for char, cnt in fill]
        fill.sort(reverse=True)
        for j in range(2):
            char = fill[j][2]
            res.append(char)
            c[char] -= 1

    remain = n % k
    if remain:
        c += Counter()
        for char in c:
            res.append(char)
            break

    # print(res)
    if res[0] == res[-1]:
        # print('###')
        return 'IMPOSSIBLE'
    return ''.join(res)



for w in range(T):
    print('Case #%r:' % (w + 1), end=' ')
    N, R, O, Y, G, B, V = map(int, Q.readline().split())
    d = {'R':R, 'Y':Y, 'B':B}
    c = Counter(d)
    res = sol(c, N)
    print(res)


sys.stdout = temp
