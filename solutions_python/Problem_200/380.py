#!/usr/bin/env python

def digits(n):
    d = []
    while n >= 10:
        d.append(n%10)
        n //= 10
    d.append(n)
    return d[::-1]

def tidy(n):
    d = digits(n)
    for i in range(len(d) - 1):
        if d[i] > d[i+1]:
            return False
    return True

def last_tidy(n):
    candidate = n
    i = 1
    while not tidy(candidate):
        i *= 10
        candidate = (n//i)*i - 1
    return candidate

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        print(f'Case #{i}: {last_tidy(n)}')
