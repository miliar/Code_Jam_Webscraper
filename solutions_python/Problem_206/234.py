import sys

# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt0.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it():
    d, n= list(map(int, input().split()))
    s = []
    k = []
    for i in range(n):
        _k, _s = list(map(int, input().split()))
        s.append(_s)
        k.append(_k)
    t = 0.0
    for i in range(n):
        tt = (d - k[i]) / s[i]
        if tt > t:
            t = tt
    res = d / t
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
