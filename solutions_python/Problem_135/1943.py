#!/usr/bin/python3

def readln(): return tuple(map(int, input().split()))

def solve(case):
    a, = readln()
    begin = [readln() for _ in range(4)][a - 1]
    b, = readln()
    end = [readln() for _ in range(4)]
    row = [0] * 4
    to = [-1] * 4
    for v in begin:
        for i in range(4):
            if v in end[i]:
                row[i] += 1
                to[i] = v
    if row[b - 1] == 1:
        print('Case #%d: %d' % (case, to[b - 1]))
    elif row[b - 1] == 0:
        print('Case #%d: Volunteer cheated!' % case)
    else:
        print('Case #%d: Bad magician!' % case)

if __name__ == '__main__':
    t, = readln()
    for _ in range(t):
        solve(_ + 1)