#!/usr/bin/env python3

num_cases = int(input())

for i in range(num_cases):
    row1 = int(input())
    arr1 = [[int(x) for x in row.split()] for row in (input(), input(), input(), input())]

    row2 = int(input())
    arr2 = [[int(x) for x in row.split()] for row in (input(), input(), input(), input())]

    possibilities = set(arr1[row1 - 1]).intersection(arr2[row2 - 1])
    if len(possibilities) == 1:
        print("Case #{}: {}".format(i + 1, possibilities.pop()))
    elif len(possibilities) > 1:
        print("Case #{}: Bad magician!".format(i + 1))
    else:
        print("Case #{}: Volunteer cheated!".format(i + 1))
