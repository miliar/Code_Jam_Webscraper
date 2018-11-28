#!/bin/env/ python

def check_rows(rows):
    for r in rows:
        x = 0
        o = 0
        for c in r:
            if c == 'X':
                x = x + 1
            elif c == 'O':
                o = o + 1
            elif c == 'T':
                x = x + 1
                o = o + 1

        if x == 4:
            return 'X'
        elif o == 4:
            return 'O'

    return False

def check_columns(rows):
    for col in range(0,4):
        x = 0
        o = 0
        for index in range(0,4):
            if rows[index][col] == 'X':
                x = x + 1
            elif rows[index][col] == 'O':
                o = o + 1
            elif rows[index][col] == 'T':
                o = o + 1
                x = x + 1
       
        if x == 4:
            return 'X'
        elif o == 4:
            return 'O'

    return False

def check_diag(rows):
    rx = 0
    ro = 0
    lx = 0
    lo = 0
    for col, row in enumerate(rows):
        if row[col] == 'X':
            rx = rx + 1
        elif  row[col] == 'O':
            ro = ro + 1
        elif  row[col] == 'T':
            ro = ro + 1
            rx = rx + 1

        if row[3 - col] == 'X':
            lx = lx + 1
        elif row[3 - col] == 'O':
            lo = lo + 1
        elif row[3 - col] == 'T':
            lo = lo + 1
            lx = lx + 1

    if rx == 4 or lx == 4:
        return 'X'
    elif ro == 4 or lo == 4:
        return 'O'

    return False

def check_draw(rows):
    for row in rows:
        if '.' in row:
            return False

    return 'Draw'


with open('A-large.in', 'r') as fd:
    lines = fd.readlines()

num_games = lines[0].strip()
linecount = 1 # next line to be read

for index in range(1, int(num_games) + 1):
    print 'Case #%s:' % index, 

    result = check_rows(lines[linecount:linecount+4])
    if not result:
        result = check_columns(lines[linecount:linecount+4])
        if not result:
            result = check_diag(lines[linecount:linecount+4])
            if not result:
                result = check_draw(lines[linecount:linecount+4])
        

    if result == 'X':
        print 'X won'
    elif result == 'O':
        print 'O won'
    elif result == 'Draw':
        print 'Draw'
    else:
        print 'Game has not completed'

    linecount = linecount + 5

