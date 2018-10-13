#!/usr/bin python3

import sys

input = sys.stdin


def data():
    input.readline()
    for l in input:
        yield l.strip()


def results(f=None):
    for i, l in enumerate(data()):
        print ("Case #" + str(i + 1) + ":", f(l))


def calc(l=None):
    N, S, p, *data = map(int, l.split(' '))
    is_ok = 0
    may_be = 0
    for summe in data:
        div, rem = divmod(summe, 3)
        #print(div, rem)
        if rem == 0:
            if div >= p:
                is_ok += 1
            elif div+1 >= p and div-1 > 0:
                may_be += 1
        elif rem == 1:
            if div + 1 >= p:
                is_ok +=1
        elif rem == 2:
            if div + 1 >= p:
                is_ok +=1
            elif div + 2 >= p:
                may_be += 1
    return is_ok+ min([may_be, S])

if __name__ == "__main__":
    f = calc
    results(f)
