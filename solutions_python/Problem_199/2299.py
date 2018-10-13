# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:28:42 2017

@author: arena
"""

def all_happy(row):
    if set(row) == {'+'}:
        return True
    else: return False
def flip_row(row):
    for r in range(len(row)):
        if row[r] == '+':
            row[r] = '-'
        else:
            row[r] = '+'
    return row
T = int(input())
for t in range(T):
    row, flip = input().split(' ')
    flip = int(flip)
    row = list(row)
    f = 0
    for i in range(0, len(row) - flip + 1):
        if row[i] == '-':
            row[i:i+flip] = flip_row(row[i:i+flip])
            f += 1
    if all_happy(row):
        print("Case #" + str(t+1) + ": ", end = "")
        print(f)
    else:
        print("Case #" + str(t+1) + ": ", end = "")
        print("IMPOSSIBLE")
            