#!/usr/bin/env python3

def calc():
    s, cnt = input().split()
    cnt = int(cnt)

    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = 0

    rep = [0] * len(s)
    mset = []
    for i, x in enumerate(s):
        if x in vowels:
            rep[i] = 1

        if rep[i] == 1:
            rep[i] = 0
        else:
            rep[i] = (rep[i - 1] if i > 0 else 0) + 1

        if rep[i] >= cnt:
            mset += [i]
            res += (i - cnt + 2) * (len(s) - i)

    res = 0
    slen = len(s)
    for i, x in enumerate(rep):
        while len(mset) > 0 and mset[0] - cnt + 1 < i:
            mset = mset[1:]

        if len(mset) == 0:
            break

        res += slen - mset[0]



    return res


if __name__ == '__main__':
    cnt = int(input())
    for T in range(cnt):
        print("Case #{}: {}".format(T + 1, calc()))

