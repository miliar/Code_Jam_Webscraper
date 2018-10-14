import sys


def tidy(n):
    r = ""
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            r = n[:i] + chr(ord(n[i]) - 1) + '9' * (len(n) - i - 1)

            if i > 0 and n[i] == n[i - 1]:
                return tidy(r)
            else:
                break

    if len(r):
        return r
    else:
        return n


nums = open(sys.argv[1])

[print("Case #{}: {}".format(n, tidy(x.strip()).lstrip('0'))) for (n, x) in enumerate(nums) if n > 0]
