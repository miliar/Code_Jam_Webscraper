import re

only_dots = re.compile("^\.*$")

def solve(rows, columns):
    turns = 0
    for row_index, row in enumerate(rows):
        for column_index, column in enumerate(columns):
            cell = row[column_index]

            if cell != '.' and row.count('.') == len(row) - 1 and column.count('.') == len(column) - 1:
                return "IMPOSSIBLE"
            
            if cell == '<' and only_dots.match(row[:column_index]):
                turns += 1
            if cell == '>' and only_dots.match(row[column_index + 1:]):
                turns += 1
            if cell == '^' and only_dots.match(column[:row_index]):
                turns += 1
            if cell == 'v' and only_dots.match(column[row_index + 1:]):
                turns += 1
    return turns

testcase_count = int(input())
for testcase_index in range(1, testcase_count + 1):
    row_count, column_count= [int(x) for x in input().split()]
    rows = []
    for row_index in range(row_count):
        rows.append(input())
    columns = []
    for column_index in range(column_count):
        column = []
        for row in rows:
            column.append(row[column_index])
        columns.append(''.join(column))
    
    result = str(solve(rows, columns))

    print("Case #%d: %s" % (testcase_index, result))