#!/usr/bin/env python3


def check_lst(lst):
    s = set(lst)
    if len(s) == 1 and (not list(s)[0] in ('.', 'T')):
        return list(s)[0]
    if len(s) == 2:
        a, b = list(s)
        if '.' in (a, b):
            return None
        if 'T' in (a, b):
            return a if a != 'T' else b
    return None


def calc(text):
    for i in range(4):
        lst = list(text[i][j] for j in range(4))
        if check_lst(lst):
            return check_lst(lst) + " won"

    for i in range(4):
        lst = list(text[j][i] for j in range(4))
        if check_lst(lst):
            return check_lst(lst) + " won"

    lst = list(text[i][i] for i in range(4))
    if check_lst(lst):
        return check_lst(lst) + " won"

    lst = list(text[i][3 - i] for i in range(4))
    if check_lst(lst):
        return check_lst(lst) + " won"

    if len(list(filter(lambda x: x, ['.' in x for x in text]))) > 0:
        return "Game has not completed"
    return "Draw"



if __name__ == '__main__':
    cnt = int(input())
    for T in range(cnt):
        text = [input() for i in range(4)]
        print("Case #{}: {}".format(T + 1, calc(text)))
        if T < cnt - 1:
            input()

