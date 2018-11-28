#! /usr/bin/env python3

def main():
    t = int(input())
    for i in range(t):
        smax, shyness = input().split(' ')
        shyness = list(map(int, shyness))
        print('Case #{}: {}'.format(i + 1, solve(shyness)))

def solve(shyness):
    acc = 0
    gap = 0
    for i, n in enumerate(shyness):
        gap = max(gap, i - acc)
        acc += n
    return gap


if __name__ == '__main__':
    main()
