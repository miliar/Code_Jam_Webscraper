#!/usr/bin/env python3
def solve(x, r, c):
    if x < 7 and (r * c % x == 0) and max(r, c) >= x and min(r, c) >= x-1:
        return "GABRIEL"
    else:
        return "RICHARD"


def main():
    num_cases = int(input())
    for case in range(1, num_cases+1):
        x, r, c = input().split()
        winner = solve(int(x), int(r), int(c))
        print("Case #{}: {}".format(case, winner))


if __name__ == '__main__':
    main()
