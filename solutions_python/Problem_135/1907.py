#!/usr/bin/env python3

def read_row():
    row = int(input())

    for i in range(row - 1):
        input()

    row_set = set(map(int, input().split()))

    for i in range(4 - (row - 1) - 1):
        input()

    return row_set

cases = int(input())
for i in range(1, cases + 1):
    first = read_row()
    second = read_row()

    if len(first & second) == 1:
        print("Case #" + str(i) + ": " + str((first & second).pop()))
    elif len(first & second) > 1:
        print("Case #" + str(i) + ": Bad magician!")
    elif not (first & second):
        print("Case #" + str(i) + ": Volunteer cheated!")
