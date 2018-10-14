#!/usr/bin/env python
def solver(p, k):
    idx = p.find('-')
    if idx == -1:
        return 0
    p = list(p[idx:])
    step = 0
    while len(p) >= k:
        step += 1

        for i in range(k):
            p[i] =  '+' if p[i] == '-' else '-'
        try:
            idx = p.index('-')
            p = p[idx:]
        except Exception as e:
            p = []

    try:
        idx = p.index('-')
    except Exception as e:
        idx = -1
    if idx == -1:
        return step
    return 'IMPOSSIBLE'

def main():
    cases = int(input())
    for i in range(cases):
        p, k = input().split(" ")
        sol = solver(p, int(k))
        print("Case #{}: {}".format(i+1, sol))

if __name__ == '__main__':
    main()