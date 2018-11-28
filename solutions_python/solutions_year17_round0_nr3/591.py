from typing import List, NamedTuple, Tuple
from pathlib import Path

import heapq


class Case(NamedTuple):
    N: int
    K: int


def read_input(f) -> List[Case]:
    f.readline()
    for line in f:
        n, k = (int(k) for k in line.split())
        yield Case(N=n, K=k)


def solve(case: Case) -> Tuple[int, int]:
    k = case.K
    h: List[int] = [-case.N]
    nd = {case.N: 1}
    mins, maxs = -1, -1

    while k > 0:
        largest = -heapq.heappop(h)
        howmany = nd[largest]
        del nd[largest]

        k -= howmany

        if largest % 2 == 0:
            mins, maxs = largest // 2 -1, largest // 2
        else:
            mins = maxs = largest // 2

        nd.setdefault(mins, 0)
        if nd[mins] == 0:
            heapq.heappush(h, -mins)
        nd[mins] += howmany

        nd.setdefault(maxs, 0)
        if nd[maxs] == 0:
            heapq.heappush(h, -maxs)
        nd[maxs] += howmany

    return (maxs, mins)

def solve_heap(case: Case) -> Tuple[int, int]:
    h: List[int] = [-case.N]
    mins, maxs = -1, -1
    for i in range(case.K):
        if not h:
            return (0, 0)

        if i % 1000 == 0:
            print(len(h))


        largest = -heapq.heappop(h)

        if largest % 2 == 0:
            mins, maxs = largest // 2 -1, largest // 2
        else:
            mins = maxs = largest // 2
        if mins > 1:
            heapq.heappush(h, -mins)
        if maxs > 1:
            heapq.heappush(h, -maxs)

    return (maxs, mins)


def main():
    for in_path in Path('.').glob('*.in'):
        with in_path.open('r') as f:
            cases = list(read_input(f))

        out_path = in_path.parent / in_path.name.replace('.in', '.out')
        print(f"solving {in_path} -> {out_path}")
        with out_path.open('w') as out:
            for idx, case in enumerate(cases, start=1):
                solution = solve(case)
                print(f"Case #{idx}: {solution[0]} {solution[1]}", file=out)


if __name__ == '__main__':
    main()