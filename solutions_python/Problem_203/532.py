#!/usr/bin/env python3
import math

def get(chars, r, c):

    return 

def expand_horizon(chars, R, C, i):
    current_char = chars[i]
    if current_char == "?":
        return
    j = i + 1

    while True:
        if math.floor(i/C) != math.floor(j/C):
            break
        if j >= len(chars):
            break
        if chars[j] == '?':
            chars[j] = current_char
        else:
            break
        if j%C == C-1:
            break
        j += 1

    j = i - 1

    while True:
        if math.floor(i/C) != math.floor(j/C):
            break
        if j < 0:
            break

        if chars[j] == '?':
            chars[j] = current_char
        else:
            break
        if j%C == 0:
            break
        j -= 1

def copy_row(chars, R, C, src, dests):
    for dest_row in dests:
        for i in range(C):
            chars[dest_row * C + i] = chars[src * C + i]

def fill_blank(chars, R, C):
    row_to_fill = []
    for row in range(R):
        j = row * C
        if chars[j] == '?':
            prev = j - C
            if prev >= 0 and chars[prev] != '?':
                copy_row(chars, R, C, row - 1, row_to_fill + [row])
                row_to_fill = []
                continue
            nex = j + C
            if nex < len(chars) and chars[nex] != '?':
                copy_row(chars, R, C, row + 1, row_to_fill + [row])
                row_to_fill = []
                continue
            row_to_fill.append(row)

def solve(case_number, R, C, chars):
    for i in range(len(chars)):
        expand_horizon(chars, R, C, i)
    fill_blank(chars, R, C)

    rows = []
    for i in range(R):
        begin = i*C
        end = i*C + C
        rows.append(''.join(chars[begin:end]))
    print_ans(case_number, rows)

def print_ans(case_number, rows):
    print("Case #%d:"%(case_number))
    for r in rows:
        print(r)

no_test = int(input())
line_num = 1
while no_test > 0:
    sp = input().split(' ')
    chars = []
    r = int(sp[0])
    c = int(sp[1])
    for i in range(r):
        chars += list(input())
    solve(line_num, r, c, chars)
    no_test -= 1
    line_num += 1
