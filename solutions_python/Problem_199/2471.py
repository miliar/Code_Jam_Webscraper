import sys

sys.setrecursionlimit(2 ** 30)

"""
flipping is commutative, so flipping left-to-right and right-to-left yields same result
it's not useful to flip already good substrings
"""

INF = 2 ** 20


def flip(d, k, p):
    assert len(d) > k + p - 1
    assert 0 <= p

    flipped = "".join(["+" if c == "-" else "-" for c in d[p:p + k]])
    ret = d[:p] + flipped + d[p + k:]
    # if flipped == "-" * k:
    #    return None
    # print("flip", d, k, p, ret, flipped)
    return ret


def solve(d, k):
    if all(c == "+" for c in d):
        return 0
    if len(d) < k:
        return INF
    if d[0] == "+":
        return solve(d[1:], k)
    return 1 + solve(flip(d, k, 0), k)


def main():
    t = int(input())

    for tc in range(t):
        d, k = input().split(" ")
        k = int(k)

        # print(t, tc, d, k)
        res = solve(d, k)
        if res >= INF:
            print("Case #{}: IMPOSSIBLE".format(tc + 1))
        else:
            print("Case #{}: {}".format(tc + 1, res))


"""

1
---+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+----+-++-+++++-+-+- 3



"""

if __name__ == "__main__":
    def eq(d, k, want):
        got = solve(d, k)
        if got != want:
            print("-" * 10)
            print("in solve(", d, ", ", k, ")")
            print("got  ", got)
            print("want ", want)


    eq("---+-++-", 3, 3)
    eq("+++++", 4, 0)
    eq("-+-+-", 4, INF+2)

    assert flip("+++", 3, 0) == "---"
    assert flip("-++", 1, 0) == "+++"
    assert flip("++-", 1, 2) == "+++"
    assert flip("+--", 2, 1) == "+++"
    assert flip("---", 3, 0) == "+++"
    assert flip("---", 1, 0) == "+--"
    assert flip("---", 1, 2) == "--+"
    assert flip("---", 2, 1) == "-++"

    main()
