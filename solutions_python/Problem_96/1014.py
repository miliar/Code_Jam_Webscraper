#/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Régis Décamps'

FILENAME = "B-large"

def solve(n, s, p, scores):
    y = 0
    for score in scores:
        if score >= p + 2*max(0,p - 1):
            # not surprising and above
            y += 1
        elif score >= p + 2*max(0,p - 2) and s > 0:
            # surprising result
            y += 1
            s -= 1
        else:
            # score does not permit to reach p
            pass
    return y


def solve_input(line):
    data=line.split()
    n = int(data[0])
    s = int(data[1])
    p = int(data[2])
    scores = map(lambda x: int(x),data[3:])
    return solve(n, s, p, scores)

if __name__ == '__main__':
    with open('dataset/' + FILENAME + '.in', 'r') as f:
        nbcases = int(f.readline())
        for i in range(1, nbcases + 1):
            y = solve_input(f.readline())
            print("Case #{i}: {result}".format(i=i, result=y))

