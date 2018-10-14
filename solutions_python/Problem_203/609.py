import collections


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        R, C = map(int, raw_input("").split())
        matrix = []
        for i in range(R):
            row = list(raw_input())
            matrix.append(row)
        res = helper(matrix, R, C)
        print "Case #{}:".format(num)
        for row in res:
            print ''.join(map(str, row))


def helper(matrix, R, C):
    temp = [[0 for _ in range(C)] for _ in range(R)]
    res = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(len(matrix)):
        next = None
        for j in range(len(matrix[i])):
            if matrix[i][j] != '?':
                next = matrix[i][j]
                break
        for j in range(len(matrix[i])):
            if not next:
                continue
            if matrix[i][j] == '?':
                temp[i][j] = next
            else:
                temp[i][j] = matrix[i][j]
                if matrix[i][j] != next:
                    next = matrix[i][j]
    for i in range(R):
        next = None
        if temp[i][0] == 0:
            for j in range(i + 1, R):
                if temp[j][0] != 0:
                    next = j
                    break
            if next:
                for j in range(C):
                    temp[i][j] = temp[next][j]
            else:
                pre = None
                for j in range(i-1, -1, -1):
                    if temp[j][0] != 0:
                        pre = j
                        break
                for j in range(C):
                    temp[i][j] = temp[pre][j]

    return temp


if __name__ == '__main__':
    main()
