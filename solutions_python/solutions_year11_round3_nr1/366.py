#!/usr/bin/env python3
T = int(input())

def swap(row, j, top=True):
    if top:
        s = '/\\'
    else:
        s = '\\/'

    tmp = row[:j] + s
    if j + 2 < len(row):
        tmp += row[j+2:]

    return tmp

def possible(r):
    count = 0
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == '#':
                count += 1

    if count % 4: 
        return False

    i = 0
    while i < len(r):
        j = 0
        while j < len(r[0]):
            if r[i][j] == '#':
                ps = [
                (i + 1 < len(r)) and r[i+1][j] == '#',
                (j + 1 < len(r[0])) and r[i][j+1] == '#',
                (i + 1 < len(r)) and (j + 1 < len(r[0])) and (r[i+1][j+1]) == '#'
                ]
                for p in ps:
                    if not p:
                        return False

                r[i] = swap(r[i], j)
                r[i+1] = swap(r[i+1],j, False)

#                print('----')
#                for k in range(len(r)):
#                    print(r[k])
            j += 1
        i += 1

    return True

for case in range(T):
    [R, C] = list(map(int, input().split()))
    rows = [input() for i in range(R)]
    print('Case #{0}:'.format(case + 1))
    if not possible(rows):
        print("Impossible")
    else:
        for i in range(len(rows)):
            print(rows[i])

