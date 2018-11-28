#!/usr/bin/env python3

def main():
    #"The first line of the input gives the number of test cases, T."
    t = int(input())
    for i in range(t):
        "Each line describes a test case with a single integer N, the last number counted by Tatiana."
        ans = solve(int(input()))
        
        print("Case #%d: %s" % (i+1, ans))


def solve(n):
    digits = list(map(int, str(n)))
    return int(''.join(map(str, recurse(digits))))


def recurse(digits):
    first, *rest = digits
    if len(rest) == 0:
        return [first]
    rest = recurse(rest)
    if first <= rest[0]:
        return [first] + rest
    else: #first > 0
        return [first-1] + [9]*len(rest)


main()
