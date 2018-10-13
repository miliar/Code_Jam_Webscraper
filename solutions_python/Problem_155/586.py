#!/usr/bin/env python3

def solve(shyness):
    friends = 0
    audience = shyness[0]
    for i, n in enumerate(shyness[1:], start=1):
        if audience < i:
            friends += i-audience
            audience = i
        audience += n
    return friends

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        _, shyness = s.split()
        shyness = [int(c) for c in shyness]
        print('Case #{0}:'.format(i+1), solve(shyness))
