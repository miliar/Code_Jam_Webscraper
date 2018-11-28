import numpy as np

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            R, C = map(int, f.readline().split())
            rows = []
            for _ in range(R):
                rows.append(f.readline().strip())
            sol = solve(R, C, rows)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return

def one_line(row):
    #assert row != '?' * len(row)
    for c in row:
        if c != '?':
            first = c
            break
    res = []
    char_to_fill = first
    for c in row:
        if c == '?':
            res.append(char_to_fill)
        else:
            char_to_fill = c
            res.append(char_to_fill)
    return ''.join(res)

def solve(R, C, rows):
    for row in rows:
        if row != '?' * len(row):
            first_row = row
            break
    res = []
    row_to_fill = one_line(first_row)
    for row in rows:
        if row == '?' * len(row):
            res.append(row_to_fill)
        else:
            row_to_fill = one_line(row)
            res.append(row_to_fill)
    return '\n'+'\n'.join(res)



dir = "./"

input_file = dir+"A-test.in"
output_file = dir+"A-test.txt"

input_file = dir+"A-small-attempt0.in"
output_file = dir+"A-small-attempt0.out"

input_file = dir+"A-large.in"
output_file = dir+"A-large.out"
'''
'''
parse(input_file, output_file)


