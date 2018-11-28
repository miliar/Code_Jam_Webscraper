#!/usr/bin/env python3
def solve(s_max, shyness):
    standing = 0
    num_friends = 0
    for i in range(s_max+1):
        if i > standing:
            num_friends += i - standing
            standing += i - standing

        standing += int(shyness[i])

    return num_friends


def main():
    num_cases = int(input())
    for case in range(num_cases):
        s_max, shyness = input().split()
        num_friends = solve(int(s_max), shyness)
        print("Case #{}: {}".format(case+1, num_friends))


if __name__ == '__main__':
    main()
