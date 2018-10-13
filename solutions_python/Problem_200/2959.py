from typing import List


def digits(n: int) -> List[int]:
    d = []
    while n > 0:
        d.append(n % 10)
        n //= 10
    return d

def is_tidy(d: List[int]) -> bool:
    for i in range(len(d) - 1):
        if d[i] > d[i + 1]:
            return False
    return True

def combine(d: List[int]) -> int:
    dd = d
    n = 0
    for i in range(0, len(dd)):
        n *= 10
        n += dd[i]
    return n

def solve(n: int) -> int:
    d = list(reversed(digits(n)))

    while True:
        if is_tidy(d):
            return combine(d)

        k = len(d)

        for i in range(k - 1):
            if d[i] > d[i + 1]:
                d[i] -= 1
                for j in range(i + 1, k):
                    d[j] = 9
                break

        while d[0] == 0: # cut off zeros
            d = d[1:]


    raise RuntimeError

def __test():
    assert (solve(132) == 129)
    assert (solve(1000) == 999)
    assert (solve(7) == 7)
    assert (solve(111111111111111110) == 99999999999999999)

__test()

def main():
    from sys import stdin
    lines = stdin.readlines()
    n = int(lines[0])
    for i, line in enumerate(lines[1: n + 1]):
        n = int(line)
        res = solve(n)
        print("Case #{}: {}".format(i + 1, res))

main()
