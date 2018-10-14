'''
def check(unicorns):
    if unicorns[1] > unicorns[4]-1:
        return False
    elif unicorns[3] > unicorns[0]-1:
        return False
    elif unicorns[5] > unicorns[2]-1:
        return False

    blue = unicorns[4] - unicorns[1]
    red = unicorns[0] - unicorns[3]
    yellow = unicorns[2] - unicorns[5]

    if unicorns[4]-unicorns[1]-1:

    else
        return True
'''
import numpy as np

def solve(unicorns):
    rs = []
    bs = []
    ys = []

    b = ''
    no = unicorns[1]
    for i in range(no):
        b+='BO'
        unicorns[4] -= 1
        unicorns[1] -= 1
        if unicorns[4] < 0:
            return 'IMPOSSIBLE'
    if unicorns[1] == 0 and unicorns[4] == 0:
        if len(b)>0 and sum(unicorns) != 0:
            return 'IMPOSSIBLE'
    else:
        b+='B'
        unicorns[4] -= 1
    if len(b)>0:
        bs.append(b)
    for i in range(unicorns[4]):
        bs.append('B')

    r = ''
    ng = unicorns[3]
    for i in range(ng):
        r+='RG'
        unicorns[0] -= 1
        unicorns[3] -= 1
        if unicorns[0] < 0:
            return 'IMPOSSIBLE'
    if unicorns[3] == 0 and unicorns[0] == 0:
        if len(r)>0 and sum(unicorns) != 0:
            return 'IMPOSSIBLE'
    else:
        r+='R'
        unicorns[0] -= 1
    if len(r)>0:
        rs.append(r)
    for i in range(unicorns[0]):
        rs.append('R')

    y = ''
    nv = unicorns[5]
    for i in range(nv):
        y+='YV'
        unicorns[2] -= 1
        unicorns[5] -= 1
        if unicorns[2] < 0:
            return 'IMPOSSIBLE'
    if unicorns[5] == 0 and unicorns[2] == 0:
        if len(y)>0 and sum(unicorns) != 0:
            return 'IMPOSSIBLE'
    else:
        y+='Y'
        unicorns[2] -= 1
    if len(y)>0:
        ys.append(y)
    for i in range(unicorns[2]):
        ys.append('Y')

    N = sum([len(rs), len(bs), len(ys)])

    colors = [[len(rs), rs], [len(bs), bs], [len(ys), ys]]
    colors.sort(reverse=True)

    ans = ''
    if N == 1 and len(colors[0][1][0])%2==0:
        ans = colors[0][1][0]
    elif colors[0][0] <= N / 2:
        d = (colors[1][0] + colors[2][0]) - colors[0][0]
        for r, y, b in zip(colors[0][1][:d], colors[1][1][:d], colors[2][1][:d]):
            ans += r+y+b
        for i in range(3):
            colors[i][0] -= d

        for r, y in zip(colors[0][1][d:], colors[1][1][d:]):
            ans += r+y
        for r, b in zip(colors[0][1][d+colors[1][0]:], colors[2][1][d:]):
            ans += r+b

    else:
        return 'IMPOSSIBLE'
    return ans


def main():
    T = int(input())
    for i in range(T):
        unicorns = [int(i) for i in input().split()]
        print('Case #{}:'.format(i+1), solve(unicorns[1:]))

if __name__ == '__main__':
    main()
