#!/usr/bin/env python3

def f(s):
    r = []
    for c in s:
        if c == 'Z':
            r.append(0)
            s = replace('ZERO', s)
        elif c == 'W':
            r.append(2)
            s = replace('TWO', s)
        elif c == 'X':
            r.append(6)
            s = replace('SIX', s)
        elif c == 'G':
            r.append(8)
            s = replace('EIGHT', s)
    for c in s:
        if c == 'S':
            r.append(7)
            s = replace('SEVEN', s)
        if c == 'T':
            r.append(3)
            s = replace('THREE', s)
    for c in s:
        if c == 'V':
            r.append(5)
            s = replace('FIVE', s)
    for c in s:
        if c == 'F':
            r.append(4)
            s = replace('FOUR', s)
        if c == 'I':
            r.append(9)
            s = replace('NINE', s)
    for c in s:
        if c == 'E':
            r.append(1)
            s = replace('ONE', s)
    r.sort()
    return r

def replace(s0, s):
    for c in s0:
        s = s.replace(c, '', 1)
    return s

def print_answer(n, result):
    res = ""
    if type(result) in [list, tuple]:
        res = "".join(map(str, result))
    elif type(result) == int:
        res = str(result)
    elif type(result) == str:
        res = result
    print("Case #{}: {}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        s = input()
        print_answer(t + 1, f(s))

if __name__ == "__main__":
    main()
