#! /usr/bin/env python
import sys

def main():
    t = int(raw_input())
    for i in xrange(t):
        line = raw_input().split()
        n, line = int(line[0]), line[1:]
        presses = zip(map(botcode, line[::2]), map(int, line[1::2]))
        assert len(presses) == int(n)
        print 'Case #%d:' % (i + 1), solve(presses)

def botcode(c):
    return 0 if c == 'O' else 1

def solve(presses):
    pos = [1, 1]
    time = [0, 0]
    for robot, button in presses:
        time[robot] += abs(pos[robot] - button) + 1
        pos[robot] = button
        other = 1 - robot
        if time[robot] < time[other] + 1:
            time[robot] = time[other] + 1
    return max(time)


if __name__ == '__main__':
    sys.exit(main())
