#!/usr/bin/env python
#coding:utf-8

def solve(N,S,p,dancers):
    sp = 0
    ret = 0
    best_scores = []
    _dancers = []
    for dan in dancers:
        if dan < 2:
            if p <= dan%2:
                ret = ret + 1

        elif dan >= 29:
            ret = ret + 1

        else:
            _dancers.append(dan)

    dancers = _dancers[:]
    _dancers = []
    for dan in dancers:
        if dan % 3 == 0:
            if dan/3 >= p:
                ret = ret + 1
            else:
                _dancers.append(dan)
        else:
            if int(dan/3) +1 >= p:
                ret = ret + 1
            else:
                if dan % 3 == 2:
                    _dancers.append(dan)

    dancers = _dancers[:]

    for dan in reversed(sorted(dancers)):
        if sp >= S:
            break
        if dan % 3 ==0:
            if dan/3+1 >= p:
                ret = ret + 1
                sp = sp + 1
        else:
            if int(dan/3)+2 >= p:
                ret = ret + 1
                sp = sp + 1

    return ret

def main():
    T = int(input())
    for i in range(T):
        inp = input().strip().split(' ')
        inp = [int(i) for i in inp]
        N = inp[0]
        S = inp[1]
        p = inp[2]
        dancer = inp[3:]
        x = solve(N,S,p,dancer)
        print("Case #%d: "%(i+1)+str(x))

if __name__ == "__main__":
    main()
