from collections import deque


def flip(pancakes, K):
    for i in range(K):
        if pancakes[i] == '+':
            pancakes[i] = '-'
        else:
            pancakes[i] = '+'


def solve(pancakes, K):
    #  print(pancakes)
    if len(pancakes) < K:
        raise
    if len(pancakes) == K:
        if all(p == '-' for p in pancakes):
            return 1
        elif all(p == '+' for p in pancakes):
            return 0
        else:
            raise
    if pancakes[0] == '+':
        pancakes.popleft()
        return solve(pancakes, K)
    else:
        flip(pancakes, K)
        pancakes.popleft()
        return 1 + solve(pancakes, K)

for case in range(int(input())):
    pancakes, K = input().split()

    try:
        ans = solve(deque(pancakes), int(K))
    except:
        ans = 'IMPOSSIBLE'
    print('Case #%d: %s' % (case+1, ans))
