import sys

sys.setrecursionlimit(10000)

def solve(pancakes, k, tries=0):
    # assumes that both ends are happy side down

    if not pancakes:
        return tries
    else:
        tries += 1

    if len(pancakes) < k:
        return "IMPOSSIBLE"

    if pancakes[0] is False:
        # flip the first k
        for i in range(k):
            pancakes[i] = not pancakes[i]
        # remove the positive ones on the left
        if all(pancakes):
            return tries
        unhappy = pancakes.index(False)
        new_pancakes = pancakes[unhappy:]
        return solve(new_pancakes, k, tries)
    elif pancakes[-1] is False:
        # flip the last k
        for i in range(1, 1+ k):
            pancakes[-i] = not pancakes[-i]
        if all(pancakes):
            return tries
        while pancakes[-1] is True:
            pancakes.pop()
        return solve(pancakes, k, tries)

if __name__ == '__main__':
    t = int(input())
    for case in range(1, 1+t):
        pancake_str, k_str = input().split()
        pancake_str = pancake_str.strip("+")
        pancakes = [cake == "+" for cake in pancake_str]
        k = int(k_str)
        answer = solve(pancakes, k)
        print("Case #{}: {}".format(case, answer))
