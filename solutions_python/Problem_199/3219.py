t = int(input())

for i in range(1, t + 1):
    pancakes, K = [s for s in input().split(' ')]
    pancakes = list(pancakes)
    K = int(K)
    moves = 0

    for p in range(len(pancakes)):
        if pancakes[p] == '-':
            moves += 1
            if p+K+1 <= len(pancakes):
                for f in range(p, p+K):
                    pancakes[f] = '+' if pancakes[f] == '-' else '-'
            else:
                for f in range(1, K+1):
                    pancakes[-f] = '+' if pancakes[-f] == '-' else '-'

    if '-' in pancakes:
        moves = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(i, moves))
