from collections import deque

def min_flips(sequence, k):
    visited = set()
    frontier = deque([(sequence, 0)])
    solutions = []
    while frontier:
        candidate, level = frontier.popleft()
        if candidate in visited:
            continue
        visited.add(candidate)
        
        if is_happy(candidate):
            solutions.append(level)

        for child in children(candidate, k):
            frontier.append((child, level + 1))

    return 'IMPOSSIBLE' if len(solutions) == 0 else min(solutions)

def children(sequence, k):
    descendants = []
    for i in range(len(sequence)):
        copy = list(sequence)
        if i + k > len(sequence):
            break
        for j in range(i, i + k):
            copy[j] = '+' if copy[j] == '-' else '-'
        descendants.append(tuple(copy))
    return descendants

def is_happy(sequence):
    for c in sequence:
        if c != '+':
            return False
    return True

T = int(input())
for t in range(1, T + 1):
    sequence, number = input().split(' ')
    sequence = tuple(sequence)
    k = int(number)
    result = min_flips(sequence, k)
    print('Case #{}: {}'.format(t, result))




