#!/usr/bin/env python
from sys import stdin


def process():
    line = stdin.readline().split(" ")
    length = int(line[0])
    n = int(line[1])

    max_time = 0
    for i in range(n):
        line = stdin.readline().split(" ")
        dist = length - int(line[0])
        speed = int(line[1])
        time = dist / speed
        max_time = max(max_time, time)

    return length / max_time # speed


def main():
    N = int(stdin.readline())
    for i in range(N):
        print("Case #{}: {}".format(i + 1, process()))

if __name__ == '__main__':
    main()
