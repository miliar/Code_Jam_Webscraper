import sys

BLUE = '#'
RED1 = '/'
RED2 = '\\'

def int_input():
    return int(raw_input())

def list_str_input():
    return raw_input().split()

def list_int_input():
    return map(int, list_str_input())

def list_char_input():
    return list(raw_input())

def table_int_input(h):
    return [list_int_input() for i in range(h)]

def table_char_input(h):
    return [list_char_input() for i in range(h)]

def fill_table(w, h, table):
    for i in range(h-1):
        for j in range(w-1):
            if table[i][j] == BLUE and table[i][j+1] == BLUE and table[i+1][j] == BLUE and table[i+1][j+1] == BLUE:
                table[i][j] = RED1
                table[i][j+1] = RED2
                table[i+1][j] = RED2
                table[i+1][j+1] = RED1 

def is_table_ok(table):
    for row in table:
        for char in row:
            if char == BLUE:
                return False
    return True

def print_table(table):
    for row in table:
        for char in row:
            sys.stdout.write(char)
        print '\n',

def solve(c):
    h, w = list_int_input()
    table = table_char_input(h)
    print 'Case #%d:' % c
    fill_table(w, h, table)
    if is_table_ok(table):
        print_table(table)
    else:
        print 'Impossible'

def main():
    for c in range(int_input()):
        solve(c+1)

main()

