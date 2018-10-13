# Template
import string

def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        R, C = list(map(int, input().split()))
        grid = []
        for row in range(R):
            rowstring = input()
            grid.append(list(rowstring))

        done = []
        # Expand letters greedy
        for letter in list(string.ascii_uppercase):
            for row in range(R):
                for col in range(C):
                    letter = grid[row][col]
                    if grid[row][col] != "?" and (letter not in done):
                        # Expand and update grid
                        lidx = col
                        ridx = col
                        # Expand left
                        for l in range(col - 1, -1, -1):
                            if grid[row][l] == "?":
                                grid[row][l] = letter
                                lidx = l
                            else:
                                break
                        # Expand right
                        for r in range(col + 1, C):
                            if grid[row][r] == "?":
                                grid[row][r] = letter
                                ridx = r
                            else:
                                break
                        # Expand up
                        for up in range(row - 1, -1, -1):
                            part = grid[up][lidx:ridx+1]
                            if part.count("?") == len(part):
                                for i in range(lidx, ridx + 1):
                                    grid[up][i] = letter
                            else:
                                break

                        # Expand down
                        for down in range(row + 1, R):
                            part = grid[down][lidx:ridx+1]
                            if part.count("?") == len(part):
                                for i in range(lidx, ridx + 1):
                                    grid[down][i] = letter
                            else:
                                break
                        #letter = grid[row][col]
                        done.append(letter)

        print("Case #{}:".format(test_case + 1))
        for row in grid:
            print("".join(row))

def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
