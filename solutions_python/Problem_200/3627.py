#!/usr/bin/env python3

def digits(n):
    dig = []
    while n != 0:
        dig.insert(0, n % 10)
        n = n // 10
    return dig

def nondecreasing(xs):
    for i in range(len(xs) - 1):
        if xs[i + 1] < xs[i]:
            return False
    return True

def lasttidy(n):
    tidy = lambda n: nondecreasing(digits(n))
    for i in range(n, 0, -1):
        if tidy(i):
            return i

def main():
    cases = int(input())
    for c in range(1, cases + 1):
        n = int(input())
        print('Case #{}: {}'.format(c, lasttidy(n)))

if __name__ == '__main__':
    main()
