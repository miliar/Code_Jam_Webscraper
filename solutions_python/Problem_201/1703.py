import sys
from sortedcontainers import SortedDict


def _debug(spaces):
    print(list(reversed(list(spaces))))


def pop_max(spaces: SortedDict):
    max_n = spaces.iloc[-1]
    max_n_count = spaces[max_n] - 1

    if max_n_count == 0:
        spaces.pop(max_n)
    else:
        spaces[max_n] -= 1

    return max_n


def increment(spaces, key):
    if key in spaces:
        spaces[key] += 1
    else:
        spaces[key] = 1


def split(spaces):
    n = pop_max(spaces)
    increment(spaces, get_min_space(n))
    increment(spaces, get_max_space(n))


def get_min_space(n):
    return (n - 1) // 2


def get_max_space(n):
    n -= 1
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1

for index, line in enumerate(sys.stdin):
    if index == 0:
        continue

    (N, P) = list(map(int, line.split()))
    spaces = SortedDict({N: 1})
    for _ in range(P - 1):
        split(spaces)
    N = pop_max(spaces)
    print(f'Case #{index}:', get_max_space(N), get_min_space(N))
