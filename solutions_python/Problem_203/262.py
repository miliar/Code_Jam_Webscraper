# -*- coding: utf-8 -*-


def is_blank(row):
    for c in row:
        if c != '?':
            return False
    return True


def g(row):
    for i in range(len(row)):
        if row[i] == '?':
            if i > 0 and row[i - 1] != '?':
                row[i] = row[i - 1]
            else:
                j = i + 1
                while j < len(row):
                    if row[j] != '?':
                        row[i : j] = row[j] * (j - i)
                        break
                    j += 1
            assert(row[i] != '?')

    return row


def f(R, C, grid):
    for i in range(R):
        if not is_blank(grid[i]):
            grid[i] = g(grid[i])

    for i in range(R):
        if is_blank(grid[i]):
            if i > 0 and not is_blank(grid[i - 1]):
                grid[i] = list(grid[i - 1])
            else:
                j = i + 1
                found = False
                while j < R and not found:
                    if not is_blank(grid[j]):
                        for k in range(i, j):
                            grid[k] = list(grid[j])
                            found = True
                            break

                    j += 1

    return grid


def main():
    T = int(input())
    for i in range(T):
        x = i + 1
        print("Case #%d:" % x)

        R, C = input().split()
        R = int(R)
        C = int(C)

        grid = []
        for j in range(R):
            grid.append(list(input()))
        # for j in range(R):
        #     print(''.join(grid[j]))
        # print('--')

        ans = f(R, C, grid)

        for j in range(R):
            print(''.join(ans[j]))


if __name__ == '__main__':
    main()
