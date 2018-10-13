import sys
from collections import defaultdict
# sys.stdin = open('b1.in')
sys.stdin = open('B-small-attempt0.in')
# sys.stdin = open('B-large.in')
sys.stdout = open('out.txt', 'w')


def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def solve_it0():
    rides, promotions = solve_it()
    return '{} {}'.format(rides, promotions)


def solve_it():
    n, c, m = read_int_list()
    a = [[0] * 1001 for i in range(c)]
    pb = []
    for i in range(m):
        p, b = read_int_list()
        p -= 1
        b -= 1
        a[b][p] += 1
        pb.append((p,b))
    if a[0][0] + a[1][0] > max(sum(a[0]), sum(a[1])):
        return a[0][0] + a[1][0], 0
    rides = max(sum(a[0]), sum(a[1]))
    for j in range(1001):
        if a[0][j] + a[1][j] > rides:
            conflicts = a[0][j] + a[1][j] - rides
            return rides, conflicts
    return rides, 0


def main():

    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it0()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)

if __name__ == '__main__':
    main()
