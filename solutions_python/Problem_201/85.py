import sys
import bintrees


def score(n):
    return int(n/2), int((n-1)/2)


def sikanie(n, k):
    tree = bintrees.RBTree()
    tree.insert(n, 1)
    while True:
        m, v = tree.pop_max()
        if k <= v:
            return score(m)
        for i in score(m):
            curr = tree.pop(i) if i in tree else 0
            tree.insert(i, v+curr)
        k -= v
    return tree.get(n)


file_name = sys.argv[1]
with open(file_name) as file:
    T = int(file.readline())
    for x in range(T):
        N, K = file.readline().split(' ')
        result = sikanie(int(N), int(K))

        print('Case #{}: {} {}'.format(x+1, max(result), min(result)))