from math import pi
from typing import List, NamedTuple, Dict, IO, Tuple
from pathlib import Path


class Pancake(object):
    radius: float
    height: float

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @property
    def lateral_surface(self) -> float:
        return self.radius * 2 * pi * self.height

    @property
    def surface(self) -> float:
        return (self.radius ** 2) * pi


class Case(NamedTuple):
    howmany: int
    pancakes: List[Pancake]

def read_case(f: IO) -> Case:
    pan = []
    total, howmany = (int(x) for x in f.readline().split())
    for _ in range(total):
        radius, height = (float(x) for x in f.readline().split())
        pan.append(Pancake(radius, height))

    return Case(howmany, pan)


def read_input(f: IO) -> List[Case]:
    T = int(f.readline())
    return [read_case(f) for _ in range(T)]


def solve_rec(candidates: List[Pancake], left: int, idx: int, cache) -> float:
    if (idx, left) in cache:
        return cache[(idx, left)]

    if left > 0 and idx >= len(candidates):
        return -1

    if left == 0:
        return 0

    s = candidates[idx].surface if left == 1 else 0

    m = max(
        candidates[idx].lateral_surface + solve_rec(candidates, left-1, idx+1, cache) + s,
        solve_rec(candidates, left, idx+1, cache),
    )
    cache[(idx, left)] = m
    return m


def solve(case: Case) -> float:
    case.pancakes.sort(key=lambda p: p.radius)
    cache = {}
    return solve_rec(case.pancakes, case.howmany, 0, cache)


def main():
    import sys
    sys.setrecursionlimit(10000)
    for in_path in Path('.').glob('*.in'):
        with in_path.open('r') as f:
            cases = read_input(f)

        out_path = in_path.parent / in_path.name.replace('.in', '.out')
        print(f"solving {in_path} -> {out_path}")
        with out_path.open('w') as out:
            for idx, case in enumerate(cases, start=1):
                solution = solve(case)
                print(f"Case #{idx}: {solution}", file=out)


if __name__ == '__main__':
    main()