import sys


class Solution:
    def process(self, m, n, matrix):
        row_set = set({-1})
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '?':
                    row_set.add(i)

        row_list = list(row_set)
        row_list.sort()
        length = len(row_list)

        for i in range(1, length):
            start = row_list[i - 1]+1
            end = row_list[i]

            if i == length - 1:
                end1 = m - 1
            else:
                end1 = end

            for j in range(n):
                if matrix[end][j] != '?':
                    for t in range(start, end1 + 1):
                        matrix[t][j] = matrix[end][j]

                    for t in range(start, end1 + 1):
                        t1 = j - 1
                        while t1 >= 0 and matrix[t][t1] == '?':
                            matrix[t][t1] = matrix[end][j]
                            t1 -= 1

                        t1 = j + 1
                        while t1 < n and matrix[t][t1] == '?':
                            matrix[t][t1] = matrix[end][j]
                            t1 += 1

# INPUT_FILE_NAME = 'input.in'
INPUT_FILE_NAME = 'A-large.in'
OUTOUT_FILE_NAME = 'a-small.out'

fi = open(INPUT_FILE_NAME, 'r')
fo = open(OUTOUT_FILE_NAME, 'w')

number_test = int(fi.readline())
for i in xrange(1, number_test + 1):
    r, c = [int(s) for s in fi.readline().split(" ")]

    matrix = []
    for j in range(r):
        line = list(fi.readline())
        matrix.append(line)

    solution = Solution()
    solution.process(r, c, matrix)

    print i
    fo.write("Case #%s:\n" % (i))
    for i in range(r):
        fo.write("%s" % "".join(matrix[i]))

fi.close()
fo.close()
