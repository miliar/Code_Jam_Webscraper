def cut_cake(grid):
    row, col = len(grid), len(grid[0])
    clone = [[grid[r][c] for c in range(col)] for r in range(row)]

    for r in range(row):
        for c in range(col):
            if grid[r][c] != "?":
                maximize_neighbours(clone, grid, r, c)
    return clone


def maximize_neighbours(clone, grid, r, c):
    left_bound = c
    target_initial = grid[r][c]
    if c > 0:
        left_nbr = c - 1
        while left_nbr >= 0 and clone[r][left_nbr] == "?":
            clone[r][left_nbr] = target_initial
            left_bound -= 1
            left_nbr -= 1
    right_bound = c
    if c < len(grid[0]) - 1:
        right_nbr = c + 1
        while right_nbr < len(grid[0]) and clone[r][right_nbr] == "?":
            clone[r][right_nbr] = target_initial
            right_nbr += 1
            right_bound += 1
    # going up
    upper_bound = r
    if r > 0:
        upper = r - 1
        unmatched = False
        while upper >= 0:
            for cur_r in range(upper, upper_bound):
                for cur_c in range(left_bound, right_bound + 1):
                    if (clone[cur_r][cur_c] != "?"):
                        unmatched = True
                        break
            if unmatched:
                break
            else:
                for cur_r in range(upper, upper_bound):
                    for cur_c in range(left_bound, right_bound + 1):
                        clone[cur_r][cur_c] = target_initial
                upper_bound -= 1
                upper -= 1
    lower_bound = r
    if r < len(grid) - 1:
        lower = r + 1
        unmatched = False

        while lower <= len(grid) - 1:
            for cur_r in range(lower_bound + 1, lower + 1):
                for cur_c in range(left_bound, right_bound + 1):
                    if (clone[cur_r][cur_c] != "?") :
                        unmatched = True
                        break
            if unmatched:
                break
            else:

                for cur_r in range(lower_bound + 1, lower + 1):
                    for cur_c in range(left_bound, right_bound + 1):
                        clone[cur_r][cur_c] = target_initial
                lower_bound += 1
                lower += 1


def main():
    """The main driver"""
    n_tests = int(input())
    for i in range(n_tests):
        row, col = [int(i) for i in input().split()]
        grid = []
        for r in range(row):
            cur_row = []
            row_string = input()
            for c in range(col):
                cur_row.append(row_string[c])
            grid.append(cur_row)
        # print("INput #{}:".format(i + 1))
        # for r in grid:
        #     print("".join(r))
        res = cut_cake(grid)
        print("Case #{}:".format(i + 1))
        for r in res:
            print("".join(r))


if __name__ == "__main__":
    main()
