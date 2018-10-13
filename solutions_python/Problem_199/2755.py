from typing import Tuple, Union


def flip_pancakes(s: str, k: int) -> Tuple[int, str]:
    '''Brute force - but can be done in O(n) using DP'''
    ps = [c for c in s]
    flips = 0
    for idx in range(0, len(s) - k + 1):
        if ps[idx] != '+':
            flips += 1
            for idy in range(idx, idx + k):
                ps[idy] = ['-', '+'][ps[idy] == '-']
    return flips, ''.join(ps)


def pancakes(s: str, k: int) -> Union[int, str]:
    forward_flips, forward_ps = flip_pancakes(s, k)
    if '-' in forward_ps:
        return 'IMPOSSIBLE'
    else:
        return forward_flips


def solve() -> None:
    n = int(input())
    for idx in range(n):
        s, k = input().split()
        k_int = int(k)
        print('Case #{}: {}'.format(idx + 1, pancakes(s, k_int)))


solve()
