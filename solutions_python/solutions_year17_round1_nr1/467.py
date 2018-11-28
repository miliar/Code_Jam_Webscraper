def find_nearest_right(row, ind):
    for i in range(ind, len(row)):
        if row[i] != '?':
            return i

    return -1


def find_nearest_left(row, ind):
    ans = -1
    for i in range(0, ind + 1):
        if row[i] != '?':
            ans = i

    return ans


def solve(R, C, grid):

    all_empty = list()
    empty_spaces = list()

    for i in range(R):
        flag = True
        for j in range(C):
            if grid[i][j] != '?':
                flag = False

        if flag:
            all_empty.append(i)
        else:
            for j in range(C):
                if grid[i][j] == '?':
                    if j == 0:
                        ind = find_nearest_right(grid[i], j)
                    else:
                        ind = find_nearest_left(grid[i], j)

                    grid[i][j] = grid[i][ind]

    for k in all_empty:
        if k == 0:
            flag = False
            next = k
            while not flag:
                next = next+1
                if next not in all_empty:
                    flag = True

            for m in range(C):
                grid[k][m] = grid[next][m]
        else:
            for m in range(C):
                grid[k][m] = grid[k-1][m]

    for row in range(R):
        rw = ''.join(grid[row])
        print(rw)


if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        line = input().split(" ")
        R = int(line[0])
        C = int(line[1])

        grid = list()

        for i in range(R):
            grid.append(list())
            li = input()
            grid[i].extend(list(li))

        print("Case #%i:" % nth_case)
        solve(R, C, grid)
