#!/usr/bin/env python

import sys

T = input()

def get_row(): 
    index = input()
    grid = [map(int, raw_input().split()) for _ in range(4)]
    return grid[index-1]

for t in range(1, T+1): 
    row = get_row()
    row_m = get_row()
    cnt = 0
    num = -1
    for n in row: 
        if n in row_m: 
            cnt += 1
            num = n
    if cnt == 0: 
        print 'Case #%d: Volunteer cheated!' %(t)
    elif cnt == 1: 
        print 'Case #%d: %d' %(t, num)
    else: 
        print 'Case #%d: Bad magician!' %(t)

