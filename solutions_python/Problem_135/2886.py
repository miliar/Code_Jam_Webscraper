#!/usr/bin/python

if __name__ == "__main__":
    cases = int(raw_input())
    current = 1
    testreport = []
    while current <= cases:
        row1 = int(raw_input()) - 1
        matrix1 = []
        for i in range(0, 4):
            matrix1.append(raw_input().split(' '))
        row2 = int(raw_input()) - 1
        matrix2 = []
        for i in range(0, 4):
            matrix2.append(raw_input().split(' '))
        result = 0
        matched = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if matrix1[row1][i] == matrix2[row2][j]:
                    result = matrix1[row1][i]
                    matched += 1
        if matched == 0:
            testreport.append((current, 'Volunteer cheated!'))
        elif matched > 1:
            testreport.append((current, 'Bad magician!'))
        else:
            testreport.append((current, result))
        current += 1

    for i in range(0, cases):
        print "Case #" + str(testreport[i][0]) + ": " + testreport[i][1]
