#!/usr/bin/python

with open('b.large') as fin:
    cases = int(fin.next())
    for testNo in range(1, cases + 1):
        y, x = (int(j) for j in fin.next()[:-1].split())
        rows = [[int(j) for j in fin.next()[:-1].split()] for i in range(y)]

        columns = [[rows[i][j] for i in range(y)] for j in range(x)] 

        maxRow    = [max(row) for row in rows]
        maxColumn = [max(column) for column in columns]

        try:
            for py in range(y):
                for px in range(x):
                    if rows[py][px] != maxRow[py] and rows[py][px] != maxColumn[px]:
                        raise Exception

            print "Case #{0}: YES".format(testNo)

        except Exception as e:
            print "Case #{0}: NO".format(testNo)
