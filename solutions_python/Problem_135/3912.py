#!/usr/bin/env python3

def get_int():
    return int(input())

def solve():
    choice1 = get_int() - 1
    arr1 = [set(input().split()) for x in range(4)]
    choice2 = get_int() - 1
    arr2 = [set(input().split()) for x in range(4)]
    diff = arr1[choice1] & arr2[choice2]
    if not len(diff):
        return 'Volunteer cheated!'
    if len(diff) > 1:
        return 'Bad magician!'
    return diff.pop()

for x in range(get_int()):
    print('Case #{}: {}'.format(x + 1, solve()))

