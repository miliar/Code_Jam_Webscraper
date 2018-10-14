#!/usr/bin/env python

def Solve(arr):
    result = 0
    changed = 0
    outputDic = {}
    xLinesX = [0]*len(arr)
    xLinesY = [0]*len(arr)
    pLines1 = [0]*(2*len(arr)-1)
    pLines2 = [0]*(2*len(arr)-1)
    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            if arr[i][j] == 'x':
                xLinesX[i] = 1
                xLinesY[j] = 1
                result += 1
            elif arr[i][j] == 'o':
                xLinesX[i] = 1
                xLinesY[j] = 1
                pLines1[i+j] = 1
                pLines2[len(arr)-1-i + j] = 1
                result += 2
            elif arr[i][j] == '+':
                pLines1[i+j] = 1
                pLines2[len(arr)-1-i + j] = 1
                result += 1

    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            if arr[i][j] == '.' and xLinesX[i] != 1 and xLinesY[j] != 1:
                xLinesX[i] = 1
                xLinesY[j] = 1
                arr[i][j] = 'x'
                outputDic[(i+1, j+1)] = 'x'
                result += 1
                changed += 1

    for i in [len(arr)-1, 0]:
        for j in xrange(len(arr)):
            if arr[i][j] == '.' and pLines1[i+j] != 1 and pLines2[len(arr)-1-i + j] != 1:
                pLines1[i+j] = 1
                pLines2[len(arr)-1-i + j] = 1
                arr[i][j] = '+'
                outputDic[(i+1, j+1)] = '+'
                result += 1
                changed += 1

    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            if (arr[i][j] == '+' and xLinesX[i] != 1 and xLinesY[j] != 1) or (arr[i][j] == 'x' and pLines1[i+j] != 1 and pLines2[len(arr)-1-i + j] != 1):
                xLinesX[i] = 1
                xLinesY[j] = 1
                pLines1[i+j] = 1
                pLines2[len(arr)-1-i + j] = 1
                arr[i][j] = 'o'
                if (i+1, j+1) not in outputDic:
                    changed += 1
                outputDic[(i+1, j+1)] = 'o'
                result += 1

    output = [outputDic[(key0, key1)] + " " + str(key0) + " " + str(key1) for key0, key1 in outputDic]
    return result, changed, output



def main():
    with open("d.txt") as _in, open("d_out.txt", "w") as _out:
        i = -1
        step = 0
        n = 0
        m = 0
        im = 0
        matrix = []
        iss = 0
        for line in _in:
            i += 1
            if i == 0:
                continue
            parts = line.rstrip().split(" ")
            if step == 0:
                iss += 1
                step+=1
                n = int(parts[0])
                m = int(parts[1])
                matrix = [['.']*n for r in xrange(n)]

            if step == 2 and im < m:
                im += 1
                matrix[int(parts[1])-1][int(parts[2])-1] = parts[0]

            step = 2

            if im == m:
                step = 0
                im = 0
                res, changed, output = Solve(matrix)
                _out.write("Case #" + str(iss) + ": " + str(res) + " " + str(changed) + "\n")
                for j in output:
                    _out.write(j + "\n")


if __name__ == "__main__":
    main()
