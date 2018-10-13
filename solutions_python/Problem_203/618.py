import re
import sys

def pullUp(arr):
    if ('?' in arr[0]):
        return pullUp(arr[1:])
    return arr[0]

for i in range(int(input())):
    rowCol = sys.stdin.readline().rstrip()
    rowCol = rowCol.split(" ")
    rows = []
    for j in range(int(rowCol[0])):
        row = sys.stdin.readline().rstrip()
        firstCharIndex = -1
        for m in range(len(row)):
            if not row[m] == '?':
                firstCharIndex = m
                break
        if ('?' in row and firstCharIndex > -1):
            row = row[firstCharIndex] * (firstCharIndex + 1) + row[firstCharIndex + 1:]
            for k in range(len(row) - firstCharIndex):
                if (row[k+firstCharIndex] == '?'):
                    row = row[:k + firstCharIndex] + row[firstCharIndex + k - 1] + row[firstCharIndex + k + 1:]
        rows.append(row)
    for l in range(int(rowCol[0])):
        if ('?' in rows[l]):
            if (l > 0 and not '?' in rows[l - 1]):
                rows[l] = rows[l-1]
            else:
                rows[l] = pullUp(rows[l+1:])
    print("Case #" + str(i+1) + ":")
    for row in rows:
        print(row)