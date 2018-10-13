import sys
from collections import defaultdict
# sys.stdin = open('b1.in')
# sys.stdin = open('B-small-attempt0.in')
sys.stdin = open('B-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(n):
    digits = list(map(int, list(str(n))))
    m = len(digits)
    while True:
        changed = False
        for i in range(m-1):
            if digits[i] > digits[i+1]:
                digits[i] -= 1
                for j in range(i+1, m):
                    digits[j] = 9
                changed = True
                break
        if not changed:
            break
    res = int(''.join(map(str, digits)))
    return res


def main():

    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        n = int(input())
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it(n)
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)

if __name__ == '__main__':
    main()
