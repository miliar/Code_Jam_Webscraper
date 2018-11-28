#!/usr/bin/python3

def solve(S):
    result = 0
    stoodups = 0

    for i, s in enumerate(S):
        if stoodups >= i:
            stoodups += s
        elif s > 0:
            invites = i - stoodups
            result += invites
            stoodups += invites + s

    return result

def main():
    T = int(input())

    for i in range(T):
        _, S = input().split()
        S = [int(s) for s in S]

        result = solve(S)

        print('Case #{0}: {1}'.format(i+1, result))

if __name__ == '__main__':
    main()
