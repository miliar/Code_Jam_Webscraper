#!/usr/bin/env python3


def get_ans():
    return int(input())


def get_mas():
    return [[x for x in input().split()] for i in range(4)]


for i in range(int(input())):
    ans1 = get_ans()
    mas1 = get_mas()

    ans2 = get_ans()
    mas2 = get_mas()

    m = set(mas1[ans1 - 1]) & set(mas2[ans2 - 1])
    s = "Case #{0}: ".format(i + 1)
    l = len(m)
    if l == 0:
        s += "Volunteer cheated!"
    if l == 1:
        s += m.pop()
    elif l > 1:
        s += "Bad magician!"
    print(s)