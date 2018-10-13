import sys
#sys.stdin = open('a1.in')
sys.stdin = open('b.in')
#sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(f):
    next_digit = f % 10
    f = f / 10
    while f:
        digit = f % 10
        if digit > next_digit:
            return False
        next_digit = digit
        f = f / 10
    return True



def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        n=int(input())
        while not solve_it(n):
            n -= 1
        print 'Case #' + str(test_case) + ':', n


if __name__ == '__main__':
    main()
