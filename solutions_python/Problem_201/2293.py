from sortedcontainers import SortedList


def best(n):
    l = r = n // 2
    if n % 2 == 0:
        l -= 1
    return l, r


# print(best(11))

def solve(n, k):
    slots = SortedList([n])
    for i in range(k):
        res = best(slots.pop())
        slots.update(r for r in res if r != 0)

    return sorted(res)

# print(solve(10, 9))

from pathlib import Path
import sys

from tqdm import trange

def main():
    ip = sys.argv[1]
    lines = (l.strip() for l in open(ip))
    t = int(next(lines))

    cases = (map(int, l.split()) for l in lines)

    with open(Path(ip).with_suffix('.out').name, mode='w') as op:
        for i in trange(t):
            case = next(cases)
            r = solve(*case)
            print(f'Case #{i+1}: {r[1]} {r[0]}', file=op)

main()
