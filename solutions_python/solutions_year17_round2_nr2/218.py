import sys

# sys.stdin = open('b1.in')
# sys.stdin = open('B-small-attempt0.in')
sys.stdin = open('B-small-attempt1.in')
# sys.stdin = open('B-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it():
    impossible = 'IMPOSSIBLE'
    n, r, o, y, g, b, v = list(map(int, input().split()))
    # if n // 2 < max(r, y, b):
    #     return impossible

    t = [[r,'R'], [y, 'Y'], [b, 'B']]
    t.sort(reverse=True)
    c = [t[0][1]] * t[0][0]
    p = len(c)
    for i in range(1,3):
        for j in range(t[i][0]):
            c.insert(p, t[i][1])
            p -= 1
            if p == -1:
                p = len(c) - 1
    res = ''.join(c)
    if res[0] == res[-1]:
        return impossible
    # assert res[0] != res[-1]
    for pattern in ['YY', 'RR', 'BB']:
        if res.find(pattern) > -1:
            return impossible
        # assert res.find(pattern) == -1
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
