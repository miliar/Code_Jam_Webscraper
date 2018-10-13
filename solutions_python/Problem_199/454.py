from __future__ import print_function, unicode_literals


def flip(pancakes, K, index):
    if index > len(pancakes) - K:
        return False

    for i in range(index, index + K):
        pancakes[i] = not pancakes[i]

    return True


def solve(pancakes, K, index=0):
    ans = 0
    for i in range(index, len(pancakes) - K + 1):
        if not pancakes[i]:
            flip(pancakes, K, i)
            ans += 1

    return ans if all(pancakes) else None

if __name__ == '__main__':
    N = int(raw_input())
    for Ni in range(N):
        pancakes, K = raw_input().strip().split(" ")
        pancakes = map(lambda x: True if x == "+" else False, pancakes)
        K = int(K)

        best = solve(pancakes, K, index=0)
        ans = "IMPOSSIBLE" if best is None else best
        print("Case #{}: {}".format(Ni + 1, ans))
