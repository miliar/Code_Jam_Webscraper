#!/usr/bin/env python3
from typing import List, Optional

for case_num in range(int(input())):
    cake = [list(input()) for _ in range(int(input().split()[0]))]
    prev_row: List[str] = None
    for row_num in range(len(cake)):
        row = cake[row_num]
        if not all(i == '?' for i in row):  # if not all question marks
            prev_filled: Optional[str] = None
            for cell_num in range(len(row)):
                if row[cell_num] == '?':
                    if prev_filled is not None:
                        row[cell_num] = prev_filled
                else:
                    if prev_filled is None:
                        prev_filled = row[cell_num]
                        for i in range(cell_num):
                            row[i] = prev_filled
                    else:
                        prev_filled = row[cell_num]
            if prev_row is None:
                prev_row = row
                for i in range(row_num):
                    cake[i] = row
            else:
                prev_row = row
        else:
            if prev_row is not None:
                cake[row_num] = prev_row
    print('Case #%d:' % (case_num + 1))
    print('\n'.join(''.join(i) for i in cake))
