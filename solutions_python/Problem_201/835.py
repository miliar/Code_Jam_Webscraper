from bisect import *

def split(N):
    if N == 1:
        return 0, 0
    s = (N - 1) // 2
    return N - s - 1, s

def insert(l, c, x, m):
    i = bisect_left(l, x)
    if i < len(l) and l[i] == x:
        c[i] += m
    else:
        l.insert(i, x)
        c.insert(i, m)

def solve(N, K):
    l = [N]
    c = [1]
    while K > 0:
        largest = l.pop()
        count = c.pop()

        s1, s2 = split(largest)

        if count >= K:
            return s1, s2

        insert(l, c, s1, count)
        insert(l, c, s2, count)

        K -= count

def main():
    num_cases = int(input())
    for c in range(num_cases):
        N, K = map(int, input().split(' '))
        print('Case #{}: {}'.format(c + 1, ' '.join(map(str, solve(N, K)))))

main()
