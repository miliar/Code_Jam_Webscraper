#!/usr/bin/env python

base = 10
unit = int(base/base)


def clean_up(s, i, digits):
    s[i + 1] = str(base - unit)
    s[i] = str(int(s[i]) - unit)
    for j in range(i, 0, -1):
        if int(s[j]) < int(s[j - 1]):
            s[j] = str(base - unit)
            s[j - 1] = str(int(s[j - 1]) - unit)
        else:
            break
    i = i + 1
    while i < digits:
        s[i] = str(base - unit)
        i = i + 1

    return int("".join(s))


def tidy(s):
    s = list(s)
    digits = len(s)
    if digits <= 1:
        return int("".join(s))

    for i in range(digits-1):
        if int(s[i]) > int(s[i+1]):
            return clean_up(s, i, digits)

    return int("".join(s))


def launch():

    t = int(input())

    for i in range(t):
        x = tidy(str(int(input())))
        print("Case #" + str(i + 1) + ": " + str(x))


if __name__ == "__main__":
    launch()
