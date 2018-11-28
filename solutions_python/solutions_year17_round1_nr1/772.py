import sys
import time

def get_next_space(start,line):
    for i in range(start,len(line)):
        if line[i] == ' ':
            return i
    return len(line)

def get_chars(line):
    start = 0
    to_return = []
    while start < len(line):
        end=  get_next_space(start,line)
        to_return.append(int(line[start:end]))
        start = end+1
    return to_return


def parse(lines):
    i = 1
    cakes = []
    while i < len(lines):
        rows = get_chars(lines[i])[0]
        cols = get_chars(lines[i])[1]
        cake = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                cake[r][c] = lines[i+1+r][c]
        cakes.append(cake)
        i += rows + 1
    return cakes

def get_first_non_mark(arr):
    for a in arr:
        if a != '?':
            return a
    return '?'

def fill_in_cake(cake):
    #fill in non empty rows
    for row in cake:
        current = get_first_non_mark(row)
        for i in range(len(row)):
            if row[i] == '?':
                row[i] = current
            else:
                current = row[i]
   
    cont = True
    while cont:
        cont = False
        for row in range(len(cake)):
            if get_first_non_mark(cake[row]) == '?':
                cont = True
                for col in range(len(cake[row])):
                    if row == 0 and cake[row+1][col] != '?':
                        cake[row][col] = cake[row+1][col]
                    elif cake[row-1][col] != '?':
                        cake[row][col] = cake[row-1][col]


def arr_to_str(arr):
    to_return = ''
    for a in arr:
        to_return = to_return+a
    return to_return

lines = open(sys.argv[1]).readlines()

cakes =  parse(lines)
for i in range(len(cakes)):
    fill_in_cake(cakes[i])
    print "Case #%d:"%(i+1)
    for row in cakes[i]:
        print arr_to_str(row)
