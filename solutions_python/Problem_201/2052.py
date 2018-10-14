import math

cases = int(input())

for case in range(1, cases + 1):
    inputs = input().split()
    N = int(inputs[0])
    K = int(inputs[1])
    stalls = ['*'] + ['.'] * N + ['*']
    for person in range(0, K):
        occupied = [i for i, x in enumerate(stalls) if x == "*"]
        differences = [j-i for i, j in zip(occupied[:-1], occupied[1:])]
        biggestGap = differences.index(max(differences))
        target = occupied[biggestGap] + math.floor((occupied[biggestGap + 1] - occupied[biggestGap])/2)
        stalls[target] = '*'
    stalls[target] = '.'
    left = target - ''.join(stalls).rfind('*',0,target) - 1
    right = ''.join(stalls).find('*',target) - target - 1
    print('Case #{}: {} {}'.format(case, max(left, right), min(left, right)))
