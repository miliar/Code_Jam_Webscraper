#!/usr/bin/env python
def solver(n):
    if len(n) == 1:
        return n
    try:
        idx = next(i for i in range(len(n) - 1) if n[i] > n[i+1])
    except Exception as e:
        return n
    sol = n[:idx] + chr(ord(n[idx]) - 1) + '9'*(len(n) - idx - 1)
    return int(sol)

def main():
    cases = int(input())
    for i in range(cases):
        n = input()
        sol = solver(n)
        print("Case #{}: {}".format(i+1, sol))

if __name__ == '__main__':
    main()