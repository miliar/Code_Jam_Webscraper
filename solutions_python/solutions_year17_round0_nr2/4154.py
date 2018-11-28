#!/usr/bin/env python3

def pred(c):
    if c == '0':
        return '9'
    return chr(ord(c) - 1)

def lstrip(n, char='0'):
    l = list(n)
    while l[0] == char:
        l = l[1:]
    return ''.join(l)

def tidyup(n):
    l = len(n)
    if l == 1:
        return n
    for i in range(l-1):
        if n[i] > n[i+1]:
            return tidyup(n[:i] + pred(n[i])) + '9' * (l-i-1)
    return n

def main():
    t = int(input())
    for i in range(1, t+1):
        n = input()
        print("Case #{}: ".format(i), end='')
        res = tidyup(n)
        print(lstrip(res))

if __name__ == '__main__':
    main()
