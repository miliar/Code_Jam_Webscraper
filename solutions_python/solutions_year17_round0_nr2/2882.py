# QR 2017
from itertools import zip_longest
from sys import stdin, stdout, stderr


def solve(num):
    if int(num) < 10:
        return num
    ans = []

    highest = int(num[0])
    prev, idx = int(num[0]), 0
    for i, s in enumerate(num):
        s = int(s)
        if highest <= s:
            highest = max(highest, s)
            if s != prev:
                ans.extend([prev] * (i - idx))
                prev = s
                idx = i
        else:
            if highest != 1:
                ans.append(highest - 1)
            ans.extend([9] * (len(num) - idx - 1))
            return int(''.join(str(s) for s in ans))

    ans.extend([prev] * (len(num) - idx))
    return int(''.join(str(s) for s in ans))


if __name__ == "__main__":
    cases = int(stdin.readline())
    for c in range(1, cases + 1):
        num = stdin.readline().split()[0]
        # print(num)
        ans = solve(num)
        stdout.write("Case #{0}: {1}\n".format(c, ans))
