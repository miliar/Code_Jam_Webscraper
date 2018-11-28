import itertools
import math

def is_valid(data, order):
    new_data = [ data[i] for i in order]
    for i in range(len(new_data) - 1):
        if new_data[i][0] < new_data[i + 1][0]:
            return False
    return True

def calc(data, order):
    new_data = [ data[i] for i in order]
    ans = 0
    for i in range(len(new_data) - 1):
        ans += 2. * math.pi * new_data[i][0] * new_data[i][1]
        ans += math.pi * (new_data[i][0] ** 2 - new_data[i+1][0] ** 2);
    ans += 2. * math.pi * new_data[-1][0] * new_data[-1][1]
    ans += math.pi * (new_data[-1][0] ** 2);
    return ans


def solve():
    (n, k) = map(int, input().split())
    data = []
    for i in range(n):
        (r, h) = map(int, input().split())
        data.append([r, h])

    ans = -1.
    for seq in itertools.permutations(range(n), r=k):
        if is_valid(data, seq):
            ans = max(ans, calc(data, seq))

    return "{0:.7f}".format(ans)

if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        print("Case #" + str(test + 1) + ": " + str(solve()))

