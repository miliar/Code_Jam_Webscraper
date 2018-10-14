from typing import NamedTuple, List, Union


class Case(NamedTuple):
    pancakes: List[int]
    k: int


def read_input(path: str):
    cases: List[Case] = []
    with open(path, 'r') as f:
        f.readline()
        for line in f:
            p, k = line.split(' ')
            pancake = [0 if c == '-' else 1 for c in p]
            cases.append(Case(pancake, int(k)))

    return cases


def flip(l: List[int], i: int, ik: int):
    for j in range(i, ik):
        l[j] = 0 if l[j] == 1 else 1

def solve(case: Case) -> Union[int, str]:
    pk = case.pancakes
    k = case.k
    flips = 0
    for i in range(0, len(pk) - k + 1):
        if pk[i] == 1:
            continue

        flip(pk, i, i+k)
        flips += 1

    if any(x != 1 for x in pk):
        return "IMPOSSIBLE"

    return flips



def main():
    cases = read_input('A-large.in')
    print(cases)
    with open('output.txt', 'w') as out:
        for idx, case in enumerate(cases, start=1):
            solution = solve(case)
            print(f"Case #{idx}: {solution}", file=out)

if __name__ == '__main__':
    main()