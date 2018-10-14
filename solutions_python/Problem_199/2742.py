from typing import Optional


def solve(ss: str, k: int) -> Optional[int]:
    # diff = ss.count('-')
    # if diff % k != 0:
    #     return None

    s = [c for c in ss]

    n = len(s)
    flips = 0
    for i in range(n - k + 1):
        if s[i] == '-':
            flips += 1
            for j in range(i, i + k):
                s[j] = '-' if s[j] == '+' else '+'

    if s.count('-') != 0:
        return None
    else:
        return flips

def __test():
    assert(solve('---+-++-', 3) == 3)
    assert(solve('+++++', 4) == 0)
    assert(solve('-+-+-', 4) == None)

def main():
    from sys import stdin
    lines = stdin.readlines()
    n = int(lines[0])
    for i, line in enumerate(lines[1: n + 1]):
        s, sn = line.split()
        res = solve(s, int(sn))
        print("Case #{}: {}".format(i + 1, res if res is not None else "IMPOSSIBLE"))

main()