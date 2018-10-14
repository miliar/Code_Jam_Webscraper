#!/usr/bin/env python3


def stable_combination(unicorns):
    unicorns.sort()
    combination = ''
    n_intersect = unicorns[0][0] + unicorns[1][0] - unicorns[2][0]
    if n_intersect < 0:
        return 'IMPOSSIBLE'
    for _ in range(unicorns[0][0]-n_intersect):
        combination += unicorns[0][1] + unicorns[2][1]
    for _ in range(n_intersect):
        combination += unicorns[0][1] + unicorns[1][1] + unicorns[2][1]
    for _ in range(unicorns[1][0]-n_intersect):
        combination += unicorns[1][1] + unicorns[2][1]
    return combination


def main():
    for case in range(int(input())):
        _, nr, _, ny, _, nb, _ = [int(n) for n in input().split()]
        answer = stable_combination([[nr, 'R'], [ny, 'Y'], [nb, 'B']])
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
